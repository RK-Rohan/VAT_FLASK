### INSTALLATION OF BMIT VAT - FLASK EDITION 

#### Install Virtual Environment 

```plaintext
pip install virtualenv
```

#### Activate Virtual Environment

```plaintext
venv\scripts\activate
```

#### Install All required Pakage

```plaintext
pip install -r requirements.txt
```

#### Configure MySQL Database 

add the code below to the app.py 

```python
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@hostname/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
```

#### Flask-Migrate Database

```plaintext
flask db init
flask db migrate -m “Initial migration.”
flask db upgrade
```