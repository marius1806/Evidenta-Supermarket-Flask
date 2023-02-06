from __main__ import app, request, cursor, conn, redirect, url_for

@app.route('/insert/produs/', methods=['GET', 'POST'])
def submitInsertProdus():
    IDprodus_text = request.form['IDprodus']
    Denumire_text = request.form['Denumire']
    IDcategorie_text = request.form['IDcategorie']
    Cantitate_text = request.form['Cantitate']
    PretBucata_text = request.form['PretBucata']
    cursor.execute("INSERT INTO produse VALUES (%s, %s, %s, %s, %s)",  (int(IDprodus_text), Denumire_text, int(IDcategorie_text), int(Cantitate_text), float(PretBucata_text)))
    conn.commit()
    return redirect(url_for('index'))