"""src/page.html (the same file published as the claude.ai artifact) -> index.html for GitHub Pages.
The artifact host wraps the page in a document skeleton; this adds the same skeleton so both look identical.
Usage: python3 build.py"""
import pathlib
root = pathlib.Path(__file__).parent
page = (root / "src" / "page.html").read_text(encoding="utf-8")
head = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);'
        'padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}'
        'body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}'
        'img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')
(root / "index.html").write_text(head + page + "\n</body></html>\n", encoding="utf-8")
print("index.html written")
