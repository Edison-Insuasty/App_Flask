from flask import render_template,abort
import mysql.connector

def connectionBD():
    try:
        mydb = mysql.connector.connect(
            host ="localhost",
            user ="root",
            password ="",
            db = "bd_parrilla"
            )
    except Exception:
        abort(500)
    return mydb