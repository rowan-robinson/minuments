import json

from flask import redirect, render_template, flash, url_for, request
from app import app, db, bcrypt, models
from app.forms import GetEditPersonalInfoForm, GetEditFinancialInfoForm, GetLoginForm, GetRegisterForm
from flask_login import current_user, login_required, login_user, logout_user


# ROOT (home page) ==============================================================================================

@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template("base.html")


# SHOP ==============================================================================================

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    # collect data from the database
    itemsObject = models.Items.query.all()
    itemtagsObject = models.ItemTags.query.all()
    userfavouritesObject = models.UserFavourites.query.all()

    # check if a user is logged in or not;
    # if they are, store the id
    if (current_user.is_authenticated):
        currentUserID = current_user.id
    else:
        # 0 can be used as no user will have that id
        currentUserID = 0

    items = []
    for x in itemsObject:
        completeTags = []
        itemFavourited = "unfilled" # (string chosen due to the filename of the star)

        for y in itemtagsObject:
            if y.itemid == x.id:
                tag = models.Tags.query.get(y.tagid)
                completeTags.append(tag.name)

        if userfavouritesObject:
        # ...iterate through all of them to look for a match
        # (more detailed comments can be found at the bottom of this file
        # in a more complex version of this setup)
            for z in userfavouritesObject:
                if (z.userid == currentUserID) and (z.itemid == x.id):
                    itemFavourited = "filled"
        
        #items.append([x.city, x.country, x.monument, x.image, completeTags, x.page, x.description, itemFavourited])
        items.append([x.id, x.city, x.country, x.country_alttext, x.monument, x.monument_alttext, completeTags, x.description, itemFavourited])

    return render_template("shop.html",
                           title = "SHOP",
                           header = "ALL ITEMS",
                           items = items)


# ITEM ===========================================================================================

@app.route('/item<id>', methods=['GET', 'POST'])
def item(id):
    # collect data from the database
    itemObject = models.Items.query.get(id)
    itemtagsObject = models.ItemTags.query.all()
    tagsObject = models.Tags.query.all()

    # one iteration (flag)
    completeTags = []
    for y in itemtagsObject:
        if y.itemid == itemObject.id:
            tag = models.Tags.query.get(y.tagid)
            completeTags.append(tag.name)

    # check to see if the item is favourited by the user
    itemFavourited = "unfilled"
    userfavouritesObject = models.UserFavourites.query.all()

    # ( same as above )
    if (current_user.is_authenticated):
        currentUserID = current_user.id
    else:
        currentUserID = 0

    if userfavouritesObject:
        for x in userfavouritesObject:
            if (x.userid == currentUserID) and (x.itemid == itemObject.id):
                itemFavourited = "filled"
    
    item = [itemObject.id,
            itemObject.city,
            itemObject.country,
            itemObject.country_alttext,
            itemObject.monument,
            itemObject.monument_alttext,
            completeTags,
            itemObject.description,
            itemFavourited]

    return render_template("item.html",
                           title = itemObject.monument.upper(),
                           header = "MINUMENT",
                           item = item)

@app.route('/ajax_favourite', methods=['GET', 'POST'])
def ajax_favourite():
    # receiving JSON data from the AJAX request
    data = json.loads(request.data)
    # storing the id as an integer
    itemID = int(data.get('itemid'))

    # get a list of all favourited items by all users
    userfavouritesObject = models.UserFavourites.query.all()

    # first check if a user is logged in or not.
    # if they aren't, they shouldn't be allowed to use this feature
    if not (current_user.is_authenticated):
        resultingAction = "needlogin"
        return json.dumps({'status': 'OK', 'response': resultingAction})

    # if there are any records...
    if userfavouritesObject:
        # ...iterate through all of them to look for a match
        # and start by assuming we haven't found it yet
        found = False

        for x in userfavouritesObject:
            # if the current item being viewed is found in the table
            # it means that it is currently favourited. since we got here
            # by pressing the button, we must now unfavourite this item
            # by removing this record from the table
            if (x.userid == current_user.id) and (x.itemid == itemID):
                db.session.delete(x)
                db.session.commit()
                found = True
                resultingAction = "unfavourited"
        
        # if we make it to this point and found == False, then it means
        # that a match wasn't found in the table, which means the item
        # hadn't been favourited. this means we clicked the button to
        # favourite it, and so it should be added to the table
        if found == False:
            newFav = models.UserFavourites(itemid=itemID, userid=current_user.id)
            db.session.add(newFav)
            db.session.commit()
            resultingAction = "favourited"
    # if there aren't any records...
    else:
        # ...the item couldn't have been favourited and should now be added
        newFav = models.UserFavourites(itemid=itemID, userid=current_user.id)
        db.session.add(newFav)
        db.session.commit()
        resultingAction = "favourited"

    # Return a request to the JavaScript
    return json.dumps({'status': 'OK', 'response': resultingAction})

