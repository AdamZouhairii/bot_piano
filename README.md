# musica-bot![ico](https://user-images.githubusercontent.com/97172783/213868140-600839da-a1b0-4c43-90a5-c9d7130ad417.png)

Ce repository contient deux  bot qui utilise PyAutoGUI pour jouer du piano sur votre ordinateur.
Le fichier PianoBot joue sur le piano que j'ai crée l'autre fichier joue du piano sur un site en ligne avec un piano virtuel(le lien et dans le fichier).

### Avant de commencer, assurez-vous de télécharger les packages PyAutoGUI et Tkinter.


Ce code est un programme en Python qui utilise la bibliothèque pyautogui et tkinter pour créer un bot de piano qui peut jouer des notes de musique à l'aide de touches du clavier et simuler des clics de souris sur l'écran. Le programme contient également une interface graphique qui permet à l'utilisateur d'entrer des séquences de notes musicales pour que le bot les joue.

Le code commence par importer les bibliothèques pyautogui, tkinter et time. Il définit également une liste de notes de musique appelée "moz". Cette liste contient une séquence de notes musicales que le bot peut jouer à l'aide de touches du clavier.

Ensuite, il y a plusieurs fonctions définies dans le code. La première fonction "press" prend un argument "touche" qui correspond à une touche du clavier et utilise les fonctions pyautogui "keyDown" et "keyUp" pour simuler l'appui et la libération de la touche correspondante.

La deuxième fonction "click" prend deux arguments "x" et "y" qui correspondent aux coordonnées de l'emplacement où le clic de souris doit être simulé. Cette fonction utilise la fonction pyautogui "click" pour simuler le clic de souris à l'emplacement correspondant.

La troisième fonction "note_vers_touche" prend un argument "note" qui correspond à une note de musique et renvoie la touche correspondante sur le clavier qui doit être utilisée pour jouer cette note. Cette fonction utilise un dictionnaire pour associer chaque note de musique à une touche spécifique du clavier.

La quatrième fonction "piano" prend un argument "note" qui correspond à une note de musique et utilise la fonction "note_vers_touche" pour trouver la touche correspondante, puis utilise la fonction "press" pour simuler l'appui et la libération de la touche correspondante.

La cinquième fonction "test" est une fonction de test qui utilise la boucle "while" pour jouer la séquence de notes de musique "moz" en utilisant la fonction "piano" pour chaque note. Cette fonction utilise également la fonction "click" pour simuler un clic de souris à une position spécifique à l'écran.

La sixième fonction "jouer_les_note" est la fonction principale qui est appelée lorsque l'utilisateur appuie sur le bouton "Jouer" dans l'interface graphique. Cette fonction utilise les widgets Entry dans l'interface graphique pour récupérer trois séquences de notes musicales entrées par l'utilisateur, puis les joue en utilisant la fonction "jouer" qui utilise la fonction "piano" pour chaque note et utilise la fonction "time.sleep" pour faire une pause de 0,5 seconde entre chaque note.

Enfin, le code crée une interface graphique en utilisant tkinter. L'interface graphique contient trois widgets Entry pour entrer les séquences de notes musicales et deux boutons "Jouer" et "Exemple" qui appellent respectivement les fonctions "jouer_les_note" et "test" lorsque l'utilisateur appuie sur eux. La fonction "mainloop" est utilisée pour exécuter l'interface graphique en continu.



## Comment se servir du code ?

Pour commencer, il faut que les deux pages soient interposées comme ceci :

<img width="559" alt="ex1" src="https://user-images.githubusercontent.com/97172783/230633213-7540f7da-0ffb-418e-916b-6c3ad0ba6be9.png">



Ensuite, on clique sur "exemple" où l'on entre les notes que l'on souhaite, comme ceci :

<img width="553" alt="ex2" src="https://user-images.githubusercontent.com/97172783/230633281-284b418c-b2d5-44ca-83eb-093eb42960b0.png">

