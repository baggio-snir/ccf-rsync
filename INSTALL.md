# Installation

Rapatriez le dossier de l'applicatif dans un environnement virtuel (python venv).

Installez ensuite Django dans le venv : `py -m pip install Django`

Une fois Django installé dans le venv,
lancez les migrations,
ce qui va créer la base de données : `py manage.py migrate`

Avant de tester,
il est nécessaire de créer un premier "superuser"
via la commande `py manage.py createsuperuser`

L'applicatif est prêt à l'utilisation,
et vous pouvez lancer le serveur,
par exemple via `py manage.py runserver`
