from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/comenzi/comenziScumpe")
def comenziScumpe():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT co.Cod, co.DataCerere, co.DataPrimire, co.Pret, f.Nume, f.Prenume 
    FROM comenzi co 
    INNER JOIN furnizori f on co.IDfurnizor = f.IDfurnizor ORDER BY co.Pret DESC LIMIT 3
    """)
    value = cursor.fetchall()
    return render_template("comenziScumpe.html", rows = value, name = "Cele mai scumpe comenzi", length = len(value))