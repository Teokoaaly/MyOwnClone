import { NextResponse } from "next/server";

const BASE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://myownclone.com";

const WIDGET_SCRIPT = `
(function() {
  var script = document.currentScript;
  var cloneSlug = script.getAttribute('data-clone');
  if (!cloneSlug) return;

  var size = script.getAttribute('data-size') || 'medium';
  var position = script.getAttribute('data-position') || 'bottom-right';
  var color = script.getAttribute('data-color') || '#7c3aed';

  var sizes = { small: 40, medium: 56, large: 72 };
  var btnSize = sizes[size] || 56;
  var icoPad = btnSize <= 40 ? 8 : btnSize <= 56 ? 12 : 16;
  var icoSize = btnSize - icoPad * 2;
  var isLeft = position === 'bottom-left';
  var posX = isLeft ? 'left' : 'right';

  var container = document.createElement('div');
  container.id = 'moc-widget';
  document.body.appendChild(container);

  // Logo SVG — white version for button
  var logoSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="' + icoSize + '" height="' + icoSize + '" viewBox="0 0 32 32"><rect x="2" y="2" width="13" height="13" rx="4" fill="white" opacity="0.95"/><rect x="17" y="2" width="13" height="13" rx="4" fill="white" opacity="0.7"/><rect x="2" y="17" width="13" height="13" rx="4" fill="white" opacity="0.7"/><rect x="17" y="17" width="13" height="13" rx="4" fill="white" opacity="0.95"/></svg>';

  var closeSvg = '<svg width="' + (icoSize * 0.75) + '" height="' + (icoSize * 0.75) + '" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>';

  var style = document.createElement('style');
  style.textContent = \`
    #moc-widget-btn {
      position: fixed;
      bottom: 24px;
      \${posX}: 24px;
      z-index: 2147483647;
      width: \${btnSize}px;
      height: \${btnSize}px;
      border-radius: 50%;
      background: linear-gradient(135deg, \${color}, \${color}cc);
      border: none;
      box-shadow: 0 4px 16px rgba(0,0,0,0.2);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.2s, box-shadow 0.2s;
      padding: 0;
    }
    #moc-widget-btn:hover {
      transform: scale(1.08);
      box-shadow: 0 6px 24px rgba(0,0,0,0.28);
    }
    #moc-widget-url {
      position: fixed;
      bottom: 8px;
      \${posX}: \${btnSize + 32}px;
      z-index: 2147483646;
      font-family: system-ui, -apple-system, sans-serif;
      font-size: 10px;
      color: rgba(0,0,0,0.25);
      pointer-events: none;
      user-select: none;
      white-space: nowrap;
    }
    #moc-widget-iframe {
      position: fixed;
      bottom: \${btnSize + 36}px;
      \${posX}: 24px;
      z-index: 2147483646;
      width: 380px;
      height: 560px;
      max-height: calc(100vh - \${btnSize + 56}px);
      border: none;
      border-radius: 16px;
      box-shadow: 0 8px 40px rgba(0,0,0,0.18);
      display: none;
      background: #fff;
    }
    @media (max-width: 480px) {
      #moc-widget-iframe {
        bottom: 0;
        right: 0;
        left: 0;
        width: 100%;
        height: 100%;
        max-height: 100vh;
        border-radius: 0;
      }
      #moc-widget-url {
        display: none;
      }
    }
  \`;
  document.head.appendChild(style);

  // Button with logo
  var button = document.createElement('button');
  button.id = 'moc-widget-btn';
  button.innerHTML = logoSvg;
  button.setAttribute('aria-label', 'Open chat');
  container.appendChild(button);

  // URL label
  var baseUrl = '${BASE_URL}';
  var urlLabel = document.createElement('div');
  urlLabel.id = 'moc-widget-url';
  urlLabel.textContent = baseUrl.replace('https://', '');
  container.appendChild(urlLabel);

  // Iframe
  var iframe = document.createElement('iframe');
  iframe.id = 'moc-widget-iframe';
  iframe.src = baseUrl + '/' + cloneSlug;
  iframe.title = 'Chat with clone';
  container.appendChild(iframe);

  var isOpen = false;
  button.addEventListener('click', function() {
    isOpen = !isOpen;
    iframe.style.display = isOpen ? 'block' : 'none';
    button.innerHTML = isOpen ? closeSvg : logoSvg;
    button.setAttribute('aria-label', isOpen ? 'Close chat' : 'Open chat');
  });
})();
`;

export async function GET() {
  const script = WIDGET_SCRIPT.replace("${BASE_URL}", BASE_URL);
  return new NextResponse(script, {
    headers: {
      "Content-Type": "application/javascript; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