@app.route('/ajax_buy', methods=['GET', 'POST'])
def ajax_buy():
    # receiving JSON data from the AJAX request
    #data = json.loads(request.data)
    # storing the id as an integer
    #itemID = int(data.get('itemid'))

    # simply check if a user is logged in or not.
    # if they aren't, they shouldn't be allowed to use this feature
    if not (current_user.is_authenticated):
        resultingAction = "needlogin"
        return json.dumps({'status': 'OK', 'response': resultingAction})
    else:
        resultingAction = "buy"
        return json.dumps({'status': 'OK', 'response': resultingAction})


# PROFILE and ACCOUNT SETTINGS ======================================================================================

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    # collect data from the database
    itemsObject = models.Items.query.all()
    itemtagsObject = models.ItemTags.query.all()
    userfavouritesObject = models.UserFavourites.query.all()

    items = []
    for x in itemsObject:
        completeTags = []
        itemFavourited = "unfilled"

        for y in itemtagsObject:
            if y.itemid == x.id:
                tag = models.Tags.query.get(y.tagid)
                completeTags.append(tag.name)

        if userfavouritesObject:
            for z in userfavouritesObject:
                if (z.userid == current_user.id) and (z.itemid == (x.id)):
                    itemFavourited = "filled"
        
        if itemFavourited == "filled":
            items.append([x.id, x.city, x.country, x.country_alttext, x.monument, x.monument_alttext, completeTags, x.description, itemFavourited])

    return render_template("profile.html",
                           title = "PROFILE",
                           header = "YOUR PROFILE",
                           items = items)

@app.route('/edit-personal-info', methods=['GET', 'POST'])
@login_required
def edit_personal_info():
    form = GetEditPersonalInfoForm()

    return render_template("edit.html",
                           title = "EDIT PERSONAL INFO",
                           header = "EDIT PERSONAL INFO",
                           form = form)

@app.route('/edit-personal-info/submit', methods=['GET', 'POST'])
@login_required
def edit_personal_info_submit():
    form = GetEditPersonalInfoForm()

    if form.validate_on_submit():
        # first check if there was even a change made
        if ((current_user.firstname == form.firstname.data)
        and (current_user.lastname == form.lastname.data)
        and (current_user.username == form.username.data)):    
            flash("No changes were made.", 'flashed-info')
            return redirect(url_for('profile'))
        
        # if not, reflect the new changes in the database
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.username = form.username.data
        db.session.commit()

        flash("Personal details have been updated!", 'flashed-success')
        return redirect(url_for('profile'))
    else:
        # display each validation error message
        for x in form.errors:
            for y in range(0, len(form.errors.get(x))):
                flash(form.errors.get(x)[y], 'flashed-error')
    
    return redirect(url_for('edit_personal_info'))

@app.route('/edit-financial-info', methods=['GET', 'POST'])
@login_required
def edit_financial_info():
    form = GetEditFinancialInfoForm()

    return render_template("edit.html",
                           title = "EDIT FINANCIAL INFO",
                           header = "EDIT FINANCIAL INFO",
                           form = form)

