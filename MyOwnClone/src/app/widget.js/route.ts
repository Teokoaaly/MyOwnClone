import { NextResponse } from "next/server";

const BASE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://myownclone.com";

const WIDGET_SCRIPT = `
(function() {
  "use strict";
  var s = document.currentScript;
  if (!s) return;
  var slug = s.getAttribute("data-clone");
  if (!slug) { console.error("MyOwnClone: data-clone is required"); return; }
  var BASE = (function() { try { return new URL(s.src).origin; } catch(e) { return "https://myownclone.com"; } })();
  var cfg = {
    mode: s.getAttribute("data-mode") || "bubble",
    container: s.getAttribute("data-container"),
    size: s.getAttribute("data-size") || "medium",
    position: s.getAttribute("data-position") || "bottom-right",
    color: s.getAttribute("data-color") || "#7c3aed",
    height: s.getAttribute("data-height") || "560px",
    width: s.getAttribute("data-width") || "380px",
    voice: s.getAttribute("data-voice") === "true",
    placeholder: s.getAttribute("data-placeholder") || "Type your message...",
    simple: s.getAttribute("data-simple") === "true",
    zIndex: 2147483647,
  };
  var tooltips = [];
  try { var tt = s.getAttribute("data-tooltips"); if (tt) tooltips = JSON.parse(tt); } catch(e) {}
  if (!tooltips.length) tooltips = ["Talk to me!","Ask me anything","Need help?","Let\\u2019s chat!"];
  var sizes = {small:48,medium:60,large:72};
  var B = sizes[cfg.size]||60, P = Math.round(B*.15), I = B-P*2;

  // Inject styles
  var STID="moc-ws";
  if(!document.getElementById(STID)){
    var st=document.createElement("style");st.id=STID;
    st.textContent="@keyframes moc-p{0%{transform:scale(1);opacity:.4}100%{transform:scale(1.7);opacity:0}}@keyframes moc-f{0%{transform:translateY(0)}50%{transform:translateY(-5px)}100%{transform:translateY(0)}}@keyframes moc-ti{from{opacity:0;transform:translateX(10px) scale(.9)}to{opacity:1;transform:translateX(0) scale(1)}}@keyframes moc-to{from{opacity:1;transform:translateX(0) scale(1)}to{opacity:0;transform:translateX(10px) scale(.9)}}@keyframes moc-ii{from{opacity:0;transform:scale(0)}to{opacity:1;transform:scale(1)}}.moc-o{position:relative;display:flex;align-items:center;justify-content:center}.moc-oc{width:100%;height:100%}.moc-oe{position:fixed;z-index:"+cfg.zIndex+";pointer-events:auto}.moc-oe.moc-pbr{bottom:24px;right:24px}.moc-oe.moc-pbl{bottom:24px;left:24px}.moc-oe.moc-ptr{top:24px;right:24px}.moc-oe.moc-ptl{top:24px;left:24px}.moc-w{position:relative;display:flex;align-items:center;justify-content:center}.moc-ww{position:absolute;border-radius:9999px!important;opacity:0;pointer-events:none;animation:moc-p 2s cubic-bezier(.4,0,.2,1) infinite}.moc-b{position:relative;display:flex!important;align-items:center!important;justify-content:center!important;border-radius:9999px!important;border:none!important;cursor:pointer!important;outline:none!important;pointer-events:auto;transition:transform .15s ease;padding:0!important;margin:0!important;box-sizing:border-box!important;overflow:hidden!important}.moc-b:hover{transform:scale(1.1)}.moc-b:active{transform:scale(.95)}.moc-bf{animation:moc-f 2s ease-in-out infinite}.moc-iw{display:flex;align-items:center;justify-content:center;animation:moc-ii .2s cubic-bezier(.4,0,.2,1) both}.moc-tt{position:absolute;top:0;bottom:0;right:100%;margin-right:12px;display:flex;align-items:center;pointer-events:none}.moc-tti{animation:moc-ti .25s ease both}.moc-tto{animation:moc-to .2s ease both}.moc-ttin{position:relative;white-space:nowrap;border-radius:12px;padding:10px 16px;background:#1f2937;color:#fff;box-shadow:0 4px 12px rgba(0,0,0,.15);font-size:14px;font-weight:500;display:flex;align-items:center;gap:8px;font-family:system-ui,-apple-system,sans-serif}.moc-tta{position:absolute;right:-8px;top:50%;transform:translateY(-50%);width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-left:8px solid #1f2937}.moc-iw{display:flex;align-items:center;justify-content:center}";
    document.head.appendChild(st);
  }

  var expanded=false,hasInteracted=false,ttIdx=0,tt1,tt2,tt3;
  var outerEl,wrapperEl,floatEl,btnEl,iconSlot,tooltipEl;
  var iframeEl,iframeWrap,pendingCalls={};

  function svg(vb,sz,c){var e=document.createElementNS("http://www.w3.org/2000/svg","svg");e.setAttribute("viewBox",vb);e.setAttribute("width",String(sz));e.setAttribute("height",String(sz));e.setAttribute("fill","none");e.setAttribute("xmlns","http://www.w3.org/2000/svg");e.innerHTML=c;return e;}
  function posCls(){return "moc-p"+cfg.position.replace("-","");}
  function rSize(){return "clamp("+Math.round(B*.7)+"px,10vw,"+B+"px)";}

  // Build bubble
  function buildBubble(){
    outerEl=document.createElement("div");outerEl.className="moc-o moc-oc";
    wrapperEl=document.createElement("div");wrapperEl.className="moc-w";
    ["0s",".65s","1.3s"].forEach(function(dl){
      var w=document.createElement("div");w.className="moc-ww";
      w.style.cssText="width:"+rSize()+";height:"+rSize()+";background:"+cfg.color+";animation-delay:"+dl+";";
      wrapperEl.appendChild(w);
    });
    floatEl=document.createElement("div");
    if(!cfg.simple)floatEl.className="moc-bf";
    btnEl=document.createElement("button");btnEl.className="moc-b";
    btnEl.setAttribute("aria-label","Open chat");
    btnEl.style.cssText="width:"+rSize()+";height:"+rSize()+";background:"+cfg.color+";box-shadow:0 4px 20px "+cfg.color+"80,0 2px 8px rgba(0,0,0,.15);";
    tooltipEl=buildTT();tooltipEl.style.display="none";btnEl.appendChild(tooltipEl);
    iconSlot=document.createElement("div");renderIcon(false);btnEl.appendChild(iconSlot);
    floatEl.appendChild(btnEl);wrapperEl.appendChild(floatEl);outerEl.appendChild(wrapperEl);
    document.body.appendChild(outerEl);
    btnEl.addEventListener("click",handleClick);
    startTT();
  }

  function buildTT(){
    var w=document.createElement("div");w.className="moc-tt";
    var inn=document.createElement("div");inn.className="moc-ttin";
    inn.appendChild(svg("0 0 24 24",16,'<path d="M12 3L13.4 8.6L19 10L13.4 11.4L12 17L10.6 11.4L5 10L10.6 8.6L12 3Z" fill="#facc15"/><path d="M19 15L19.8 17.2L22 18L19.8 18.8L19 21L18.2 18.8L16 18L18.2 17.2L19 15Z" fill="#facc15"/>'));
    var sp=document.createElement("span");sp.textContent=tooltips[0];inn.appendChild(sp);
    var ar=document.createElement("div");ar.className="moc-tta";inn.appendChild(ar);
    w.appendChild(inn);return w;
  }

  function renderIcon(exp){
    if(!iconSlot)return;while(iconSlot.firstChild)iconSlot.removeChild(iconSlot.firstChild);
    var w=document.createElement("div");w.className="moc-iw";
    if(exp){w.appendChild(svg("0 0 24 24",I,'<path d="M18 6L6 18M6 6L18 18" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'));}
    else{w.appendChild(svg("0 0 28 28",I,'<path d="M14 2.33C7.56 2.33 2.33 7.03 2.33 12.83C2.33 15.32 3.3 17.59 4.9 19.36V25.67L10.76 22.52C11.8 22.75 12.88 22.88 14 22.88C20.44 22.88 25.67 18.18 25.67 12.38C25.67 6.58 20.44 2.33 14 2.33Z" fill="#fff"/>'));}
    iconSlot.appendChild(w);
  }

  function startTT(){clearTT();tt1=setTimeout(function(){if(hasInteracted||expanded)return;showTT();schedHide();},3000);}
  function showTT(){if(!tooltipEl||cfg.simple||expanded||hasInteracted)return;tooltipEl.style.display="flex";tooltipEl.classList.remove("moc-tto");tooltipEl.offsetWidth;tooltipEl.classList.add("moc-tti");}
  function hideTT(a){if(!tooltipEl)return;if(!a){tooltipEl.style.display="none";tooltipEl.classList.remove("moc-tti","moc-tto");return;}tooltipEl.classList.remove("moc-tti");tooltipEl.offsetWidth;tooltipEl.classList.add("moc-tto");tooltipEl.addEventListener("animationend",function h(){tooltipEl.style.display="none";tooltipEl.classList.remove("moc-tto");tooltipEl.removeEventListener("animationend",h);});}
  function schedHide(){tt2=setTimeout(function(){hideTT(true);tt3=setTimeout(function(){if(hasInteracted||expanded)return;ttIdx=(ttIdx+1)%tooltips.length;var sp=tooltipEl.querySelector("span");if(sp)sp.textContent=tooltips[ttIdx];showTT();schedHide();},8000);},4000);}
  function clearTT(){[tt1,tt2,tt3].forEach(function(t){if(t)clearTimeout(t);});}

  function handleClick(){
    hasInteracted=true;clearTT();hideTT(false);
    if(expanded){expanded=false;setExp(false);shrinkC();}
    else{expanded=true;setExp(true);if(!iframeEl)createIframe();expandC();postChild({type:"PARENT_CALL",method:"open",id:"o-"+Date.now()});}
  }

  function setExp(exp){
    if(outerEl){var c=posCls();if(exp){outerEl.classList.remove("moc-oc");outerEl.classList.add("moc-oe",c);outerEl.style.width=rSize();outerEl.style.height=rSize();}else{outerEl.classList.remove("moc-oe",c);outerEl.classList.add("moc-oc");outerEl.style.width="";outerEl.style.height="";}}
    var ws=wrapperEl?wrapperEl.querySelectorAll(".moc-ww"):[];ws.forEach(function(w){w.style.display=(!cfg.simple&&!exp)?"block":"none";});
    if(floatEl){if(!cfg.simple&&!exp)floatEl.classList.add("moc-bf");else floatEl.classList.remove("moc-bf");}
    renderIcon(exp);
  }

  function expandC(){if(!iframeWrap||cfg.mode==="inline")return;iframeWrap.style.cssText="position:fixed;top:0;left:0;right:0;bottom:0;width:100vw;height:100vh;z-index:"+(cfg.zIndex-1)+";pointer-events:none;";showIframe();}
  function shrinkC(){if(!iframeWrap||cfg.mode==="inline")return;iframeWrap.style.cssText="position:fixed;z-index:"+(cfg.zIndex-1)+";pointer-events:none;";hideIframe();}

  function createIframe(){
    if(cfg.mode==="inline"){var el=document.querySelector(cfg.container);if(!el){console.error("MyOwnClone: container "+cfg.container+" not found");return;}iframeWrap=el;iframeWrap.style.cssText="position:relative;width:100%;height:"+cfg.height+";display:block;";}
    else{iframeWrap=document.createElement("div");iframeWrap.id="moc-wc";iframeWrap.style.cssText="position:fixed;z-index:"+(cfg.zIndex-1)+";pointer-events:none;";document.body.appendChild(iframeWrap);}
    iframeEl=document.createElement("iframe");iframeEl.id="moc-wi";iframeEl.title="MyOwnClone Chat";
    iframeEl.style.cssText="width:100%;height:100%;border:none;background:transparent;pointer-events:auto;";
    iframeEl.setAttribute("sandbox","allow-scripts allow-same-origin allow-forms allow-popups allow-popups-to-escape-sandbox");
    iframeEl.setAttribute("allow","microphone; camera; autoplay; display-capture");
    iframeEl.src=buildUrl();iframeWrap.appendChild(iframeEl);
    iframeEl.addEventListener("load",function(){});
  }

  function buildUrl(){
    var p=new URLSearchParams({slug:slug,mode:cfg.mode,position:cfg.position,primaryColor:cfg.color,enableVoice:String(cfg.voice),inputPlaceholder:cfg.placeholder,height:cfg.height,width:cfg.width});
    return BASE+"/embed/chat?"+p.toString();
  }

  function showIframe(){if(iframeEl){iframeEl.style.visibility="visible";iframeEl.style.position="";iframeEl.style.width="100%";iframeEl.style.height="100%";iframeEl.style.pointerEvents="auto";}}
  function hideIframe(){if(iframeEl){iframeEl.style.visibility="hidden";iframeEl.style.position="absolute";iframeEl.style.width="0";iframeEl.style.height="0";iframeEl.style.pointerEvents="none";}}

  function postChild(m){if(iframeEl&&iframeEl.contentWindow)iframeEl.contentWindow.postMessage(m,"*");}

  window.addEventListener("message",function(e){
    if(e.source!==(iframeEl&&iframeEl.contentWindow))return;
    var d=e.data;if(!d||typeof d.type!=="string")return;
    if(d.type==="CHILD_READY"){}
    else if(d.type==="CHILD_RESPONSE"&&d.id&&pendingCalls[d.id]){if(d.error)pendingCalls[d.id].reject(new Error(d.error));else pendingCalls[d.id].resolve(d.result);delete pendingCalls[d.id];}
    else if(d.type==="CHILD_CALL"){
      var fns={notifyOpen:function(){},notifyClose:function(){if(expanded){expanded=false;setExp(false);shrinkC();}},notifyMessage:function(){},notifyEmailSubmit:function(){},notifyError:function(){},notifyAvatarUrl:function(){}};
      var fn=fns[d.method];if(fn){try{var r=fn.apply(null,d.args||[]);postChild({type:"PARENT_RESPONSE",id:d.id,result:r});}catch(err){postChild({type:"PARENT_RESPONSE",id:d.id,error:err.message});}}
    }
  });

  var api={open:function(){if(cfg.mode==="bubble"&&!expanded)return handleClick();if(iframeEl)return postChild({type:"PARENT_CALL",method:"open",id:"o-"+Date.now()});},close:function(){if(cfg.mode==="bubble"&&expanded)return handleClick();if(iframeEl)return postChild({type:"PARENT_CALL",method:"close",id:"c-"+Date.now()});},toggle:function(){return expanded?api.close():api.open();},destroy:function(){clearTT();if(outerEl&&outerEl.parentNode)outerEl.parentNode.removeChild(outerEl);if(iframeWrap&&iframeWrap.parentNode&&cfg.mode!=="inline")iframeWrap.parentNode.removeChild(iframeWrap);outerEl=iframeEl=iframeWrap=null;}};

  function init(){if(cfg.mode==="inline"){createIframe();}else if(cfg.mode==="fullpage"){var fp=document.createElement("div");fp.id="moc-wc";fp.style.cssText="position:fixed;top:0;left:0;right:0;bottom:0;width:100vw;height:100vh;z-index:"+cfg.zIndex+";background:#fff;";document.body.appendChild(fp);document.body.style.overflow="hidden";iframeWrap=fp;createIframe();}else{buildBubble();setTimeout(function(){if(!iframeEl&&cfg.mode==="bubble"){createIframe();hideIframe();}},3000);}}

  if(document.body)init();else document.addEventListener("DOMContentLoaded",init,{once:true});
  window.MyOwnClone=api;
})();
`;

export async function GET() {
  return new NextResponse(WIDGET_SCRIPT, {
    headers: {
      "Content-Type": "application/javascript; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
