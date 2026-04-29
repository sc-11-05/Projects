from flask import Flask, request, render_template
from summarizer import summarize_text
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""

    if request.method == "POST":
        style = request.form["style"]

        # To check if file is uploaded
        if "pdf" in request.files and request.files["pdf"].filename != "":
            file = request.files["pdf"]

            reader = PyPDF2.PdfReader(file)
            text= ""

            for page in reader.pages:
                text += page.extract_text() or ""
        else:
            text = request.form["notes"]
        
        summary = summarize_text(text, style)

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)