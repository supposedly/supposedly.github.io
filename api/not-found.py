from urllib.parse import quote

from flask import Flask, request
app = Flask(__name__)

main_characters = set(
  'hadi is not'
  '(for now)'
  'This was automatically concocted from your own input. If it says something unsavory,'
  "that's on you."
  'See hadi.is/liable?'
)

document = '''<!DOCTYPE html><html lang=en><head><meta property=og:type content=website><title>hadi is 404</title><meta property=og:title content="Hadi is 404"><link rel=canonical href={url}><meta property=og:url content={url}><meta property=og:site_name content=Hadi.is><meta name=description content="Hadi is not {readable}"><meta property=og:description content="Hadi is not {readable}"><meta name=twitter:card content=summary><meta name=twitter:title content="Hadi is not {readable}"><meta name=twitter:description content="(for now)"><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;900&text={characters}&display=swap" rel=stylesheet><style>body,html{{height:100%;margin:0}}body{{font-family:'Noto Sans TC',sans-serif;font-size:1rem;background-color:var(--bg-color);color:var(--content-color)}}pre{{font-family:Inconsolata,monospace}}header :first-child{{margin-top:1rem}}h1,h2{{font-weight:900}}.yuge,h1{{font-size:calc(1.625rem + 4.5vw)}}@media (min-width:1200px){{.yuge,h1{{font-size:5rem}}}}.big,h2{{font-size:calc(1.325rem + .9vw);font-weight:900}}@media (min-width:1200px){{.big,h2{{font-size:2rem}}}}.less-big{{font-size:calc(1.275rem + .3vw);font-weight:500}}@media (min-width:1200px){{.less-big{{font-size:1.5rem}}}}.small{{font-size:.75rem;font-weight:400}}.giga{{font-size:calc(1.525rem + 3.3vw);font-weight:900}}@media (min-width:1200px){{.giga{{font-size:4rem}}}}.center-children{{display:flex;flex-direction:column;align-items:center}}.red{{color:red}}.faint{{opacity:.5}}.hidden{{display:none}}.flex-main{{flex:1 0 auto}}.flex-last{{flex-shrink:0}}.full-height{{height:100%}}#quicc-icons a{{opacity:var(--quicc-icon-opacity);transition:opacity 75ms}}#quicc-icons a:hover{{opacity:1}}</style></head><body><script>!function(){{const t={{local:function(){{let t;try{{t=window.localStorage;let e="__storage_test__";return t.setItem(e,e),t.removeItem(e),!0}}catch(e){{return e instanceof DOMException&&(22===e.code||1014===e.code||"QuotaExceededError"===e.name||"NS_ERROR_DOM_QUOTA_REACHED"===e.name)&&t&&0!==t.length}}}}(),set:(e,o)=>{{t.local?localStorage.setItem(e,o):document.cookie="lasttheme="+encodeURIComponent(o)+";max-age=31536000;path=/"}},get:e=>{{if(t.local)return localStorage.getItem(e);{{const t=document.cookie.split(";").find(t=>t.startsWith("lasttheme="));return t&&decodeURIComponent(t.split("=")[1])}}}}}};const e=function(){{const e=t.get("lasttheme");if("string"==typeof e)return e;const o=window.matchMedia("(prefers-color-scheme: dark)");return"boolean"==typeof o.matches&&o.matches?"dark":"light"}}(),o=document.documentElement;"light"===e?(o.style.setProperty("--bg-color","white"),o.style.setProperty("--content-color","black"),o.style.setProperty("--quicc-icon-opacity","0.25")):(o.style.setProperty("--bg-color","#2a2525"),o.style.setProperty("--content-color","#fdd"),o.style.setProperty("--quicc-icon-opacity","0.5")),o.style.setProperty("--initial-theme",e)}}();</script><nav id=quicc-icons style=position:fixed;margin:.5em><a href=/ ><svg fill=red stroke-width=0 viewBox="0 0 576 512" size=32 height=32 width=32><path d="M280.37 148.26L96 300.11V464a16 16 0 0 0 16 16l112.06-.29a16 16 0 0 0 15.92-16V368a16 16 0 0 1 16-16h64a16 16 0 0 1 16 16v95.64a16 16 0 0 0 16 16.05L464 480a16 16 0 0 0 16-16V300L295.67 148.26a12.19 12.19 0 0 0-15.3 0zM571.6 251.47L488 182.56V44.05a12 12 0 0 0-12-12h-56a12 12 0 0 0-12 12v72.61L318.47 43a48 48 0 0 0-61 0L4.34 251.47a12 12 0 0 0-1.6 16.9l25.5 31A12 12 0 0 0 45.15 301l235.22-193.74a12.19 12.19 0 0 1 15.3 0L530.9 301a12 12 0 0 0 16.9-1.6l25.5-31a12 12 0 0 0-1.7-16.93z"/></svg></a></nav><div class="center-children full-height"><div class="flex-main center-children"><p class=big>hadi is <span class=red>not</span> <span class=input>{readable}</span></p><p class=less-big>(for now)</p></div><p class="small faint flex-last">This was automatically concocted from your own input. If it says something unsavory, <b>that's on you</b>. See <a href=/liable?>hadi.is/liable?</a></p></div></body></html>'''
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def catch_all(path):
  readable = ' '.join(path.split('.', 1)[0].replace('/', ' ').split())
  return (
    document.format(
      url=request.url,
      readable=readable,
      characters=quote(''.join(main_characters | {*readable}), safe='')  # for optimizing font request
    ),
    404
  )
