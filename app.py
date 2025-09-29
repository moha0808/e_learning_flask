from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Courses Page
@app.route('/courses')
def courses():
    return render_template('courses.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Signup Page
@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
