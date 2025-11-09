from flask import Flask, render_template, request

app = Flask(__name__)

# Sample project data
projects = [
    {"title": "Library Management System", "image": "project1.jpg", "description": "Efficient system to manage library operations."},
    {"title": "ML Digit Classifier", "image": "project2.jpg", "description": "Classifies digits using ML algorithms."},
    {"title": "Weather App", "image": "project3.jpg", "description": "Shows real-time weather updates."}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ""
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        msg = request.form['message']
        message = f"Thanks {name}, your message has been received!"
        # Here you can save messages to a DB or send email
    return render_template('contact.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
