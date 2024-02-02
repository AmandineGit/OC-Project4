# Documentation du logiciel de gestion de tournois d'échecs
:grinning: Fait par @AmandineGit le 2 fevrier 2024

## Utilisation du logiciel de gestion de tournois d'échecs
Il s'agit d'un programme permettant la gestion de tournois d'échecs dans un contexte hors Internet.
Ce programme vous permt de :
+ <span style="color:orange"> Créer un tournoi </span>
+ <span style="color:orange"> Planifier un tournoi </span>
+ <span style="color:orange"> Inscrire des joueurs à un tournoi </span>
+ <span style="color:orange"> Lancer un round </span>
+ <span style="color:orange"> Clôturer un round </span>
+ <span style="color:orange"> Afficher un rapport </span>

Les données de travail seront oragnisées dans des fichiers Json, enregistrés dans le dossier datas. </br>

### Création de l'environnement virtuel necéssaire pour l'execution
- [ ] Créer un environnement virtuel nommé `env` grace à la commande : `>>> python3 -m venv env`
- [ ] Activer l'environnment virtuel crée avec la commande : `>>> source env/bin/activate`
- [ ] Vérifier, votre prompt doit afficher : <span style="color:green">(env)</span> `user@machine:~/repertoire_projet$`


### Installation des paquets necéssaires 
- [ ] Installer les paquets dans la version recommandée dans le requirement.txt grace à la commande pip : </br>
     `(env) user@machine:~/repertoire_projet$ pip install paquet_a_installer==version`</br>
- [ ] Vérifier l'installation des paquets grace à :</br>
       ```(env) user@machine:~/repertoire_projet$ pip freeze```</br>
        Le retour devrait correspondre à :</br>
       `flake8==7.0.0`</br>
       `flake8-html==0.4.3`</br>
       `Jinja2==3.1.3`</br>
       `MarkupSafe==2.1.4`</br>
       `mccabe==0.7.0`</br>
       `pycodestyle==2.11.1`</br>
       `pyflakes==3.2.0`</br>
       `Pygments==2.17.2`</br>

### Execution du programme

 - [ ] Accéder au répertoire projet et lancer le programme :</br>
       `(env) user@machine:~/repertoire_projet$ python3 ./main.py`</br>

