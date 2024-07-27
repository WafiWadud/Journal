from asyncio import set_event_loop_policy
from glob import glob
from typing import Dict

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from pypandoc import convert_file
from uvicorn import run
from uvloop import EventLoopPolicy

# Set uvloop as the event loop policy
set_event_loop_policy(EventLoopPolicy())

app = FastAPI()
html_files: Dict[str, str] = {}

# Convert all Markdown files to HTML and store them in memory
for filename in glob("*.md"):
    html_content = convert_file(filename, to="html", format="md")
    # Use the base name of the file without extension for the key
    html_files[filename] = (
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js" integrity="sha512-D9gUyxqja7hBtkWpPWGt9wfbfaMGVt9gnyCvYa+jojwwPHLCzUm5i8rpk7vD7wNee9bA35eYIjobYPaQuKS1MQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/darcula.css" integrity="sha512-LBTd9wWU9cpQj0FeE4eAN9aZYIp7zDFIRc5yyGyRaVaob8vkmfrJIAxg2lpZppwzAZMA5ErYbpngxxGGMKpRZA==" crossorigin="anonymous" referrerpolicy="no-referrer" /><link rel="stylesheet" href="index.css"><script>hljs.highlightAll();</script>'
        + html_content
    )


@app.get("/{filename:path}")
async def serve_file(filename: str):
    if filename in html_files:
        return HTMLResponse(content=html_files[filename])
    elif filename.endswith((".css", ".js")):
        return FileResponse(filename)
    else:
        return FileResponse(filename)


run(app, host="0.0.0.0", port=80, loop="uvloop")
