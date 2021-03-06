from django.conf.urls import url
from User.views import Register, ProfileEdit, ProfileDetail, LinkList
from User.views import InviteList
# from User.views import AcceptInvitation
from .views import PeopleList, OthersProfile, SendFriendRequest, sugComplete
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^register', Register.as_view(), name='registro'),
    url(r'^reg_ok', TemplateView.as_view(template_name='User/reg_ok.html')),
    url(r'^accounts/profile/$', ProfileDetail.as_view(), name='profile'),
    url(r'^accounts/profile/edit/$', ProfileEdit.as_view(), name='edit'),
    url(r'^edit_ok/', TemplateView.as_view(template_name='User/edit_ok.html')),
    url(r'^fr_req_fail/',
        TemplateView.as_view(template_name='User/fr_req_fail.html')),
    url(r'^$', ProfileDetail.as_view(), name='home'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', OthersProfile.as_view(),
        name='oprofile'),
    url(r'^accounts/(?P<pk>[0-9]+)/sug/$', sugComplete, name='sug'),
    url(r'^accounts/links', LinkList.as_view(), name='vinculos'),
    url(r'^accounts/invitations', InviteList.as_view(), name='invitations'),
    url(r'^accounts/people', PeopleList.as_view(), name='people'),
    url(r'^accounts/friend_request/(?P<pk>[0-9]+)/$',
        SendFriendRequest.as_view(), name='friendrequest')
]
