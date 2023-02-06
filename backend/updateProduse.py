from __main__ import app, render_template, session, redirect, url_for

@app.route("/update/produse")
def updateProduse():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    return render_template("updateProduse.html")