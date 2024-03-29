## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement
Le job de déploiement se produit dès lors qu'un changement est effectué sur la branche `main` et que les jobs précendents de la CI (`lint-and-test` et `build-and-push`) passent avec succès. Lors de ce job une image est envoyée à Heroku puis publiée.

Afin de pouvoir déployer sur Heroku, il vous faut une application.
- Connectez-vous à Heroku et aller à l'adresse https://dashboard.heroku.com/apps
- Cliquez sur "New" puis sur "Create new app"
- Complétez le champ "App name" avec "celiats-python-oc-lettings-13"
- Sélectionnez "Europe" dans le sélecteur "Choose a region"
- Cliquez sur "Create app"

Pour que le déploiement fonctionne correctement, il faut que les variables d'environnement CircleCI soient correctement configurées.
- Aller sur l'application web CircleCI
- Dans le menu, cliquez sur "Organization Settings"
- Dans le menu, cliquez sur "Contexts"
- Cliquez sur "Create context" et donnez-lui comme nom "lettings"
- Une fois dans votre context, créez les variables d'environnement suivantes :
  - DATABASE_NAME
  - HEROKU_API_KEY
  - HEROKU_APP_NAME
  - HEROKU_TOKEN
  - SECRET_KEY
  - SENTRY_IDS

## Sentry
Afin de suivre les erreurs de notre projet, nous utilisons Sentry. Pour créer un nouveau projet Sentry, il faut :
- Connectez-vous à Sentry et allez à l'adresse https://lettings.sentry.io/projects/
- Dans le menu latéral, cliquez sur "Projects"
- Cliquez sur "Create Project"
- Dans la section "1. Choose your platform", sélectionnez "DJANGO"
- Dans la section "2. Set your alert frequency", sélectionnez "Alert me on every new issue"
- Dans la section "Name your project and assign it a team", "Project name", laissez le nom "python-django"
- Cliquez sur "Create project"
- Vous allez ensuite être redirigé vers la page "Configure Django SDK", suivez les instructions afin de terminez la configuration de Sentry.
