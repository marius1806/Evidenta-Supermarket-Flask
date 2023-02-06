from __main__ import app, request, cursor, conn, redirect, url_for

@app.route('/delete/produs/', methods=['GET', 'POST'])
def submitDeleteProdus():
    ID_text = request.form['ID']
    cursor.execute(f"DELETE FROM comandaprodus WHERE IDprodus = {int(ID_text)}")
    cursor.execute(f"DELETE FROM produse WHERE IDprodus = {int(ID_text)}")
    conn.commit()
    return redirect(url_for('index'))