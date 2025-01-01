# bootcamp_teachmemore

# 🐳 Conteneurisation d'une application Flask Python avec Docker et Vagrant

## 🚀 Fonctionnalités

- 🌐 **Application Flask** : Une application web simple avec un front-end stylé en Bootstrap.
- 📦 **Conteneurisation avec Docker** : Un Dockerfile et un docker-compose pour déployer l'application.
- 💻 **Machine Virtuelle via Vagrant** : Une VM Ubuntu prête à l'emploi configurée automatiquement.
- 🤖 **Automatisation GitHub Actions** : Un workflow CI pour tester la construction des images Docker.
- 📖 **Documentation complète** : Instructions détaillées pour configurer, exécuter et utiliser le projet.

## 📂 Arborescence du Projet

portfolio_app/
├── app.py
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   └── index.html
├── Dockerfile
├── requirements.txt
└── docker-compose.yml

## 📋 Prérequis

Avant de commencer, installer les outils suivants : 
- **Git** 
- **Vagrant** 
- **VirtualBox**
- **Docker** et **docker-compose**

### 1 Cloner le dépôt
- git clone https://github.com/Lengula/bootcamp_teachmemore.git
- cd bootcamp_teachmemore

### 2 Lancer la VM
- vagrant up

connecter à la vm via ssh
- vagrant ssh

### 3 Démarrer l'application avec Docker

cd /atelier/app_flask

Lancer l'application
- docker-compose up

L'application sera accessible depuis le navigateur
http://localhost:5000

# 💡 À propos
Ce projet a été conçu pour :

- **🌱 Apprendre les bases de Docker, Flask et Vagrant.**
- **🔗 Explorer l'intégration de plusieurs technologies.**

