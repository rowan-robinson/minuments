from app import db, loginManager
from flask_login import UserMixin

# manages logging in
@loginManager.user_loader
def loadUser(userid):
    return User.query.get(int(userid))

# a model for the items that the website is selling
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30), index=True)
    country = db.Column(db.String(30), index=True)
    country_alttext = db.Column(db.Text, index=True)
    monument = db.Column(db.String(30), index=True)
    monument_alttext = db.Column(db.Text, index=True)
    # tags are stored in the many-to-many relation called ItemTags
    description = db.Column(db.Text, index=True)
    # favourited'ness is stored in the many-to-many relation called UserFavourites

# a model for the tags that items hold
class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True)

# a many-to-many relation that holds the tags of each item
# each tag can be tagged onto many items, and each item can hold many tags
class ItemTags(db.Model):
    itemid = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    tagid = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

# a model to hold user data
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    # personal details
    firstname    = db.Column(db.String(30), index=True)
    lastname     = db.Column(db.String(30), index=True)
    username     = db.Column(db.String(30), index=True, unique=True)
    password     = db.Column(db.String(30), index=True)

    # financial details
    cardholder   = db.Column(db.String(100), index=True)
    cardnumber   = db.Column(db.String(16), index=True)
    cardexpiry   = db.Column(db.String(5), index=True)
    cardcvv      = db.Column(db.String(3), index=True)
    addressline1 = db.Column(db.String(100), index=True)
    addressline2 = db.Column(db.String(100), index=True)
    addressline3 = db.Column(db.String(100), index=True)
    zippostcode  = db.Column(db.String(20), index=True)

# a many-to-many relation that holds users' favourited items
# each item can be favourited by many users, and each user can have many favourite items
class UserFavourites(db.Model):
    itemid = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)