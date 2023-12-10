from flask import Flask, render_template, request


app = Flask(__name__)





@app.route('/', methods=["POST","GET"])
def main_Menu():
    if request.method == "GET":
        return render_template("Main.html")

    if request.method == "POST":
        print(request.form['url'])
        print(request.form.get('likedPhoto'))
        print(request.form.get('followingInfluencer'))
        print(request.form.get('maxVotes'))

        #from Backend import ContestResultsGenerator
        #contest = ContestResultsGenerator("Example Contest HTML File.html","Likes.csv")
        #print(contest)


        return render_template("SpinWheel.html")

        #return render_template("SpinWheel.html", inputData = contest)




if __name__ == '__main__':
    app.run()
