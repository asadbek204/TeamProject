from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('Organick.html')

@app.route('/blog')
def blog():
    return render_template('Blog.html')