from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is my first Flask App'

@app.route('/index/')
def index_page():
    return '<body style = background-color:pink>' \
           '<h1>Home</h1>' \
           '<ul>' \
           '<li><a href="http://127.0.0.1:5000/about/">About</a></li>' \
           '<li><a href="http://127.0.0.1:5000/projects/">Projects</a></li>' \
           '<li><a href="http://127.0.0.1:5000/contact/">Contacts</a></li>' \
           '</ul>' \
           '</body>'

@app.route('/about/')
def about_page():
    return '<body style=background-color:pink>' \
           '<h1>About</h1></body>'

@app.route('/projects/')
def projects_page():
    return '<body style = background-color:pink>' \
           '<h1>Projects</h1></body>'

@app.route('/contact/')
def contact_page():
    return '<body style = background-color:pink>' \
           '<h1>Contact</h1></body>'


if __name__ == "__main__":
    app.debug = True
    app.run()