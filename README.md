# MINIDB BOOK LIBRARY

Designed a Mini-Database Book Library that declares columns data-types,CRUD Operations,basic indexing,primary and Unique keys and some joinings,and a Flask-based CRUD web app to demonstrate real usage.

## Features

- Table definitions with data-types.eg(Integer,Text)
- CRUD Operations(CREATE,READ,UPDATE,DELETE)
- Primary and Unique Keys constraints.
- Basic Indexing
- SQL-like interface-REPL (INSERT,CREATE TABLE,SELECT)
- Web Demonstration(Demonstrated via a Flask app)

## Tech Stack

**Client:** Python3,Flask,Html,Git

## Run Locally

Clone the project

```bash
  git clone https://github.com/Nyam-bura/Dev-challenge-26-.git
```

Go to the project directory

```bash
  cd mini_dbms
  #Create a virtual environment
  python3 -m venv env
  #Activate the environment
  source env/bin/activate
```

Install dependencies

```bash
  pip install Flask
```

Start the server

```bash
  python3 app.py
```

```bash
  #Go to browser
  http://127.0.0.1:5000
```

```bash
  #Run the REPL
  python3 repl.py
```
