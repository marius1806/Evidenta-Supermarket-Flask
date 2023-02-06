from __main__ import app, request, cursor, conn, redirect, url_for

@app.route('/insert/categorie/', methods=['GET', 'POST'])
def submitInsertCategorie():
    ID_text = request.form['ID']
    Denumire_text = request.form['Denumire']
    cursor.execute("INSERT INTO categorie VALUES (%s, %s)",  (int(ID_text), Denumire_text))
    conn.commit()
    return redirect(url_for('index'))