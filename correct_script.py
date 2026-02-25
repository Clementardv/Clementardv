"""Module de demonstration conforme."""
def addition(a: int,b: int) -> int:
    """Retourne la somme de deux nombres."""
    return a + b

def main():
    """Point d'entrée principale."""
    resultat = addition(2,3)
    print("Résultat : ",resultat)

if __name__ == "__main__":
    main()
