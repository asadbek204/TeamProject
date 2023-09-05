from flask import Flask, render_template, url_for
from dataclasses import dataclass, asdict
app = Flask(__name__)

pages: list = [
    ('main', 'Organick'),
    ('service', 'Service'),
    ('portfolio', 'Portfolio'),
    ('blog', 'Blog'),
    ('team', 'Team'),
]

# page blog content 

@dataclass
class BlogCart:
    class_name: str
    date_day: int
    date_month: str
    user_name: str
    h1_content: str
    p_content: str
    user_img: str
    button_id: str

class_name: str = 'page-blog-box-{}'
date_day: int = 25
date_month: str = 'Nov'
p_content: str = 'Simply dummy text of the printing and typesetting industry. Lorem Ipsum'
user_img: str = 'img/blog/user-icon.png'
user_name: str = 'Rachi Card'
button_id: str = "button-box-{}"
h1_contents: list = [
    ['The Benefits of Vitamin D & How to Get It',
    'Our Favorite Summertime Tomato'],
    ['Benefits of Vitamin C & How to Get It',
    'Research More Organic Foods'],
    ['Everyday Fresh Fruites',
    'Don’t Use Plastic Product! it’s Kill Nature']
]

page_blog_content = [[
    asdict(
        BlogCart(
            class_name=class_name.format(index*2+i),
            date_day=date_day,
            date_month=date_month,
            user_name=user_name,
            h1_content=h1_content,
            p_content=p_content,
            user_img=user_img,
            button_id=button_id.format(index) 
        )
    ) for i, h1_content in enumerate(h1_content2, start=1)] for index, h1_content2 in enumerate(h1_contents)]

# 

@app.route('/')
# @app.route('/home')
def main():
    return render_template('Organick.html', title='Organick', pages=pages[1:])

@app.route('/blog')
def blog():
    return render_template('Blog.html', title='Blog', pages=pages[:3] + pages[4:], cart_content=page_blog_content)
@app.route('/service/')
@app.route('/service')
def service():
    return render_template('services.html', title='Services', pages=pages[:1] +pages[2:], haven_t_form='haven-t-form')

@app.route('/portfolio')
def portfolio():
    return render_template('port-standart.html', title='Portfolio Standard', pages=[pages[0]]+pages[1:])

@app.route('/team')
def team():
    return render_template('our-team.html', title="Team", pages=pages[:-2] + [pages[-1]])

@app.route('/contact')
def contact():
    return '<h1>contact page</h1>'

@app.route('/about')
def about():
    return render_template('about_us.html', title='About Us', pages=pages)

@app.route('/shop')
def shop():
    return render_template('shop.html', title='Shop', pages=pages)

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

@app.route('/changelog')
def change_log():
    return render_template('change_log.html', title='Changelog', pages=pages)

@app.route('/service/<string:name>')
def service_single(name):
    match name:
        case 'store':
            return render_template('quility.html', title='Organic Store', pages=pages)
        case 'dairy':
            return 'dairy service'
        case 'delivery':
            return 'delivery'
        case 'agricultural':
            return 'agricultural sevice'
        case 'products':
            return 'Organic products'
        case 'fresh_vegetables':
            return 'fresh vegetables'
        case _:
            return url_for('service')
        
@app.route('/shop/<string:name>')
def shop_single(name):
    match name:
        case 'white_nuts':
            return render_template('shop_single.html', title='White Nuts', pages=pages)
        case _:
            return f"<h1> {name} </h1>"

@app.route('/not_found')
@app.errorhandler(404)
def not_found(e = None):
    return render_template('404_Not_Found.html', title='404 Not Found', pages=pages, haven_t_form='haven-t-form')

if __name__ == '__main__':
    app.run(debug=True)