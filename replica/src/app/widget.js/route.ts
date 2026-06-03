import { NextResponse } from "next/server";

const BASE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://replica.tudominio.com";

const WIDGET_SCRIPT = `
(function() {
  var script = document.currentScript;
  var cloneSlug = script.getAttribute('data-clone');
  if (!cloneSlug) return;

  var container = document.createElement('div');
  container.id = 'replica-widget-container';
  document.body.appendChild(container);

  var style = document.createElement('style');
  style.textContent = \`
    #replica-widget-button {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: linear-gradient(135deg, #7c3aed, #a78bfa);
      border: none;
      box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    #replica-widget-button:hover {
      transform: scale(1.1);
      box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5);
    }
    #replica-widget-iframe {
      position: fixed;
      bottom: 96px;
      right: 24px;
      z-index: 9998;
      width: 380px;
      height: 560px;
      max-height: calc(100vh - 120px);
      border: none;
      border-radius: 16px;
      box-shadow: 0 8px 40px rgba(0, 0, 0, 0.15);
      display: none;
      background: white;
    }
    @media (max-width: 480px) {
      #replica-widget-iframe {
        bottom: 0;
        right: 0;
        width: 100%;
        height: 100%;
        max-height: 100vh;
        border-radius: 0;
      }
    }
  \`;
  document.head.appendChild(style);

  var button = document.createElement('button');
  button.id = 'replica-widget-button';
  button.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>';
  button.setAttribute('aria-label', 'Abrir chat');
  document.body.appendChild(button);

  var baseUrl = '${BASE_URL}';
  var iframe = document.createElement('iframe');
  iframe.id = 'replica-widget-iframe';
  iframe.src = baseUrl + '/' + cloneSlug;
  document.body.appendChild(iframe);

  var isOpen = false;
  button.addEventListener('click', function() {
    isOpen = !isOpen;
    iframe.style.display = isOpen ? 'block' : 'none';
    button.innerHTML = isOpen
      ? '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
      : '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>';
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
