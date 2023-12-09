from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import Length, InputRequired
from flask_login import current_user
from app.models import User


# LOGIN ===================================

class GetLoginForm(FlaskForm):
    username = StringField("username",   [Length(min=1, max=30, message="USERNAME must be 1-30 characters."),
                                          InputRequired(message="USERNAME is required.")])
    password = PasswordField("password", [Length(min=1, max=30, message="PASSWORD must be 1-30 characters."),
                                          InputRequired(message="PASSWORD is required.")])


# REGISTER ===================================

class GetRegisterForm(FlaskForm):
    # custom validation
    def validateFreeUsername(form, field):
        if User.query.filter_by(username=field.data).first():
           raise ValidationError('That USERNAME is already taken, please choose another.')
    
    # personal info
    firstname    = StringField("firstname",    [Length(min=1, max=30, message="FIRST NAME must be 1-30 characters."),
                                                InputRequired(message="FIRST NAME is required.")])
    lastname     = StringField("lastname",     [Length(min=1, max=30, message="LAST NAME must be 1-30 characters."),
                                                InputRequired(message="LAST NAME is required.")])
    username     = StringField("username",     [Length(min=1, max=30, message="USERNAME must be 1-30 characters."),
                                                InputRequired(message="USERNAME is required."),
                                                validateFreeUsername])
    password     = PasswordField("password",   [Length(min=1, max=30, message="PASSWORD must be 1-30 characters."),
                                                InputRequired(message="PASSWORD is required.")])

    # financial info
    cardholder   = StringField("cardholder",   [Length(min=1, max=100, message="CARD HOLDER must be 1-100 characters."),
                                                InputRequired(message="CARD HOLDER is required.")])
    cardnumber   = StringField("cardnumber",   [Length(min=1, max=19, message="CARD NUMBER must be 1-19 characters."),
                                                InputRequired(message="CARD NUMBER is required.")]) # FLAG 16
    cardexpiry   = StringField("cardexpiry",   [Length(min=1, max=5, message="CARD EXPIRY must be 1-5 characters."),
                                                InputRequired(message="CARD EXPIRY is required.")])
    cardcvv      = StringField("cardcvv",      [Length(min=1, max=3, message="CARD CVV must be 1-3 characters."),
                                                InputRequired(message="CARD CVV is required.")])
    addressline1 = StringField("addressline1", [Length(min=1, max=100, message="ADDRESS LINE 1 must be 1-100 characters."),
                                                InputRequired(message="ADDRESS LINE 1 is required.")])
    addressline2 = StringField("addressline2", [Length(min=1, max=100, message="ADDRESS LINE 2 must be 1-100 characters."),
                                                InputRequired(message="ADDRESS LINE 2 is required.")])
    addressline3 = StringField("addressline3", [Length(min=1, max=100, message="ADDRESS LINE 3 must be 1-100 characters."),
                                                InputRequired(message="ADDRESS LINE 3 is required.")])
    zippostcode  = StringField("zippostcode",  [Length(min=1, max=20, message="ZIPCODE / POSTCODE must be 1-20 characters."),
                                                InputRequired(message="ZIPCODE / POSTCODE is required.")])

    # def validateFreeUsername(self, field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('BThis username is already taken, please choose another.')


# ACCOUNT UPDATING ====================================================

class GetEditPersonalInfoForm(FlaskForm):
    # personal info
    firstname    = StringField("firstname",    [Length(min=1, max=30, message="FIRST NAME must be 1-30 characters."),
                                                InputRequired(message="FIRST NAME is required.")])
    lastname     = StringField("lastname",     [Length(min=1, max=30, message="LAST NAME must be 1-30 characters."),
                                                InputRequired(message="LAST NAME is required.")])
    username     = StringField("username",     [Length(min=1, max=30, message="USERNAME must be 1-30 characters."),
                                                InputRequired(message="USERNAME is required.")])
        
class GetEditFinancialInfoForm(FlaskForm):
    # financial info
    cardholder   = StringField("cardholder",   [Length(min=1, max=100, message="CARD HOLDER must be 1-100 characters."),
                                                InputRequired(message="CARD HOLDER is required.")])
    cardnumber   = StringField("cardnumber",   [Length(min=1, max=19, message="CARD NUMBER must be 1-19 characters."),
                                                InputRequired(message="CARD NUMBER is required.")]) # FLAG 16
    cardexpiry   = StringField("cardexpiry",   [Length(min=1, max=5, message="CARD EXPIRY must be 1-5 characters."),
                                                InputRequired(message="CARD EXPIRY is required.")])
    cardcvv      = StringField("cardcvv",      [Length(min=1, max=3, message="CARD CVV must be 1-3 characters."),
                                                InputRequired(message="CARD CVV is required.")])
    addressline1 = StringField("addressline1", [Length(min=1, max=100, message="ADDRESS LINE 1 must be 1-100 characters."),
                                                InputRequired(message="ADDRESS LINE 1 is required.")])
    addressline2 = StringField("addressline2", [Length(min=1, max=100, message="ADDRESS LINE 2 must be 1-100 characters."),
                                                InputRequired(message="ADDRESS LINE 2 is required.")])
    addressline3 = StringField("addressline3", [Length(min=1, max=100, message="ADDRESS LINE 3 must be 1-100 characters."),
                                                InputRequired(message="ADDRESS LINE 3 is required.")])
    zippostcode  = StringField("zippostcode",  [Length(min=1, max=20, message="ZIPCODE / POSTCODE must be 1-20 characters."),
                                                InputRequired(message="ZIPCODE / POSTCODE is required.")])