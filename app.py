from flask import Flask

app= Flask(__name__)

@app.get('/hello')
def get_hello():
    return 'hello World!'

app.run(debug=True)