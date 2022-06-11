from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from emadapp.models import Conatct, Blog
# Create your views here.


class HomeView(View):
    def get(self, request):
        blog = Blog.objects.all()
        return render(request, "home.html", {'blog': blog})

    def post(self, request):
        to_name = request.POST.get('name')
        email = request.POST.get('sender')
        message = request.POST.get('message')

        saveemail = Conatct(name=to_name, email=email, message=message)
        saveemail.save()
        messages.success(
            request, "Email Successfully Send! I Checked Your Email Soon")
        return render(request, "home.html")


def blog(request, id):
    blognews = Blog.objects.get(id=id)
    return render(request, 'blog.html', {'blognews': blognews})
