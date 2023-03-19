from flask import render_template,abort
import mysql.connector

def connectionBD():
    try:
        mydb = mysql.connector.connect(
            host ="edisoninsuasty.mysql.pythonanywhere-services.com",
            user ="edisoninsuasty",
            password ="matricula1234",
            db = "edisoninsuasty$default"
            )
    except Exception:
        abort(500)
    return mydb