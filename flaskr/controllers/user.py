import random
from models.user import UserRole, User
from models.model import db
from flask import Flask,redirect,url_for,json,render_template,request,session,flash, Blueprint
from flask_mail import Message
from controllers.mail_service import mail

user_controller = Blueprint('user_controller', __name__)

def home():
    # session['user'] = 'test'    #//TEST
    # session.pop('user',None)    //TEST
    if "user" in session:
        user = session['user']
        return render_template("home.html", stringName = user, isLogin = True)
    else:
        return render_template("home.html", stringName = "you are not login", isLogin = False)
        
        
def login():

    user_name = request.form["user"]
    pass_word = request.form["pass"]

    query = User.query.filter(User.username == user_name , User.password == pass_word).first()
    if query:
        session['user'] = query.username
        return redirect(url_for("home"))
    flash("Your account doesn't exist","info")
    return render_template("login.html")


def logout():
    session.pop('user',None)
    return redirect(url_for('user_router.home'))

def forgot_password(email):
    # kiem tra email
    user = db.session.execute(db.select(User).where(User.email == email)).first()
    if user != None:
            # gen new password
            new_password = gen_new_password()
            # update password
            user[0].password = new_password
            # luu password moi vao database
            db.session.commit()
            #send email
            msg = Message('Your new password is: ' + new_password, sender = 'sweethomehola@outlook.com', recipients = [email])
            mail.send(msg)

            #thong bao toi front end
            flash("New password has been sent to your email.","info")
            return render_template("login.html")
    else:
        flash("Wrong email!","info")
        return render_template("forgot_password.html")


def register_seller():
    # nhan du lieu tu form
    # kiem tra du lieu
    # add thong bao cho admin
    # khi admin approve thi gui email cho seller
    pass
def gen_new_password():

    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    passwd = ''
    for i in range(0,8,2):
        passwd += random.choice(number)
        passwd += random.choice(alpha)
    return passwd