from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/comenzi")
def comenzi():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT C.Cod as 'Cod', C.DataCerere as 'Data cererii', C.DataPrimire as 'Data primirii', C.Pret as 'Pret', F.Nume as 'Nume furnizor', F.Prenume as 'Prenume furnizor' 
    FROM comenzi C INNER JOIN furnizori F ON C.IDfurnizor = F.IDfurnizor
    """)
    value = cursor.fetchall()
    return render_template("comenzi.html", rows = value, name = "Comenzi", length = len(value))