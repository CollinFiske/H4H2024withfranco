from flask import Flask, render_template

app = Flask(__name__)

allClubs = ["ACM (Association for Computing Machinery)",
"Acts 2 Christian Fellowship",
"African Student Association",
"AGES (Association of Graduate Engineering Students)",
"AI Collaborate",
"Alpha Kappa Psi",
"Alpha Phi Omega",
"Alpha Psi Omega",
"American Civil Liberties Union (ACLU)",
"American Constitution Society Santa Clara",
"American Institute of Aeronautics and Astronautics",
"American Sign Language Club",
"American Society of Mechanical Engineers",
"APALSA",
"Armenian Students Association",
"Art Law Society",
"Artificial Intelligence Student Association (AISA)",
"Asian & Pacific-Islander Student Union",
"Associated General Contractors of America",
"Association for Computing Machinery - Women's Chapter",
"Banda Seleccion de Santa Clara",
"Barkada of SCU",
"AI"
]


@app.route('/')
def index():
    # Read the content of clubs.html
    #file_path=r"C:\Users\franc\OneDrive\Documentos\GitHub\H4H2024withfranco\templates\clubs.html"
    
    #with open(file_path, 'r') as file:
        #clubs_content = file.read()

    # Pass the content to the template for rendering
    return render_template('index.html', allClubs=allClubs)

if __name__ == '__main__':
    app.run(debug=True)

    # Render the template with data
    #return render_template('index.html', name=name, age=age, interests=interests)

#if __name__ == '__main__':
    #app.run(debug=True)
