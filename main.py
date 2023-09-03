from flask import Flask, render_template

app = Flask(__name__)

pages: list = [
    ('main', 'Organick'),
    ('service', 'Service'),
    ('portfolio', 'Portfolio'),
    ('blog', 'Blog'),
    ('team', 'Team'),
    ('contact', 'Contact')
]

@app.route('/')
def main():
    return render_template('Organick.html', title='Organick', pages=pages[1:])

@app.route('/blog')
def blog():
    return render_template('Blog.html', title='Blog', pages=pages[:3] + pages[4:])

@app.route('/service')
def service():
    return '<h1>service page</h1>'

@app.route('/portfolio')
def portfolio():
    return '<h1>portfolio page</h1>'

@app.route('/team')
def team():
    return '<h1>team page</h1>'

@app.route('/contact')
def contact():
    return '<h1>contact page</h1>'

@app.route('/home')
def home():
    return main()

@app.route('/about')
def about():
    return '<h1>about page</h1>'

@app.route('/shop')
def shop():
    return '<h1>shop page</h1>'

@app.route('/projects')
def projects():
    return '<h1>projects page</h1>'

@app.route('/news')
def news():
    return '<h1>news page</h1>'

@app.route('/password')
def password():
    return render_template('password.html', title='Password Protected', pages=pages)

@app.route('/licenses')
def licenses():
    return render_template('licenses.html', title='Licenses', pages=pages)

@app.route('/change_log')
def change_log():
    return render_template('change_log.html', title='Change Log', pages=pages)

@app.route('/not_found')
def not_found():
    return render_template('404_Not_Found.html', title='404 Not Found', pages=pages, haven_t_form='haven-t-form')

@app.errorhandler(404)
def not_found_err(e):
    return not_found()

if __name__ == '__main__':
    app.run(debug=True)