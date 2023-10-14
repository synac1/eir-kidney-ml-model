from flask import Flask, render_template, request as req

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if req.method == "POST":
        msg = req.form.get("msg-content")
        print("Post Method", msg)
    return render_template("index.html", message_data="Hello")
if __name__ == "__main__":
    app.run(debug=True)
