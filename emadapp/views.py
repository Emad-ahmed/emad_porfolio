from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from emadapp.models import Conatct
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        to_name = request.POST.get('name')
        email = request.POST.get('sender')
        message = request.POST.get('message')

        saveemail = Conatct(name=to_name, email=email, message=message)
        saveemail.save()

        return render(request, "home.html")
