from __main__ import app, render_template, session, redirect, url_for

@app.route("/delete/produs")
def deleteProdus():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    return render_template("deleteProdus.html", name = "deleteProdus")