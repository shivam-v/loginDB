from flask import Flask , jsonify , request
app = Flask(__name__)

names = [{'name':'shivam'},
        {'name':'anshul'},
        {'name':'abhi'}]

@app.route('/')
def hello():
    return 'hi'

@app.route('/names', methods= ['GET'])
def printAll():
    return jsonify(names)

@app.route('/names', methods = ['POST'])
def addOne():
    #body must contain no spaces
    language = { 'name' : request.data[9:-2]}
    names.append(language)
    return jsonify(names)

@app.route('/names/<string:oldName>', methods = ['PUT'])
def editOne(oldName):
    editName = [name for name in names if name['name']==oldName]
    editName[0]['name'] = request.data[9:-2]
    return jsonify(names)

@app.route('/names/<string:deleteName>', methods = ['DELETE'])
def deleteOne(deleteName):
    deleteRecord = [name for name in names if name['name']==deleteName]
    names.remove(deleteRecord[0])
    return jsonify(names)

if __name__ == "__main__" :
    app.run(debug=True)
