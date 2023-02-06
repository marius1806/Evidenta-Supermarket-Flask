from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/furnizori")
def furnizori():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("SELECT * FROM furnizori")
    value = cursor.fetchall()
    return render_template("furnizori.html", data = value, name = "Furnizori")