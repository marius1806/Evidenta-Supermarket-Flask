from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/comenzi/comenziPretPesteMedie")
def comenziPretPesteMedie():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT Cod, Pret
    FROM comenzi
    WHERE Pret > (SELECT AVG(Pret) FROM comenzi)
    """)
    value = cursor.fetchall()
    return render_template("comenziPretPesteMedie.html", rows = value, name = "Comenzile cu pretul total mai mare decat media preturilor tuturor comenzilor", length = len(value))