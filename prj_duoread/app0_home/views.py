"""this is a home view"""
from django.shortcuts import render


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


def mailing(request):
    """requesting mailing service"""
    if request.method == "POST":
        email = request.POST['mailing']
    return render(request, 'mailing_registered.html', {"result": email})
