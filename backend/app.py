import os, mysql.connector
from flask import Flask, render_template, request, session, redirect, url_for

conn = mysql.connector.connect(host = "localhost", port = "3306", user = "Marius", password = "VEuLDrKHXLwvNl1R", database = "supermarket")
cursor = conn.cursor()

template_dir = os.path.abspath('../templates')

app = Flask(__name__, template_folder = template_dir)
app.config['SECRET_KEY'] = "secret"

import login, categorii, produse, index, logout, insert, update, insertCategorie, submitInsertCategorie, insertProdus, submitInsertProdus, insertComanda, submitInsertComanda
import updateCategorie, submitUpdateCategorie, delete, deleteCategorie, submitDeleteCategorie, deleteProdus, submitDeleteProdus
import comenzi, produseComandate, furnizorPrincipal, categoriiIntalnite, furnizor, updateProduse, submitUpdateProduse
import produseIeftine, comenziScumpe, produseVandute, furnizoriZerocomenzi, categoriiFurnizate, comenziPretMedie

if __name__ == "__main__":
    app.run(host = "127.0.0.9", port = 8080, debug = True)