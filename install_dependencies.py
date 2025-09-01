import subprocess
import sys
import os

def install_dependencies():
    """Installer automatiquement toutes les dépendances nécessaires"""
    
    print("🚀 Installation des dépendances")
    print("=" * 50)
    
    dependencies = [
        ("Flask", "flask"),
        ("OpenPyXL (Excel)", "openpyxl"),
        ("ReportLab (PDF)", "reportlab")
    ]
    
    failed_installs = []
    
    for name, package in dependencies:
        print(f"\n📦 Installation de {name}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                                stdout=subprocess.DEVNULL, 
                                stderr=subprocess.DEVNULL)
            print(f"✅ {name} installé avec succès")
        except subprocess.CalledProcessError:
            print(f"❌ Erreur lors de l'installation de {name}")
            failed_installs.append(name)
    
    print("\n" + "=" * 50)
    
    if failed_installs:
        print(f"⚠️ Échec d'installation pour : {', '.join(failed_installs)}")
        print("\n💡 Essayez manuellement :")
        for name, package in dependencies:
            if name in failed_installs:
                print(f"   pip install {package}")
    else:
        print("✅ Toutes les dépendances ont été installées avec succès !")
        print("\n🎉 Vous pouvez maintenant :")
        print("   1. Exécuter : python init_db_fixed.py")
        print("   2. Lancer l'app : python app.py")
        print("   3. Accéder à : http://127.0.0.1:5000")
    
    print("\n📋 Fonctionnalités d'export disponibles :")
    print("   📊 Export Excel complet (admin uniquement)")
    print("   📄 Export PDF complet (admin uniquement)")
    print("   📊 Export Excel par panne (admin uniquement)")
    print("   📄 Export PDF par panne (admin uniquement)")

def check_installation():
    """Vérifier si les dépendances sont installées"""
    print("🔍 Vérification des dépendances...")
    
    modules_to_check = [
        ("flask", "Flask"),
        ("openpyxl", "OpenPyXL"),
        ("reportlab", "ReportLab")
    ]
    
    all_installed = True
    
    for module, name in modules_to_check:
        try:
            __import__(module)
            print(f"✅ {name} est installé")
        except ImportError:
            print(f"❌ {name} n'est pas installé")
            all_installed = False
    
    return all_installed

if __name__ == '__main__':
    print("🔧 Gestionnaire d'Installation")
    print("=" * 40)
    
    if not check_installation():
        print("\n🚀 Installation des dépendances manquantes...")
        install_dependencies()
    else:
        print("\n✅ Toutes les dépendances sont déjà installées !")
        print("\n🎯 Prêt à utiliser l'application GMAO avec exports !")
        print("\n📋 Fonctionnalités disponibles :")
        print("   • Gestion complète des pannes")
        print("   • Dashboard administrateur")
        print("   • Export Excel de l'historique complet")
        print("   • Export PDF de l'historique complet")
        print("   • Export Excel détaillé par panne")
        print("   • Export PDF détaillé par panne")