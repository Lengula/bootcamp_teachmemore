from flask import Flask, render_template

app = Flask(__name__)

# Exemple de liste de projets
projects = [
    {
        "title": "Mon site web personnel",
        "description": "Un site vitrine pour présenter mon profil et mes compétences.",
        "link": "https://github.com/utilisateur/portfolio"
    },
    {
        "title": "Application de gestion de tâches",
        "description": "Une application pour gérer des tâches au quotidien, avec des rappels et des priorités.",
        "link": "https://github.com/utilisateur/todo-app"
    },
    {
        "title": "Analyse de données Twitter",
        "description": "Un projet d’analyse de données sur Twitter pour détecter les tendances et les hashtags populaires.",
        "link": "https://github.com/utilisateur/twitter-analysis"
    }
]

@app.route('/')
def index():
    return render_template("index.html", projects=projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
