import sqlite3

def createDatabase():
    conn = sqlite3.connect('flask_rest.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE student (name varchar);''')
    c.execute('INSERT INTO student VALUES("shivam")')
    c.execute('INSERT INTO student VALUES("anshul")')
    c.execute('INSERT INTO student VALUES("abhi")')
    c.execute('INSERT INTO student VALUES("ravi")')

    conn.commit()
    conn.close()

def executeQuery(query):
    conn = sqlite3.connect('flask_rest.db')
    cursor = conn.execute(query)
    conn.commit()
    conn.close()
