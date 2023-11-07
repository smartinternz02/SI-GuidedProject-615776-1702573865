from flask import Flask, render_template, request
import pickle
import numpy as np
app=Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route("/", methods=['GET', 'POST'])
def startone():
    if request.method == 'POST':
        un = request.form['un']
        pw = request.form['pw']
        if un == 'admin' and pw == 'admin':
            return render_template('index.html')
    return render_template('login.html')

@app.route("/index.html")
def start():
    return render_template('index.html')
@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/check.html")
def check():
    return render_template('check.html')
@app.route('/predict',methods=['POST'])
def home():
    fn=request.form['fn']
    a=request.form['a']
    b=request.form['b']
    c=request.form['c']
    d=request.form['d']
    e=request.form['e']
    f=request.form['f']
    g=request.form['g']
    h=request.form['h']
    i=request.form['i']
    j=request.form['j']
    k=request.form['k']
    l=request.form['l']
    m=request.form['m']
    n=request.form['n']
    o=request.form['o']
    p=request.form['p']
    q=request.form['q']
    r=request.form['r']
    s=request.form['s']
    t=request.form['t']
    u=request.form['u']

    arr = [[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u]]
    pred=model.predict(arr)
    print(pred)
    
    if(r==0):
        gender="Female"
    else:
        gender="Male"
    

    if(pred[0]==0):
        return render_template('no.html',result='Not Having Diabetes  ',name=fn,gender=gender)
    if(pred[0]==1):
        return render_template('maybe.html',result='Pre-Diabetes  ',name=fn,gender=gender)
    else:
        return render_template('yes.html',result='Having Diabetes  ',name=fn,gender=gender)

    #return render_template('index.html', result=fn)
if __name__ == "__main__":
    app.run(debug=True)
