from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    return "This is the homepage"#render_template('index.html')

@app.route('/output/<url>')
def output(url, methods=["GET","POST"]):
    if (request.method == "POST"):
        print("post")
    if (request.method == "GET"):
        print("post")

    return render_template("flask_test.html", url=url)

if __name__ == '__main__':
    app.run(debug=True)