from flask import Flask, render_template, request
from generator import generate_name_ideas

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ideas = []
    name = ""
    pron = ""
    style = ""

    if request.method == "POST":
        name = request.form.get("name", "")
        pron = request.form.get("pronunciation", "")
        style = request.form.get("style", "")
        ideas = generate_name_ideas(pron, style, num_patterns=5)

    return render_template("index.html", name=name, pron=pron, style=style, ideas=ideas)


if __name__ == "__main__":
    app.run(debug=True, port=5000)