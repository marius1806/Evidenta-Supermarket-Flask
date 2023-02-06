from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/produse")
def produse():
    cursor.execute("SELECT P.Denumire, C.Denumire, P.Cantitate, P.PretBucata FROM produse P INNER JOIN categorie C ON P.IDcategorie = C.IDcategorie")
    value = cursor.fetchall();
    pt = []
    for row in value:
        pt.append(round(row[2] * row[3], 2))
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    return render_template("produse.html", rows = value, name = "Produse", pretTotal = pt, length = len(value))