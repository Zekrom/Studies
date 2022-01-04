# SCHOOLS_OUT

### Rappel du sujet

Afin d'optimiser au maximum l'allocation de ses salles de classe, une école souhaite déterminer le nombre minimum de salles nécessaires au déroulement de sessions d'activités prévues sur une journée.

### Format des données en entrée

En entrée, votre programme recevra en premier argument le chemin d'un fichier contenant les données à traiter au format JSON.
Ce fichier contiendra une liste d'objets représentant chacun une session prévue sur la journée.

Exemple:

```json[
  {
    "start": "09:00",
    "end": "10:00",
    "session_name": "Cours : Bases de données avec Hibernate",
    "teacher_name": "Nathan TRENET"
  },
  {
    "start": "09:00",
    "end": "10:00",
    "session_name": "Cours : Bases de données avec EntityFramework Core",
    "teacher_name": "Ethan TRANNET"
  }
]
```

## Analyse & recherches

Pour éviter une grande complexité j'ai pensé à créer une timeline qui rendrait accessible les cours à chaque instant _t_ .
* Essai échoué avec une _List_ puisque la collection n'est pas assez optimale (même en 2D) car pour créer une timeline il faudrait initialiser un nombre indéterminé d'élements puisque créer une case pour chaque demi-heure de cours pourrait se révéler insuffisant
* Essai réussi avec la data structure _Dict_ qu'on peut utiliser pour créer une timeline en insérant en _key_ l'instant t et par exemple une _list_ pour contenir les events 
Il ne reste plus ensuite qu'a parser,formatter & filtrer correctement pour avoir le résultat qui correspond au besoin
* La difficulté au niveau de la timeline aura été de gérer les cas ou les cours se passent au même moment,ceux qui s'enchainent (la fin & le début sont le même t) et les cas ou plusieurs cours se finissent au même moments & s'enchainent par d'autres cours car il peut y avoir à un instant t 7 events mais n'avoir besoin que de 4 salles


## Calcul de complexité

* Les assignations : le parsing ,la timeline,la réponse → 3
* Une boucle sur la liste des cours pour initialiser la timeline pour chaque instant t à checker → 6n
* Une boucle imbriquée avec laquelle on complète pour chaque temps t les cours actifs et on met à jour la valeur de réponse : 7n²
* T(n) = 7n² + 6n + 3

### Complexité d'ordre : O(n²)
