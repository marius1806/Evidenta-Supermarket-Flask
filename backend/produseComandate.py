from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/produse/produseComandate")
def produseComandate():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT P.Denumire, (SELECT SUM(NrBucati) FROM comandaprodus CP WHERE CP.IDprodus = P.IDprodus) as NrBucatiComandate
    FROM produse P
    ORDER BY NrBucatiComandate DESC LIMIT 3
    """)
    value = cursor.fetchall()
    return render_template("produseComandate.html", rows = value, name = "Cele mai comandate produse", length = len(value))