# FECHETAH Amazigh -Projet 4 Developpez-un-programme-logiciel-en-Python
***Application de gestion de tournoi d'échecs avec base de données.***

_Réalisé sous Windows 11 - Python version Python 3.10.1_


## Sommaire

1. [Initialisation du projet](#id-section1)
    1. [Windows](#id-section1-1)
    1. [MacOS et Linux](#id-section1-2)
    3. [Générer un rapport flake8](#id-section1-3)
2. [Options des menus](#id-section2)
    1. [Menu principal](#section2-1)
    2. [Rapports](#section2-2)
3. [Exemples d'affichage](#section3)


<div id='id-section1'></div>

## 1. Initialisation du projet

<div id='id-section1-1'></div>


#### i. Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.
###### Récupération du projet

    $ git clone https://github.com/Amazigh0895/Developpez-un-programme-logiciel-en-Python.git

###### Activer l'environnement virtuel
    $ cd Developpez-un-programme-logiciel-en-Python
    $ python -m venv env 
    $ source env\scripts\activate
    
###### Installer les paquets requis
    $ pip install -r requirements.txt

###### Lancer le programme
    $ python main.py


<div id='id-section1-2'></div>

---------

#### ii. MacOS et Linux :
Dans le terminal, naviguer vers le dossier souhaité.
###### Récupération du projet

    $ git clone https://github.com/Amazigh0895/Developpez-un-programme-logiciel-en-Python.git

###### Activer l'environnement virtuel
    $ cd Developpez-un-programme-logiciel-en-Python
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### Installer les paquets requis
    $ pip install -r requirements.txt

###### Lancer le programme
    $ python3 main.py


<div id='id-section1-3'></div>

----------

#### iii. Générer un rapport flake8

    $ flake8 --format=html --htmldir=flake8_report

**Vous trouverez le rapport dans le dossier _'flake8-report'_.**
