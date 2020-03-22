Run :

```
virtualenv --python python3 env
source env/bin/activate
pip3 install -r requirements.txt
source env/bin/activate
python manage.py migrate
python3 manage.py loaddata tracker/fixtures/exercise.json
python3 manage.py runserver localhost:8000
``
