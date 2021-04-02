from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from .token import account_activation_token
from django.core.mail import EmailMultiAlternatives
from decouple import config


def send_conf_mail(request, user):
    context = {
        "small_text_detail": "Thank you for "
                             "creating an account. "
                             "Please verify your email "
                             "address to set up your account.",
        "email": user.email,
        "domain": get_current_site(request).domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": account_activation_token.make_token(user)
    }
    msg = render_to_string('account/confirmation.html', context)
    text = strip_tags(msg)
    email = EmailMultiAlternatives(
        subject='Please confirm your account',
        body=msg,
        from_email=config('EMAIL_HOST_USER'),
        to=[user.email,]
    )
    email.content_subtype = 'html'
    email.send(fail_silently=True)
