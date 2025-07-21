from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'data/pannes.json'

def charger_pannes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def enregistrer_pannes(pannes):
    with open(DATA_FILE, 'w') as f:
        json.dump(pannes, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pannes')
def pannes():
    liste = charger_pannes()
    return render_template('pannes.html', pannes=liste)

@app.route('/panne/<int:id>')
def panne_detail(id):
    pannes = charger_pannes()
    panne = next((p for p in pannes if p['id'] == id), None)
    return render_template('panne_detail.html', panne=panne)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        pannes = charger_pannes()
        nouvelle = {
            "id": len(pannes) + 1,
            "equipement": request.form['equipement'],
            "date": request.form['date'],
            "description": request.form['description'],
            "statut": request.form['statut']
        }
        pannes.append(nouvelle)
        enregistrer_pannes(pannes)
        return redirect(url_for('pannes'))
    return render_template('nouvelle_panne.html')

@app.route('/historique')
def historique():
    pannes = charger_pannes()
    return render_template('historique.html', pannes=pannes)

if __name__ == '__main__':
    app.run(debug=True)
