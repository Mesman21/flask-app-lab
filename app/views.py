from flask import render_template, redirect, url_for, flash
from app import app
from .forms import ContactForm
import logging

logging.basicConfig(filename='contact.log', level=logging.INFO, format='%(asctime)s - %(message)s')


@app.route('/')
def resume():
    return render_template("resume.html")


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = ContactForm()

    if form.validate_on_submit():
        logging.info(f"Contact form submitted by Name: {form.name.data}, Email: {form.email.data}")
        flash(f"Повідомлення від {form.name.data} ({form.email.data}) успішно надіслано!", 'success')
        return redirect(url_for('contacts'))

    return render_template('contacts.html', form=form)