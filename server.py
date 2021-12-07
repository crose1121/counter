from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'shhh this is a secret'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1 #Creating empty session dictionary, first key is 'counter' and value is 1
    else:
        session['counter'] +=1 

    return render_template('index.html', counter=session['counter'])

@app.route('/add')
def add2():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy')
def destroy_session():
    print(session)
    session.clear()
    print(session)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

# session['counter'] = request.form['counter']  #These are useful together but not always required together
