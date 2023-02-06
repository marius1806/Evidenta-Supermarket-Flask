from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/categorii")
def categorii():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("SELECT * FROM categorie")
    value = cursor.fetchall()
    return render_template("categorii.html", data = value, name = "Categorii")