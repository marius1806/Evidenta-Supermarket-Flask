from __main__ import app, render_template, session, redirect, url_for

@app.route("/insert/categorie")
def insertCategorie():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    return render_template("insertCategorie.html", name = "insertCategorie")