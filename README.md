README
======

Please follow the guide to install the project


Running the project
===================

Clone the project

	git clone https://github.com/rcshadman/mathspace.git

Install requirements

    pip install -r requirement.txt

Make migrations and migrate

    python manage.py makemigrations
    python manage.py migrate

Run Server
	
	python manage.py runserver

Access the app

    http://127.0.0.1:8000/dice

To run the algorithm on console
	
    python prob_unit.py