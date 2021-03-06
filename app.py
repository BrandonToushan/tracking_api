from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>It really do be like that sometimes</h1>
    <p>It is currently {time}.</p>

    <img src="https://raw.githubusercontent.com/BrandonToushan/BrandonToushan.github.io/master/img/Headshot.jpg">
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
