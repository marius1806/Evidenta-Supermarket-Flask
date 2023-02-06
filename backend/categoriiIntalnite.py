from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/categorii/topCategoriiIntalnite")
def topCategoriiIntalnite():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT C.Denumire, (SELECT COUNT(P.IDcategorie) FROM produse P WHERE P.IDcategorie = C.IDcategorie) as NrProduseDinCategorie FROM categorie C 
    ORDER BY NrProduseDinCategorie DESC LIMIT 3;
    """)
    value = cursor.fetchall()
    return render_template("categoriiIntalnite.html", rows = value, name = "Top 3 cele mai intalnite categorii", length = len(value))