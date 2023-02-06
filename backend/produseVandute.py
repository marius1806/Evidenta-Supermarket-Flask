from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/produse/produseVandute")
def produseVandute():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT P.Denumire as Produs, C.Denumire as Categorie, P.PretBucata as PretBucata, SUM(CP.NrBucati) - P.Cantitate as Nrvandute
    FROM produse P
    INNER JOIN categorie C ON P.IDcategorie = C.IDcategorie
    INNER JOIN comandaprodus CP ON CP.IDprodus = P.IDprodus
    GROUP BY P.IDprodus
    ORDER BY NrVandute DESC LIMIT 3
    """)
    value = cursor.fetchall()
    return render_template("produseVandute.html", rows = value, name = "Cele mai vandute produse", length = len(value))