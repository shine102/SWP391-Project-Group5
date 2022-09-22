import controllers.user
from decorators.authentication import login_required
from flask import Blueprint, jsonify, request, render_template, session


user_router = Blueprint('user_router', __name__)

@user_router.route("/home", methods=["POST", "GET"])
def home():
    return controllers.user.home()

@user_router.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        return controllers.user.register(username, password, email)
    return render_template("register.html")

@user_router.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        return controllers.user.login()
    return render_template("login.html")


@user_router.route("/logout", methods=["GET"])
# @login_required
def logout():
    return controllers.user.logout()

@user_router.route("/forgot_password", methods=["POST", "GET"])
def forgot_password():
    if(request.method == "POST"):
        return controllers.user.forgot_password(request.form.get("email"))
    else:
        return render_template("forgot_password.html")

@user_router.route("/register_seller", methods=["POST", "GET"])
def register_seller():
    if(request.method == "POST"):
        return controllers.user.register_seller(request)
    else:
        return render_template("register_seller.html")





