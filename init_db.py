import sqlite3
import os

def reset_database():
    # Supprimer l'ancienne base si elle existe
    if os.path.exists('gmao.db'):
        os.remove('gmao.db')
        print("🗑️ Ancienne base de données supprimée")
    
    # Créer une nouvelle base de données
    conn = sqlite3.connect('gmao.db')
    cursor = conn.cursor()
    
    print("🔧 Création de la nouvelle base de données...")
    
    # Création de la table users
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK (role IN ('admin', 'technicien')),
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("✅ Table 'users' créée")
    
    # Création de la table pannes
    cursor.execute('''
        CREATE TABLE pannes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipement TEXT NOT NULL,
            description TEXT NOT NULL,
            priorite TEXT NOT NULL CHECK (priorite IN ('Faible', 'Moyenne', 'Élevée', 'Critique')),
            etat TEXT NOT NULL CHECK (etat IN ('En attente', 'En cours', 'Résolue', 'Fermée')),
            date_creation TIMESTAMP NOT NULL,
            cause TEXT,
            solution TEXT,
            observation TEXT,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    print("✅ Table 'pannes' créée")
    
    # Insertion des utilisateurs par défaut
    cursor.execute('''
        INSERT INTO users (username, password, role) 
        VALUES ('admin', 'admin123', 'admin')
    ''')
    
    cursor.execute('''
        INSERT INTO users (username, password, role) 
        VALUES ('technicien', 'tech123', 'technicien')
    ''')
    print("✅ Utilisateurs par défaut créés")
    
    # Insertion de pannes d'exemple
    pannes_exemple = [
        ('Compresseur A1', 'Fuite d\'air importante au niveau du joint', 'Élevée', 'En cours', 
         '2025-01-15 09:30:00', 'Joint défaillant', 'Remplacement du joint nécessaire', 
         'Arrêt de production requis', 1),
        ('Convoyeur B2', 'Bruit anormal et vibrations', 'Moyenne', 'En attente', 
         '2025-01-16 14:20:00', 'Roulement usé', '', 'Vérifier l\'alignement', 2),
        ('Pompe C3', 'Débit insuffisant', 'Faible', 'Résolue', 
         '2025-01-14 11:45:00', 'Filtre encrassé', 'Nettoyage du filtre effectué', 
         'Remettre en service normal', 1),
        ('Moteur D4', 'Surchauffe anormale', 'Critique', 'En cours',
         '2025-01-17 16:00:00', 'Ventilation bloquée', 'Nettoyage en cours',
         'Surveillance température requise', 2),
        ('Robot E5', 'Erreur de positionnement', 'Moyenne', 'Résolue',
         '2025-01-13 08:15:00', 'Capteur défaillant', 'Remplacement capteur effectué',
         'Calibrage terminé', 1)
    ]
    
    cursor.executemany('''
        INSERT INTO pannes (equipement, description, priorite, etat, date_creation, 
                          cause, solution, observation, user_id) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', pannes_exemple)
    print("✅ Pannes d'exemple ajoutées")
    
    # Vérification de la création
    cursor.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM pannes')
    panne_count = cursor.fetchone()[0]
    
    print(f"📊 Base de données créée avec succès :")
    print(f"   - {user_count} utilisateurs")
    print(f"   - {panne_count} pannes d'exemple")
    
    # Valider et fermer
    conn.commit()
    conn.close()
    
    print("\n🎉 Base de données initialisée avec succès !")
    print("📁 Fichier créé : gmao.db")
    print("\n👥 Comptes disponibles :")
    print("   🔑 Admin     : admin / admin123")
    print("   🔧 Technicien : technicien / tech123")
    print("\n▶️ Vous pouvez maintenant lancer : python app1.py")

if __name__ == '__main__':
    reset_database()