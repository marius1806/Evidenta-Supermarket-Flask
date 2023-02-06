from __main__ import app, request, cursor, conn, redirect, url_for
import time

@app.route('/update/categorie/', methods=['GET', 'POST'])
def submitUpdateCategorie():
    inregistrareModificata = request.form.get('InregistrareModificata')
    camp = request.form.get('Categorie')
    valoare = request.form.get('ValoareNoua')
    if camp == "IDcategorie":
        try:
            valoare = int(valoare)
            sql1 = "UPDATE categorie SET IDcategorie = (%s) " % (valoare)
            sql2 = "WHERE IDcategorie = (%s)" % (int(inregistrareModificata))
            sql = sql1 + sql2
            cursor.execute(sql)
            conn.commit()
        except:
            time.sleep(1)
    else:
        sql1 = "UPDATE categorie SET Denumire = ('%s') " % (valoare)
        sql2 = "WHERE IDcategorie = (%s)" % (int(inregistrareModificata))
        sql = sql1 + sql2
        cursor.execute(sql)
        conn.commit()
    return redirect(url_for('index'))