from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/furnizori/furnizorPrincipal")
def furnizorPrincipal():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT F.Nume, F.Prenume,(SELECT COUNT(*) FROM comenzi C WHERE C.IDfurnizor = F.IDfurnizor) as NrAparitii
    FROM comenzi C
    JOIN furnizori F WHERE F.IDfurnizor = C.IDfurnizor
    ORDER BY NrAparitii DESC LIMIT 1
    """)
    value = cursor.fetchall()
    return render_template("furnizorPrincipal.html", rows = value, name = "Furnizorul principal", length = len(value))