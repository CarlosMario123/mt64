from flask import Flask,render_template
from routes.bs64Router import bs64Route
app = Flask(__name__)
app.register_blueprint(bs64Route)
@app.route('/')
def home():
    return render_template("wellcome.html")

if __name__ == '__main__':
    app.run(debug=True)
