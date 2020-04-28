import flask
import os
from smtplib import SMTP
from flask import Flask, session, Blueprint, render_template, request, Response, redirect, url_for, jsonify
from app.api.models import datasets, UserModel, _runSql


module = Blueprint('home', __name__)


@module.route('/home')
def home():

    if session["loggedIn"] == True:
        admin = session["admin"]
        user = session["user"]
        return render_template('/api/home.html', admin=admin, user=user)
    else:
        return redirect('/login_error')


