import os
import re

def check_templates():
    templates_dir = "templates"
    
    if not os.path.exists(templates_dir):
        print("❌ Le dossier 'templates' n'existe pas !")
        return
    
    print("🔍 Vérification de la syntaxe des templates Jinja2...\n")
    
    # Erreurs communes à détecter
    common_errors = [
        (r'{% if .+= =.+%}', "Double égal mal formaté (= =)"),
        (r'{% if .+==.+= %}', "Triple égal mal formaté (==)"),
        (r'{% if .+[^=]=[^=].+%}', "Simple égal au lieu de double égal"),
        (r'{%.+%}{%', "Blocs Jinja2 collés"),
        (r'{{.+}}{%', "Variables et blocs collés"),
    ]
    
    files_checked = 0
    errors_found = 0
    
    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(templates_dir, filename)
            files_checked += 1
            
            print(f"📄 Vérification de {filename}...")
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                file_errors = 0
                for line_num, line in enumerate(content.split('\n'), 1):
                    for pattern, description in common_errors:
                        if re.search(pattern, line):
                            print(f"   ❌ Ligne {line_num}: {description}")
                            print(f"      Code: {line.strip()}")
                            file_errors += 1
                            errors_found += 1
                
                if file_errors == 0:
                    print(f"   ✅ Aucune erreur détectée")
                else:
                    print(f"   ⚠️ {file_errors} erreur(s) trouvée(s)")
                
            except Exception as e:
                print(f"   ❌ Erreur de lecture: {e}")
                errors_found += 1
            
            print()
    
    print(f"📊 Résumé:")
    print(f"   - {files_checked} fichiers vérifiés")
    print(f"   - {errors_found} erreurs trouvées")
    
    if errors_found == 0:
        print("\n✅ Tous les templates semblent corrects !")
    else:
        print(f"\n⚠️ {errors_found} erreur(s) à corriger")

if __name__ == '__main__':
    check_templates()