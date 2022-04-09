from flask import Flask, render_template
from Backend import readHTMLData

app = Flask(__name__)





@app.route('/')
def spin_Wheel():
    contest = readHTMLData()
    return render_template("SpinWheel.html", inputData = contest)


if __name__ == '__main__':
    app.run()
