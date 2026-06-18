import { NextResponse } from "next/server";

const BASE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://myownclone.com";

const WIDGET_SCRIPT = `
(function() {
  var s = document.currentScript;
  var slug = s.getAttribute('data-clone');
  if (!slug) return;

  var sz = s.getAttribute('data-size') || 'medium';
  var pos = s.getAttribute('data-position') || 'bottom-right';
  var clr = s.getAttribute('data-color') || '#7c3aed';

  var sizes = { small: 40, medium: 56, large: 72 };
  var B = sizes[sz] || 56;
  var P = B <= 40 ? 8 : B <= 56 ? 12 : 16;
  var I = B - P * 2;
  var isLeft = pos === 'bottom-left';
  var side = isLeft ? 'left' : 'right';

  // Build SVG logo
  var logoSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="' + I + '" height="' + I + '" viewBox="0 0 32 32">'
    + '<rect x="2" y="2" width="13" height="13" rx="4" fill="#fff" fill-opacity="0.95"/>'
    + '<rect x="17" y="2" width="13" height="13" rx="4" fill="#fff" fill-opacity="0.7"/>'
    + '<rect x="2" y="17" width="13" height="13" rx="4" fill="#fff" fill-opacity="0.7"/>'
    + '<rect x="17" y="17" width="13" height="13" rx="4" fill="#fff" fill-opacity="0.95"/>'
    + '</svg>';

  var closeSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="' + (I*0.7) + '" height="' + (I*0.7) + '" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round">'
    + '<line x1="18" y1="6" x2="6" y2="18"/>'
    + '<line x1="6" y1="6" x2="18" y2="18"/>'
    + '</svg>';

  var base = '${BASE_URL}';

  // Button
  var btn = document.createElement('button');
  btn.id = 'moc-w-btn';
  btn.innerHTML = logoSvg;
  btn.setAttribute('aria-label', 'Open chat');
  var btnCss = 'position:fixed;bottom:24px;' + side + ':24px;z-index:2147483647;'
    + 'width:' + B + 'px;height:' + B + 'px;border-radius:50%;'
    + 'background:linear-gradient(135deg,' + clr + ',' + clr + 'cc);'
    + 'border:none;box-shadow:0 4px 16px rgba(0,0,0,0.2);cursor:pointer;'
    + 'display:flex;align-items:center;justify-content:center;padding:0;'
    + 'transition:transform 0.2s,box-shadow 0.2s;';
  btn.style.cssText = btnCss;
  btn.onmouseenter = function(){ this.style.transform='scale(1.08)'; this.style.boxShadow='0 6px 24px rgba(0,0,0,0.28)'; };
  btn.onmouseleave = function(){ this.style.transform=''; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.2)'; };
  document.body.appendChild(btn);

  // URL label
  var lbl = document.createElement('div');
  lbl.id = 'moc-w-lbl';
  lbl.textContent = 'myownclone.com';
  lbl.style.cssText = 'position:fixed;bottom:8px;' + side + ':' + (B + 32) + 'px;z-index:2147483646;'
    + 'font-family:system-ui,-apple-system,sans-serif;font-size:10px;'
    + 'color:rgba(0,0,0,0.25);pointer-events:none;user-select:none;white-space:nowrap;';
  document.body.appendChild(lbl);

  // Iframe
  var ifr = document.createElement('iframe');
  ifr.id = 'moc-w-ifr';
  ifr.src = base + '/' + slug;
  ifr.title = 'Chat';
  ifr.style.cssText = 'position:fixed;bottom:' + (B + 36) + 'px;' + side + ':24px;z-index:2147483646;'
    + 'width:380px;height:560px;max-height:calc(100vh - ' + (B + 56) + 'px);'
    + 'border:none;border-radius:16px;box-shadow:0 8px 40px rgba(0,0,0,0.18);'
    + 'display:none;background:#fff;';
  document.body.appendChild(ifr);

  // Mobile fullscreen
  var mq = window.matchMedia('(max-width:480px)');
  function setMobile(m) {
    if (m) {
      ifr.style.cssText = ifr.style.cssText
        .replace(/width:[^;]+/,'width:100%')
        .replace(/height:[^;]+/,'height:100%')
        .replace(/max-height:[^;]+/,'max-height:100vh')
        .replace(/bottom:[^;]+/,'bottom:0')
        .replace(/right:[^;]+|left:[^;]+/,'right:0;left:0')
        .replace(/border-radius:[^;]+/,'border-radius:0');
      if (lbl) lbl.style.display = 'none';
    }
  }
  mq.addEventListener('change', function(e){ setMobile(e.matches); });

  var open = false;
  btn.addEventListener('click', function(){
    open = !open;
    ifr.style.display = open ? 'block' : 'none';
    btn.innerHTML = open ? closeSvg : logoSvg;
    btn.setAttribute('aria-label', open ? 'Close chat' : 'Open chat');
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
