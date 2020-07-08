from sanic import Sanic, response
app = Sanic(__name__)

document = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta property="og:type" content="website">
    <title>Hadi is 404</title>
    <meta property="og:title" content="Hadi is 404">
    <link rel="canonical" href="{url}">
    <meta property="og:url" content="{url}">
    <meta property="og:site_name" content="Hadi.is">
    <meta name="description" content="Hadi is not {readable}">
    <meta property="og:description" content="Hadi is not {readable}">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="Hadi is not {readable}">
    <meta name="twitter:description" content="(for now)">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
      href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Inconsolata:wght@400&family=Raleway:wght@700&display=swap"
      rel="stylesheet"
    />
    <style>
      body,html{{height:100%;margin:0}}body{{font-family:'Noto Sans TC',sans-serif;font-size:1rem}}pre{{font-family:Inconsolata,monospace}}header :first-child{{margin-top:1rem}}h1,h2{{font-weight:900}}.yuge,h1{{font-size:calc(1.625rem + 4.5vw)}}@media (min-width:1200px){{.yuge,h1{{font-size:5rem}}}}.big,h2{{font-size:calc(1.325rem + .9vw);font-weight:900}}@media (min-width:1200px){{.big,h2{{font-size:2rem}}}}.less-big{{font-size:calc(1.275rem + .3vw);font-weight:500}}@media (min-width:1200px){{.less-big{{font-size:1.5rem}}}}.small{{font-size:.75rem;font-weight:400}}.giga{{font-size:calc(1.525rem + 3.3vw);font-weight:900}}@media (min-width:1200px){{.giga{{font-size:4rem}}}}.center-children{{display:flex;flex-direction:column;align-items:center}}.red{{color:red}}.faint{{opacity:50%}}.hidden{{display:none}}.flex-main{{flex:1 0 auto}}.flex-last{{flex-shrink:0}}.full-height{{height:100%}}
    </style>
  </head>
  <body>
    <div class="center-children full-height">
      <div class="flex-main center-children">
        <p class="big">
          hadi is <span class="red">not</span> <span class="input">{readable}</span>
        </p>
        <p class="less-big">(for now)</p>
      </div>
      <p class="small faint flex-last">
        This was automatically concocted using your own input.
        If it says something unsavory, <b>that's on you</b>.
        See <a href="/liable">hadi.is/liable</a>
      </p>
    </div>
  </body>
</html>
'''

@app.route('/')
@app.route('/<path:path>')
async def catch_all(request, path='index.html'):
    return response.html(
      document.format(url=request.url, readable=' '.join(path.split('.', 1)[0].replace('/', ' ').split())),
      status=404
    )
