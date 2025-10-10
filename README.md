# 🔧 Application Flask- Gestion des Pannes

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.0+-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

Une application web de **Gestion de Maintenance** développée lors d'un stage de 2 mois à l'**Office National de l'Eau Potable (ONEE-BO)**.

## 📋 À propos du projet

Cette application permet la gestion complète des pannes dans un environnement industriel, offrant une interface intuitive pour :
- 📝 Déclarer et suivre les pannes
- 📊 Visualiser les statistiques via un dashboard
- 👥 Gérer les utilisateurs et les permissions
- 📈 Analyser l'historique des interventions

## ✨ Fonctionnalités principales

- 🔐 **Authentification sécurisée** - Système de login avec gestion des sessions
- ➕ **Ajout de pannes** - Formulaire complet avec validation des données
- 📋 **Historique détaillé** - Liste complète des pannes avec filtres et recherche
- 📊 **Dashboard administrateur** - Statistiques et indicateurs en temps réel
- 📱 **Interface responsive** - Compatible mobile et desktop
- 🗄️ **Base de données SQLite** - Stockage local sécurisé et performant

## 🛠️ Technologies utilisées

### Backend
- **Python 3.8+** - Langage de programmation principal
- **Flask** - Framework web léger et performant
- **SQLAlchemy** - ORM pour la gestion de base de données
- **Werkzeug** - Utilitaires de sécurité

### Frontend
- **HTML5** - Structure des pages
- **CSS3** - Stylisation responsive
- **Jinja2** - Moteur de templates

### Base de données
- **SQLite** - Base de données embarquée

## 📁 Structure du projet

```
gmao_pannes/
├── app1.py                 # 🚀 Application principale Flask
├── init_db.py            # 🏗️ Script d'initialisation de la base de données
├── gmao.db               # 🗄️ Base de données SQLite (générée automatiquement)
├── static/               # 🎨 Fichiers statiques
│   ├── style.css         # 🎨 Feuille de style principale
│   └── images/           # 🖼️ Ressources graphiques
│       └── logo.png      # 🏢 Logo ONEP
└── templates/            # 📄 Templates HTML
    ├── base.html         # 🏠 Template de base
    ├── login.html        # 🔐 Page de connexion
    ├── ajouter_panne.html # ➕ Formulaire d'ajout
    ├── historique.html   # 📋 Liste des pannes
    └── dashboard.html    # 📊 Tableau de bord
```

## 🚀 Installation et configuration

### Prérequis
- Python 3.8 ou version supérieure
- pip (gestionnaire de paquets Python)

### Installation étape par étape

1. **Cloner le repository**
   ```bash
   git clone https://github.com/votre-username/gmao-pannes.git
   cd gmao-pannes
   ```

2. **Créer un environnement virtuel** (recommandé)
   ```bash
   python -m venv venv
   
   # Activation
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialiser la base de données** ⚠️ **OBLIGATOIRE**
   ```bash
   python init_db.py
   ```

5. **Lancer l'application**
   ```bash
   python app1.py
   ```

6. **Accéder à l'application**
   
   Ouvrez votre navigateur et allez sur : `http://localhost:5000`

## 🌐 Pages disponibles

| Route | Description | Accès |
|-------|-------------|-------|
| `/` | Page d'accueil | Public |
| `/login` | Authentification | Public |
| `/ajouter_panne` | Ajouter une nouvelle panne | Authentifié |
| `/historique` | Consulter l'historique | Authentifié |
| `/dashboard` | Tableau de bord admin | Administrateur |

## 📊 Captures d'écran

### 🔐 Page de connexion

<img width="1080" height="1050" alt="Untitled (1080 x 1070 px) (1080 x 1050 px)" src="https://github.com/user-attachments/assets/bf64a188-51a5-4f59-a0bd-6c8dcef41ba9" />

### ➕ Ajout de panne
<img width="1494" height="2085" alt="Untitled design (6)" src="https://github.com/user-attachments/assets/fb288e0e-316e-4e1f-8227-729617766926" />


### 📋 Historique des pannes
<img width="1498" height="1573" alt="Untitled design (5)" src="https://github.com/user-attachments/assets/d069a82d-91f3-421a-a68f-1fdbd1c687dc" />


### 📊 Dashboard administrateur

<img width="1913" height="2992" alt="FIG14" src="https://github.com/user-attachments/assets/a8903a8a-558e-4b56-a731-05e8ce1958b3" />

## 🧪 Tests et validation

- ✅ Tests fonctionnels sur les principales fonctionnalités
- ✅ Validation de la base de données
- ✅ Tests de compatibilité navigateurs
- ✅ Tests de responsive design

## 🔧 Développement

### Commandes utiles

```bash
# Réinitialiser la base de données
python init_db.py

# Lancer en mode debug
export FLASK_DEBUG=1
flask run

# Générer requirements.txt
pip freeze > requirements.txt
```

### Structure de la base de données

Les principales tables incluent :
- `users` - Gestion des utilisateurs
- `pannes` - Enregistrement des pannes
- `interventions` - Suivi des réparations

## 🤝 Contexte du stage

Ce projet a été développé dans le cadre d'un **stage de 2 mois** (Juillet-Août 2025) au sein de l'**Office National de l'Eau Potable (ONEE-BO)**, sous l'encadrement de **Ayoub ZERZOUR**, Chef de station.

### Objectifs atteints
- ✅ Digitalisation du processus de gestion des pannes
- ✅ Interface utilisateur intuitive et moderne
- ✅ Système de reporting et statistiques
- ✅ Documentation complète du projet

## 👨‍💻 Auteur

**Yakout BENSSALLAM**
- 🎓 Étudiante en Master IT
- 🏢 Stagiaire ONEP (Juillet-Août 2025)
- 💼 LinkedIn : BENSSALLAM Yakout
- 📧 Email : yakoutbenssallam@gmail.com

## 📄 Licence

Ce projet a été développé dans un cadre éducatif et professionnel.

## 🙏 Remerciements

- **M. Ayoub ZERZOUR** - Chef de station et encadrant du stage
- **Équipe ONEP** - Pour leur accueil et leur confiance
- **Office National de l'Eau Potable (ONEP)** - Organisme d'accueil

---

⭐ **N'hésitez pas à mettre une étoile si ce projet vous intéresse !**








