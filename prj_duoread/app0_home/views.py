"""this is a home view"""
from django.shortcuts import render
from app0_home.models import Mailing
from django.views.generic.edit import CreateView

# Create your views here.


def home(request):
    """this is a home page"""
    res_data = {}
    try:
        user = request.user
        if user.username:
            return render(request, "member_home.html")
    except Exception:
        user = None
        error = Exception.__dict__
        res_data['error'] = error
    return render(request, "welcome.html", res_data)


def mailing_register(request):
    """requesting mailing service"""
    if request.method == "POST":
        email = request.POST['mailing']
        mailing = Mailing.objects.get_or_create(email=email)
    return render(request, 'mailing_registered.html', {"email": email})
