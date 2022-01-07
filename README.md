# SCHOOLS_OUT

### Rappel du sujet

Afin d'optimiser au maximum l'allocation de ses salles de classe, une école souhaite déterminer le nombre minimum de salles nécessaires au déroulement de sessions d'activités prévues sur une journée.

### Format des données en entrée

En entrée, votre programme recevra en premier argument le chemin d'un fichier contenant les données à traiter au format JSON.
Ce fichier contiendra une liste d'objets représentant chacun une session prévue sur la journée.

Exemple:

```json
[
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
* Essai échopué avec la data structure _Dict_ qu'on peut utiliser pour créer une timeline en insérant en _key_ l'instant t et par exemple une _list_ pour contenir les events 
Il ne reste plus ensuite qu'a parser,formatter & filtrer correctement pour avoir le résultat qui correspond au besoin mais complexité trop grande
* La difficulté au niveau de la timeline aura été de gérer les cas ou les cours se passent au même moment,ceux qui s'enchainent (la fin & le début sont le même t) et les cas ou plusieurs cours se finissent au même moments & s'enchainent par d'autres cours car il peut y avoir à un instant t 7 events mais n'avoir besoin que de 4 salles
* Essai réussi avec complexité plus courte en notant chaque minute de la journée dans un tableau en tant que timeline et en itérant pour chaque minute le nombre de cours actifs


## Calcul de complexité

### Complexité temporelle

* Étant donné qu'on traite une liste de cours ,on considère n comme le nombre de cours
* On considère aussi m = (mx-mn) la plus longue durée d'un cours
* On 3 assignations ,puis 2 assignations par boucle sur la liste de cours et pour chaque cours on boucle sur sa durée
* J'utilise aussi la fonction max qui a une complexité de n pour renvoyer la valeur maximale du tableau
* T(n) = 3 + 3mn


#### Complexité d'ordre : O(nm)

### Complexité spatiale

* On garde n comme le nombre de cours.

* On considère la liste des cours parsée comme 8n puisque l'objet a 8 champs
* On rajoute à ça argv[1], open file, mn, mx : 4
* La timeline , un tableau de 1440 cases qui représente chaque minute d'un jour
* S(n) = 8n + 1444

#### Complexité d'ordre : O(n)

### Conclusion

La solution me paraît correcte puisque les complexité temporelle & spatiale sont suffisamment optimales pour traiter d'une journée de cours quelque soit les horaires (même les plus irréguliers ) rapidement et efficacement 