@app.route('/edit-financial-info/submit', methods=['GET', 'POST'])
@login_required
def edit_financial_info_submit():
    form = GetEditFinancialInfoForm()

    if form.validate_on_submit():
        # first check if there was even a change made
        if ((current_user.cardholder == form.cardholder.data)
        and (current_user.cardnumber == form.cardnumber.data)
        and (current_user.cardexpiry == form.cardexpiry.data)
        and (current_user.cardcvv == form.cardcvv.data)
        and (current_user.addressline1 == form.addressline1.data)
        and (current_user.addressline2 == form.addressline2.data)
        and (current_user.addressline3 == form.addressline3.data)
        and (current_user.zippostcode == form.zippostcode.data)):
            flash("No changes were made.", 'flashed-info')
            return redirect(url_for('profile'))
        
        # if not, reflect the new changes in the database
        current_user.cardholder  =form.cardholder.data
        current_user.cardnumber  =form.cardnumber.data
        current_user.cardexpiry  =form.cardexpiry.data
        current_user.cardcvv     =form.cardcvv.data
        current_user.addressline1=form.addressline1.data
        current_user.addressline2=form.addressline2.data
        current_user.addressline3=form.addressline3.data
        current_user.zippostcode =form.zippostcode.data
        db.session.commit()

        flash("Financial details have been updated!", 'flashed-success')
        return redirect(url_for('profile'))
    else:
        # display each validation error message
        for x in form.errors:
            for y in range(0, len(form.errors.get(x))):
                flash(form.errors.get(x)[y], 'flashed-error')
    
    return redirect(url_for('edit_financial_info'))


# LOGIN ==============================================================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if the user is already logged in,
    # immediately redirect them to the profile page
    # and let them know they are already logged in
    if (current_user.is_authenticated):
        flash("You are already logged in.", 'flashed-info')
        return redirect(url_for('profile'))

    form = GetLoginForm()

    return render_template("login.html",
                           title = "LOG IN",
                           header = "LOG IN",
                           form = form)

@app.route('/login/submit', methods=['GET', 'POST'])
def login_submit():
    form = GetLoginForm()

    if form.validate_on_submit():
        # get the first user in the database with the username that the user entered;
        # there should only be one (as usernames are unique), so .first() is applicable here
        userToLogIn = models.User.query.filter_by(username=form.username.data).first()

        # check if a user with that username exists
        # and check if the password that came with it is the correct one
        if (userToLogIn) and (bcrypt.check_password_hash(userToLogIn.password, form.password.data)):
            # log the user in
            login_user(userToLogIn, remember=True)
            # take them to the profile page
            # and let them know the login was a success
            flash(("Login successful! Welcome back, " + userToLogIn.username + "."), 'flashed-success')
            return redirect(url_for('profile'))
        else:
            flash("USERNAME or PASSWORD is incorrect, please try again.", 'flashed-error')
    else:
        # display each validation error message
        for x in form.errors:
            for y in range(0, len(form.errors.get(x))):
                flash(form.errors.get(x)[y], 'flashed-error')
    
    return redirect(url_for('login'))


# REGISTER ==============================================================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if the user is already logged in,
    # immediately redirect them to the profile page
    # and let them know they are already logged in
    if (current_user.is_authenticated):
        flash("You are already logged in.", 'flashed-info')
        return redirect(url_for('profile'))

    form = GetRegisterForm()

    return render_template("register.html",
                           title = "REGISTER",
                           header = "REGISTER",
                           form = form)

@app.route('/register/submit', methods=['GET', 'POST'])
def register_submit():
    form = GetRegisterForm()

    if form.validate_on_submit():
        hashedPassword = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        newUser = models.User(firstname   =form.firstname.data,
                              lastname    =form.lastname.data,
                              username    =form.username.data,
                              password    =hashedPassword,
                           
                              cardholder  =form.cardholder.data,
                              cardnumber  =form.cardnumber.data,
                              cardexpiry  =form.cardexpiry.data,
                              cardcvv     =form.cardcvv.data,
                              addressline1=form.addressline1.data,
                              addressline2=form.addressline2.data,
                              addressline3=form.addressline3.data,
                              zippostcode =form.zippostcode.data,)
        db.session.add(newUser)
        db.session.commit()

        flash("Registration succcess! You may now log in.", 'flashed-success')
        return redirect(url_for('login'))
    else:
        # display each validation error message
        for x in form.errors:
            for y in range(0, len(form.errors.get(x))):
                flash(form.errors.get(x)[y], 'flashed-error')
    
    return redirect(url_for('register'))


# LOG OUT =============================================================================================

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # simply log the user out
    logout_user()
    # and then redirect to the profile page
    flash("Logged out successfully.", 'flashed-success')
    return redirect(url_for('login'))