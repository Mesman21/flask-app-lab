from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import ContactForm
import logging

main_bp = Blueprint('main', __name__)

logging.basicConfig(filename='contact.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@main_bp.route('/')
def resume():
    return render_template("resume.html")

@main_bp.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = ContactForm()

    if form.validate_on_submit():
        logging.info(f"Contact form submitted by Name: {form.name.data}, Email: {form.email.data}")
        flash(f"Повідомлення від {form.name.data} ({form.email.data}) успішно надіслано!", 'success')
        return redirect(url_for('main.contacts'))

    return render_template('contacts.html', form=form)