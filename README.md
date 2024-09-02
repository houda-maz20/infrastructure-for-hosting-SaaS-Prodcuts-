## Automatisation et Optimisation de la Gestion de l'Infrastructure Informatique
Ce projet est un projet PFA qui vise à automatiser et optimiser la gestion de l'infrastructure informatique 
en utilisant des technologies telles que Docker, Ansible, et Flask. Le projet permet de gérer
des conteneurs Nginx et Odoo via une interface web intuitive, et inclut également un environnement
de production avec Grafana et Prometheus pour la surveillance.

## Table des Matières
1. [Aperçu](#aperçu)
2. [Technologies Utilisées](#technologies-utilisées)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Structure du Projet](#structure-du-projet)
6. [Contribution](#contribution)
7. [Licence](#licence)
## Aperçu
Le projet permet à l'utilisateur de lancer des conteneurs Docker pour Nginx et Odoo sur des plages de ports spécifiques.
Les conteneurs peuvent être configurés pour s'exécuter pendant des périodes définies (1 jour, 1 semaine, 1 mois) à l'aide d'Ansible.
Une interface web construite avec Flask permet de gérer ces conteneurs de manière intuitive.

## Technologies Utilisées
- *Docker* : Pour la création et la gestion des conteneurs.
- *Ansible* : Pour l'orchestration du déploiement des conteneurs.
- *Flask* : Pour la création de l'interface web.
- *HTML/CSS/JavaScript* : Pour l'interface utilisateur.
- *Prometheus et Grafana* : Pour la surveillance et la visualisation des métriques.
## Installation
### Prérequis
- Docker et Docker Compose installés
- Ansible installé
- Python 3.x et pip installés
## Étapes d'installation
1. Clonez ce dépôt :
2. 
   
   git clone https://github.com/votre_nom_utilisateur/votre_projet.git
   cd votre_projet
2.Installez les dépendances Python nécessaires :


pip install -r requirements.txt
Configurez les fichiers nginx_playbook.yml et odoo_playbook.yml avec les chemins corrects si nécessaire.

3.Exécutez l'application Flask :


python app.py
Accédez à l'interface web via votre navigateur à l'adresse : http://localhost:5000

## Utilisation
### Lancer un Conteneur
- Sélectionnez le type de conteneur que vous souhaitez exécuter (Nginx ou Odoo).
- Choisissez la durée d'exécution du conteneur (1 jour, 1 semaine, ou 1 mois).
- Cliquez sur "Run Container" pour démarrer le conteneur.
- L'interface affichera un message indiquant si le conteneur a été démarré avec succès ou si une erreur est survenue (par exemple, si aucun port disponible n'a été trouvé).
## Surveillance avec Grafana et Prometheus
Les conteneurs de production pour Grafana, Prometheus, et d'autres services de surveillance peuvent être démarrés 
en utilisant le fichier docker-compose.yml fourni :


docker-compose up -d
Accédez à Grafana via : http://localhost:3001

## Structure du Projet
```
├── app.py                     # Application Flask principale
├── Dockerfile                 # Dockerfile pour l'image Nginx
├── dockerfileodoo             # Dockerfile pour l'image Odoo
├── playbooks/                 # Répertoire contenant les playbooks Ansible
│   ├── nginx_playbook.yml
│   └── odoo_playbook.yml
├── templates/                 # Répertoire pour les templates HTML
│   └── index.html             # Fichier HTML de l'interface utilisateur
├── inventory/                 # Fichier d'inventaire Ansible
├── prometheus.yml             # Fichier de configuration pour Prometheus
├── docker-compose.yml         # Configuration Docker Compose pour la production
├── docker-compose.odoo.yml    # Configuration Docker Compose spécifique pour Odoo
├── nginx.conf                 # Fichier de configuration Nginx
├── scripts/                   # Scripts Python pour exécuter les conteneurs
│   ├── script_nginx.py
│   └── script_odoo.py
└── Rapport_de_projet/         # Dossier contenant les documents du projet
```
