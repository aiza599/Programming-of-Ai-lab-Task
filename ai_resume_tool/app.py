from flask import Flask, render_template, request

app = Flask(__name__)

def improve_resume(text):
    suggestions = []
    if "I am" in text:
        suggestions.append("Avoid 'I am'. Start with action verbs like 'Developed', 'Managed'.")
    if len(text.split()) < 50:
        suggestions.append("Add more details about your achievements and projects.")
    if "responsible for" in text:
        suggestions.append("Replace 'responsible for' with strong verbs like 'Led', 'Designed'.")
    if not suggestions:
        suggestions.append("Good resume! Consider adding metrics (e.g., increased sales by 20%).")
    return suggestions

@app.route("/", methods=["GET", "POST"])
def index():
    suggestions = []
    if request.method == "POST":
        resume_text = request.form.get("resume")
        suggestions = improve_resume(resume_text)
    return render_template("index.html", suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
