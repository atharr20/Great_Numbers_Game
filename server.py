from flask import Flask, render_template, request, redirect, session # added request and redirect
import random

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe' 
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'num' not in session:
        session['num']=random.randint(1,100)

    return render_template('index.html')


            
@app.route('/guess', methods=['POST'])
def guess():
    session['guess']= int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
