
from django.urls import path
from emadapp.views import HomeView, blog

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("blog/<int:id>/", blog, name='blog')
]
