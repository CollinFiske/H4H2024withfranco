from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Read the content of clubs.html
    file_path=r"C:\Users\franc\OneDrive\Documentos\GitHub\H4H2024withfranco\templates\clubs.html"
    
    with open(file_path, 'r') as file:
        clubs_content = file.read()

    # Pass the content to the template for rendering
    return render_template('index.html', clubs_content=clubs_content)

if __name__ == '__main__':
    app.run(debug=True)

    # Render the template with data
    #return render_template('index.html', name=name, age=age, interests=interests)

#if __name__ == '__main__':
    #app.run(debug=True)
