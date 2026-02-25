import sys
import subprocess
from pathlib import Path

def pylint(fichier_path):
    if not Path(fichier_path).exists():
        print('le fichier est introuvable')
        return 1
    try:
        process = subprocess.run(["pylint", fichier_path],check = False)
        return process.returncode
    except FileNotFoundError:
        print("Pylint n'est pas installer")
        return 1

def main():
    if len(sys.argv) != 2 :
        print("Usage : python check_quality.py <chemin>")
        sys.exit(1)
    
    fichier = sys.argv[1]
    code = pylint(fichier)

    if code == 0:
        print("Le code est de qualité")
    else:
        print ("probleme detecté (code ",code," )")
    sys.exit(code)

if __name__ == "__main__":
    main()
