import flask
import os
from smtplib import SMTP
from flask import Flask, session, Blueprint, render_template, request, Response, redirect, url_for, jsonify
from app.api.models import datasets, UserModel, _runSql


module = Blueprint('dataset_upload', __name__)


@module.route('/new_dataset')
def new_dataset():

    if session["loggedIn"] == True:
        user = session["user"]
        return render_template('/api/new_dataset.html', user=user)
    else:
        return redirect('/login_error')