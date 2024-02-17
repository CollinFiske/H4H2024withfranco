from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data
    name = "John"
    age = 30
    interests = ["Python", "Flask", "Jinja"]

    # Render the template with data
    return render_template('index.html', name=name, age=age, interests=interests)

if __name__ == '__main__':
    app.run(debug=True)
