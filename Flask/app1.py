## Building Url Dynamically
## Flask Variable Rules And Url Building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Hello welcome to code"


@app.route('/success/<int:score>')
def success(score):
    return "The person has marks is"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed with"+str(score)


## Result checker
@app.route('/scorecard/<int:marks>')
def scorecard(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result="success"
    return redirect(url_for(result,score=marks))





if __name__=='__main__':
    app.run(debug=True)