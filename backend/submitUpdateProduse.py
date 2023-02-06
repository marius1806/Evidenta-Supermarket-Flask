from __main__ import app, request, cursor, conn, redirect, url_for
import time

@app.route('/update/produse/', methods=['GET', 'POST'])
def submitUpdateProduse():
    inregistrareModificata = request.form.get('InregistrareModificata')
    camp = request.form.get('Produse')
    valoare = request.form.get('ValoareNoua')
    if camp == "IDprodus":
        try:
            valoare = int(valoare)
            sql1 = "UPDATE produse SET IDprodus = (%s) " % (valoare)
            sql2 = "WHERE IDprodus = (%s)" % (int(inregistrareModificata))
            sql = sql1 + sql2
            cursor.execute(sql)
            conn.commit()
        except:
            time.sleep(1)
    elif camp == "IDcategorie":
        try:
            valoare = int(valoare)
            sql1 = "UPDATE produse SET IDcategorie = (%s) " % (valoare)
            sql2 = "WHERE IDprodus = (%s)" % (int(inregistrareModificata))
            sql = sql1 + sql2
            cursor.execute(sql)
            conn.commit()
        except:
            time.sleep(1)
    elif camp == "Denumire":
        sql1 = "UPDATE produse SET Denumire = ('%s') " % (valoare)
        sql2 = "WHERE IDprodus = (%s)" % (int(inregistrareModificata))
        sql = sql1 + sql2
        cursor.execute(sql)
        conn.commit()
    elif camp == "Cantitate":
        try:
            valoare = int(valoare)
            sql1 = "UPDATE produse SET Cantitate = (%s) " % (valoare)
            sql2 = "WHERE IDprodus = (%s)" % (int(inregistrareModificata))
            sql = sql1 + sql2
            cursor.execute(sql)
            conn.commit()
        except:
            time.sleep(1)
    elif camp == "PretBucata":
        try:
            valoare = float(valoare)
            sql1 = "UPDATE produse SET PretBucata = (%s) " % (valoare)
            sql2 = "WHERE IDprodus = (%s)" % (int(inregistrareModificata))
            sql = sql1 + sql2
            cursor.execute(sql)
            conn.commit()
        except:
            time.sleep(1)
    return redirect(url_for('index'))