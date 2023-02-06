from __main__ import app, request, cursor, conn, redirect, url_for
from datetime import datetime

@app.route('/insert/comanda/', methods=['GET', 'POST'])
def submitInsertComanda():
    IDcomanda_text = request.form['IDcomanda']
    Cod_text = request.form['Cod']
    DataCerere_text = request.form['DataCerere']
    DataPrimire_text = request.form['DataPrimire']
    Pret_text = request.form['Pret']
    IDfurnizor_text = request.form['IDfurnizor']
    cursor.execute("INSERT INTO comenzi VALUES (%s, %s, %s, %s, %s, %s)",  (int(IDcomanda_text), Cod_text, datetime.strptime(DataCerere_text, '%m-%d-%Y'), datetime.strptime(DataPrimire_text, '%m-%d-%Y'), float(Pret_text), int(IDfurnizor_text)))
    conn.commit()
    return redirect(url_for('index'))