from __main__ import app, render_template, request, session, redirect, url_for

def redirect_url(default = 'index'):
    return request.args.get('next') or request.referrer or url_for(default)

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if session.get('loggedin') == True:
        return redirect(redirect_url())
    session['loggedin'] = False
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        if username == "Marius" and password == "VEuLDrKHXLwvNl1R":
            session['loggedin'] = True
            session['username'] = username
            session['password'] = password
            return redirect(url_for('index'))
        else:
            message = 'Please enter correct username / password !'
    return render_template('login.html', message = message)