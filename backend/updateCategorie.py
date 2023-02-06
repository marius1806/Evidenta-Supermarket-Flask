from __main__ import app, render_template, session, redirect, url_for

@app.route("/update/categorie")
def updateCategorie():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    return render_template("updateCategorie.html")