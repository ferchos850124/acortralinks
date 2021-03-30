import mariadb


config = {
    'host' : 'localhost',
    'port' : 3309,
    'user' : 'root',
    'password' : 'Maleja21*',
    'database' : 'flask_mvc',
}

DB = mariadb.connect(**config)
DB.autocommit = True