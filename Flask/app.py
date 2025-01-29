from flask import Flask
#### WSGI application 
app=Flask(__name__)

## decorator take 2 parameters which take url
@app.route('/')

def welcome():
    return "Hello there , I am Sumit Sangwan"

@app.route("/members")
def members():
    return "Welcome to the Program."


if __name__=='__main__':
    app.run(debug=True)
