"""Classe com as configurações dos formulários"""
from flask.app import Flask
from flask_wtf import FlaskForm
from flask_wtf.recaptcha.fields import RecaptchaField
from wtforms import StringField, TextField, SubmitField
from wtforms.fields.core import DateField, SelectField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL

class ContactForm(FlaskForm):
    """Formulário de Contato"""

    # field = FieldType(
    #     'LABEL',
    #     validators=[ExampleValidator(message="ERROR MESSAGE")],
    # )

    name = StringField(
        'Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            Email(message=('Insira um email válido')),
            DataRequired()
        ]
    )
    body = TextField(
        'Message',
        [
            DataRequired(),
            Length(min=10,
            message=('Mensagem muito curta'))
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Enviar')


class SignupForm(FlaskForm):
    """Formulário de Cadastro"""

    email = StringField(
        'Email',
        [
            Email(message=('Insira um email válido')),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Senha',
        [DataRequired(message=('Por favor informe uma senha'))]
    )
    confirmPassword = PasswordField(
        'Confirmar senha',
        [EqualTo(password, message=('Senhas não batem'))]
    )
    title = SelectField(
        'Título',
        [DataRequired()],
        choices=[
            ('developer', 'Desenvolvedor'),
            ('designer', 'Designer Gráfico'),
            ('whatever', 'Analista de sistema')
        ]
    )
    website = StringField(
        'Website',
        validators=[URL()]
    )
    birthday = DateField('Seu aniversário')
    recaptcha = RecaptchaField()
    submit = SubmitField('Cadastrar')