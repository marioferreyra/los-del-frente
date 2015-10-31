from django.conf.urls import url
from User.views import Register2
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^register/', Register2.as_view(), name='registro'),
    url(r'^reg_ok/', TemplateView.as_view(template_name='User/reg_ok.html')),
]