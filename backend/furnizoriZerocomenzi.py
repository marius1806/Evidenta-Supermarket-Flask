from __main__ import app, cursor, render_template, session, redirect, url_for

@app.route("/furnizori/furnizoriZeroComenzi")
def furnizoriZeroComenzi():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT Nume, Prenume, Telefon
    FROM furnizori 
    WHERE IDfurnizor NOT IN (SELECT IDfurnizor FROM comenzi);
    """)
    value = cursor.fetchall()
    return render_template("furnizoriZeroComenzi.html", rows = value, name = "Furnizorii cu 0 comenzi livrate", length = len(value))