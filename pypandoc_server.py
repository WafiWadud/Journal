from asyncio import set_event_loop_policy
from os import PathLike

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from pypandoc import convert_file
from uvicorn import run
from uvloop import EventLoopPolicy
from os.path import exists
from glob import glob

for filename in glob("*.md"):
    if not exists(f"build/{filename}.html"):
        with open(f"build/{filename}.html", "w") as f:
            pass
        convert_file(
            filename, to="html", format="md", outputfile=f"build/{filename}.html"
        )
# Set uvloop as the event loop policy
set_event_loop_policy(EventLoopPolicy())

app: FastAPI = FastAPI()


async def read_file(filename: str | PathLike[str]) -> str:
    with open(filename, "r") as f:
        return f.read()


@app.get("/index")
async def list_files():
    return HTMLResponse(
        content='<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js" integrity="sha512-D9gUyxqja7hBtkWpPWGt9wfbfaMGVt9gnyCvYa+jojwwPHLCzUm5i8rpk7vD7wNee9bA35eYIjobYPaQuKS1MQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/darcula.css" integrity="sha512-LBTd9wWU9cpQj0FeE4eAN9aZYIp7zDFIRc5yyGyRaVaob8vkmfrJIAxg2lpZppwzAZMA5ErYbpngxxGGMKpRZA==" crossorigin="anonymous" referrerpolicy="no-referrer" /><link rel="stylesheet" href="index.css"><script>hljs.highlightAll();</script>'
        + f"""
            <h1>Index of /</h1>
            <ul>
            {"".join(f'<li><a href="{filename}">{filename}</a></li>' for filename in glob("*.md"))}
            </ul>
            """
    )


@app.get("/{filename:path}")
async def serve_file(filename: str):
    if not exists(filename):
        return FileResponse(path="404.html", status_code=404)
    if filename.endswith(".md"):
        return HTMLResponse(
            content='<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js" integrity="sha512-D9gUyxqja7hBtkWpPWGt9wfbfaMGVt9gnyCvYa+jojwwPHLCzUm5i8rpk7vD7wNee9bA35eYIjobYPaQuKS1MQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/darcula.css" integrity="sha512-LBTd9wWU9cpQj0FeE4eAN9aZYIp7zDFIRc5yyGyRaVaob8vkmfrJIAxg2lpZppwzAZMA5ErYbpngxxGGMKpRZA==" crossorigin="anonymous" referrerpolicy="no-referrer" /><link rel="stylesheet" href="index.css"><script>hljs.highlightAll();</script>'
            + await read_file(f"build/{filename}.html")
        )
    return FileResponse(path=filename)


run(app=app, host="0.0.0.0", port=80, loop="uvloop")
