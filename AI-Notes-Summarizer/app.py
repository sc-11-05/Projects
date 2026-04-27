from flask import Flask, request, render_template
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""

    if request.method == "POST":
        text = request.form["notes"]
        style = request.form["style"]
        summary = summarize_text(text, style)

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)