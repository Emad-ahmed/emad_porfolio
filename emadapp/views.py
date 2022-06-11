from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        to_name = request.POST.get('name')
        email = request.POST.get('sender')
        message = request.POST.get('message')

        content = f"Hello \nYour Registration Has Been Successfull.\nPay 500 For The Form Fee and Use This  Code As A Refernce Number Thanks For Registration.Use This Link For Pay http://127.0.0.1:8000/paymentLeading University, Sylhet"
        send_mail("Successfully Registration",
                  content,
                  settings.EMAIL_HOST_USER,
                  ["amadahmed1234678@gmail.com"]
                  )
        return render(request, "home.html")
