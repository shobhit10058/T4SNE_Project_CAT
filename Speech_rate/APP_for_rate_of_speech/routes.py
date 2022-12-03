from flask import render_template, url_for, flash, redirect,request,abort,jsonify,session
import requests
import json
import imaplib
from APP_for_rate_of_speech import application,db,bcrypt,mail #using bcrypt to has the passwords in user database

from flask_login import login_user,current_user,logout_user,login_required
from sqlalchemy.orm.exc import NoResultFound

from datetime import datetime, timedelta
from random import sample
import urllib.request
import urllib.parse
from flask_mail import Message

#--------------------------------------------------------------------------------------------
import time
import string
import pyaudio
import speech_recognition as sr
from plyer import notification 
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from nltk.tokenize import sent_tokenize, word_tokenize 
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from Codes.APP_for_rate_of_speech.rate_of_speech import getRoS, getTranscript
#--------------------------------------------------------------------------------------------

import os
from os import path
import moviepy.editor as mp

#--------------------------------------------------------------------------------------------
@application.route("/speechAsisstance",methods=['GET', 'POST'])
def speechAsisstance():
    return render_template("speechAsisstance.html") 


@application.route("/speechAsisstance_RoS")
def speechAsisstance_RoS():
    print("Starting Recording\n")
    average_RoS, words_in_speech, text = getRoS()
    string3 = str(words_in_speech) + " words"
    string4 = str(average_RoS) + " words/min" 
    message1 = "<h3>" +str(average_RoS) + " words/min</h3>" 
    message2 = "<h5 class=\"mb-6\">You said        : <span class=\"text-muted h5 font-weight-normal\">" + text + "<br></span></h5>"
    message3 = "<h5 class=\"mb-6\">Words in Speech : <span class=\"text-muted h5 font-weight-normal\">" + string3 + "<br></></h5>"
    message4 = "<h5 class=\"mb-6\">Rate of Speech  : <span class=\"text-muted h5 font-weight-normal\">" + string4 + "<br></></h5>"
    
    ret_val = jsonify(message1 =message1, message2= message2 ,message3=message3,message4=message4)
    return ret_val