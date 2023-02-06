from __main__ import app, request, cursor, conn, redirect, url_for

@app.route('/delete/categorie/', methods=['GET', 'POST'])
def submitDeleteCategorie():
    ID_text = request.form['ID']
    cursor.execute(f"DELETE FROM categorie WHERE IDcategorie = {int(ID_text)}")
    conn.commit()
    return redirect(url_for('index'))