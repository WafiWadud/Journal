from typing import Any
from flask import Flask, Response
from glob import glob
from pypandoc import convert_file
from typing import Dict

app: Flask = Flask(__name__)
html_files: Dict = {}

# Convert all Markdown files to HTML and store them in memory
for filename in glob("*.md"):
    html_content = convert_file(filename, to="html", format="md")
    # Use the base name of the file without extension for the key
    html_files[filename] = (
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js" integrity="sha512-D9gUyxqja7hBtkWpPWGt9wfbfaMGVt9gnyCvYa+jojwwPHLCzUm5i8rpk7vD7wNee9bA35eYIjobYPaQuKS1MQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/darcula.css" integrity="sha512-LBTd9wWU9cpQj0FeE4eAN9aZYIp7zDFIRc5yyGyRaVaob8vkmfrJIAxg2lpZppwzAZMA5ErYbpngxxGGMKpRZA==" crossorigin="anonymous" referrerpolicy="no-referrer" /><link rel="stylesheet" href="index.css">'
        + html_content
    )


@app.route("/<path:filename>")
def serve_html(filename: Any) -> Response:
    # Check if the requested file exists in our stored HTML files
    if filename in html_files:
        return Response(html_files[filename], mimetype="text/html")
    elif str(filename).endswith(".css"):
        return Response(open(filename, "r").read(), mimetype="text/css")
    elif str(filename).endswith(".js"):
        return Response(open(filename, "r").read(), mimetype="text/javascript")
    else:
        return Response(open(filename, "rb").read(), mimetype="image")


app.run(debug=False, port=80, host="0.0.0.0")
