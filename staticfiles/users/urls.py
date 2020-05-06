from django.urls import path

#All views of the Property application are imported
from .views import signup, ActivateUser, templateEmailSent

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', ActivateUser, name='activate'),
    path('emailsent/<str:username>/', templateEmailSent, name='emailsent'),
]
