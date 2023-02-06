from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/produse/produseIeftine")
def produseIeftine():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT p.Denumire, p.cantitate, p.PretBucata, c.Denumire 
    FROM produse p 
    INNER JOIN categorie c ON p.IDcategorie = c.IDcategorie 
    ORDER BY p.PretBucata LIMIT 3

    """)
    value = cursor.fetchall()
    return render_template("produseIeftine.html", rows = value, name = "Cele mai ieftine produse", length = len(value))