from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/categorii/topCategoriiFurnizate")
def topCategoriiFurnizate():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT C.Denumire, SUM(CP.NrBucati) AS NrBucatiComandate 
    FROM comandaprodus CP 
    INNER JOIN produse P ON P.IDprodus = CP.IDprodus
    INNER JOIN categorie C ON C.IDcategorie = P.IDcategorie 
    GROUP BY P.IDcategorie 
    ORDER BY NrBucatiComandate DESC LIMIT 3
    """)
    value = cursor.fetchall()
    return render_template("categoriiFurnizate.html", rows = value, name = "Top 3 cele mai furnizate categorii", length = len(value))