# Database Systems : Simplified Taxicab System

## Requirements

### Seeding the database

- pip install Faker

- pip install geopy

### Frontend

- Pandas

- pip install flask

- python3 -m pip install PyMySQL

## Setup

- Creating user:

```
    create user 'dbproject'@'localhost' IDENTIFIED BY 'password';
```

- Grant priviliges:

```
    GRANT ALL ON pdb1.* TO 'dbproject'@'localhost';
```

May need to repeat these two step twice if there is a duplicate email (chances are low):

- Create seed file:

```
    python db-seeder.py > test-db.sql
```

- Seed the database:

```
    mysql -u dbproject -p < test-db.sql
```

## Demo

- Start the flask frontend:

```
    python frontend.py
```

- Direct browser to:

```
	http://127.0.0.1:5000
```