import string
import random
from django.shortcuts import HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.core.signing import Signer
from django.contrib import messages
signer = Signer()
from core.settings import EMAIL_HOST_USER

def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    str = ''.join(random.choice(chars) for _ in range(size - 1))
    return str

def unsign_key(key):
    return signer.unsign(key)

def is_password_correct(password, request, msg, path ,kwargs={}):
    matchcheck= check_password(password,request.user.password)
    if not matchcheck:
        messages.error(request,msg)
        return HttpResponseRedirect(reverse(path,kwargs=kwargs))

def send_email_generic(content,receiver):
     msg = EmailMessage('Your Appname', content, to=[receiver,], from_email=EMAIL_HOST_USER)
     msg.content_subtype = 'html'
     msg.send()

