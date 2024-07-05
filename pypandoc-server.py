from flask import Flask, Response
from glob import glob
from pypandoc import convert_file

app = Flask(__name__)
html_files = {}

# Convert all Markdown files to HTML and store them in memory
for filename in glob("*.md"):
    html_content = convert_file(filename, to="html", format="md")
    # Use the base name of the file without extension for the key
    html_files[filename] = html_content


@app.route("/<path:filename>")
def serve_html(filename):
    # Check if the requested file exists in our stored HTML files
    if filename in html_files:
        return Response(html_files[filename], mimetype="text/html")
    elif filename.endswith(".css"):
        return Response(open(filename, "r").read(), mimetype="text/css")
    elif filename.endswith(".js"):
        return Response(open(filename, "r").read(), mimetype="text/javascript")
    else:
        return Response(open(filename, "rb").read(), mimetype="image")


if __name__ == "__main__":
    app.run(debug=False, port=80, host="0.0.0.0")
