from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

