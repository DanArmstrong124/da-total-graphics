from django.conf.urls import url
from .views import contact, about, reset

urlpatterns = [
    url(r'^contact$', contact, name="contact"),
    url(r'^about$', about, name="about"),
    url(r'^reset$', reset, name="reset"),
]