# Refactoring : switch statements

Refactoring.guru, switch-statements : [lien](https://refactoring.guru/smells/switch-statements)

Le refactoring consiste à réécrire un code qui effectue une fonction pour qu'il soit plus lisible tout en effectuant la même fonction.

Ce code se concentre sur des codes qui utilisent les switch et les if de manière abusif (voir presentation.pdf)

## Installer le code
```
git clone <lien-de-clone-du-repo>
cd refactoring_switch_statements
pip install -r requirements.txt
```

## Que fait le code?

Dans votre terminal : `pytest` pour lancer les tests du fichier test_refactoring.
Dans le fichier test_refactoring.py :
- `test_original_parler()` lance le test sur le code "de if abusif"
- `test_refactored_parler()` lance le test sur le code refactored
On voit que les tests sont identiques et se passent tous les deux.

Le fichier main.py contient la fonction de "if abusif"

Le fichier animaux.py contient :
- une classe Animal avec comme attribut "type" pour le code de "if abusif"
- des classes Chien/Chat/Oiseau avec une méthode "parler"

Python ne connaît pas les interfaces. Il est plus intéressant de faire du polymorphisme (avec une classe interface Animal) dans des langages comme Java et rend le refactoring plus parlant.

### Auteur : Lilian Janicot
