# ФАЙЛ: app/views.py
from flask import render_template
# ВИПРАВТЕ ЦЕЙ РЯДОК:
from . import app

@app.route('/')
def resume():
    return render_template('resume.html', title='Резюме')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакти')