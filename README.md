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

### Complexité temporelle

* Étant donné qu'on traite une liste de cours ,on considère n comme étant un cours 
* Les assignations : le parsing ,la timeline,la réponse → 3
* Une boucle sur la liste des cours pour initialiser la timeline pour chaque instant t à checker : 4 assignations,2 comparaison → 6n
* Une boucle imbriquée avec laquelle on complète pour chaque temps t les cours actifs et on met à jour la valeur de réponse : 3 assignations (heure de début,heure de fin,réponse),2 comparaison dans le if, 1 comparaison dans l'expression ternaire et un append pour completer la timeline → 7n²
* T(n) = 7n² + 6n + 3

#### Complexité d'ordre : O(n²)

### Complexité spatiale

* On garde n comme étant un cours 
* On considère la liste des cours parsée comme 8n puisque l'objet a 8 champs
* On rajoute à ça argv[1], open file, réponse, mn, mx : 5
* La timeline ,un _dict_ dont les _key_ seront au pire 2n (on rajoute l'heure de début & l'heure de fin si elles n'y sont pas), multiplié par n le nombre cours actifs à l'instant
* donc 2n²
* S(n) = 2n² + 8n + 5

#### Complexité d'ordre : O(n²)

### Conclusion

Même si une complexité d'ordre O(n²) peut ne pas paraître optimal j'ai un programme qui assume un gros volume de données avec un temps d'éxecution honorable **inférieur à un centième de seconde**


Test réalisé avec le fichier strengthenschedule.json qui contient plus de 1000 cours 

```
PS C:\Users\Zekrom\IdeaProjects\ALG4\schools_out> python schools_out.py strengthenschedule.json
400
--- 0.009767532348632812 seconds ---
```
