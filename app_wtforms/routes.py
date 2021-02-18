"""Rotas da aplicação"""

# Carrega o app criado em app.py
from flask import current_app as app

from flask import url_for, render_template, redirect
from .forms import ContactForm, SignupForm

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        'contact.html',
        form=form
    )

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        'signup.html',
        form=form
    )

@app.route("/success", methods=["GET", "POST"])
def success():
    return render_template(
        "success.html"
    )