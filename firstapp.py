from flask import Flask,render_template,url_for

app = Flask(__name__)

posts=[
    {
        'author':'James John',
        'Title':'Blog of Reality',
        'content':'Everything in this is not real',
        'date_of_post':'April 20,2021'
    },
    {
        'author':'James Hennry',
        'Title':'Blog of Illusion',
        'content':'Everyday will be better then yesterday',
        'date_of_post':'April 22,2021'
    }
]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)
