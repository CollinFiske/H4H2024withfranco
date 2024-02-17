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
"Be the Match On Campus SCU", "Belles Service Organization", 
"Biomedical Engineering Society", "Bird Up! SCU", 
"Black Business Association",
"Blockchain & Compliance Legal Society",
"BLSA (The Black Law Student  Association)", 
"Blueprints for Pangea",
"Bread Lover's Club",
"Bronco Foodie Club",
"Broncos for Life"
"C.A.E.S.A.R",
"Camp Kesem at Santa Clara University",
"Cannabis Law and Policy Group",
"Card Game Club",
"Chinese Student Association",
"Chinese Students and Scholars Association",
"ChIPs (Chiefs in IP)",
"Clara Craft Club",
"Club Bio",
"College Catholics",
"Commuter Student Union",
"Core Christian Fellowship",
"Criminal Law Society",
"Cultural Italian American Organization",
"DayBreak K-Pop Dance Crew",
"Delta Epsilon Mu, Inc",
"Delta Sigma Pi",
"Dynamic Rhythm",
"Economics Student Association",
"Engineers Without Borders",
"Environmental Law Society",
"EQSCU (Equality at Santa Clara Law)",
"Ethnic Studies Club",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
]
allClubs = sorted(allClubs)

@app.route('/')
def index():
   

    # Pass the content to the template for rendering
    return render_template('index.html', allClubs=allClubs)

if __name__ == '__main__':
    app.run(debug=True)

