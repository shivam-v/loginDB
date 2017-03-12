from flask import Flask , jsonify , request
from sqlite import *

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hi'

@app.route('/names', methods= ['GET'])
def printAll():
    conn = sqlite3.connect('flask_rest.db')
    query = 'select * from student'
    cursor = conn.execute(query)
    conn.commit()

    name = []
    for temp in cursor :
        struct = {'name' : ''.join(temp)}
        name.append(struct)

    conn.close()
    return jsonify(name)


@app.route('/names', methods = ['POST'])
def addOne():
    #body must contain no spaces
    newName = request.data[9:-2]
    executeQuery("INSERT INTO student VALUES('" + newName + "')")
    return printAll()

@app.route('/names/<string:oldName>', methods = ['PUT'])
def editOne(oldName):
    changeName = request.data[9:-2]
    executeQuery("UPDATE student set name='" + changeName + "' WHERE name='" + oldName + "'")
    return printAll()

@app.route('/names/<string:deleteName>', methods = ['DELETE'])
def deleteOne(deleteName):
    executeQuery("DELETE FROM student WHERE name='" + deleteName + "'")
    return printAll()


if __name__ == "__main__" :
    # createDatabase()
    app.run(debug=True)