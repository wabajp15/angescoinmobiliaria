from django.urls import path

#All views of the Property application are imported
from  . import views

urlpatterns = [
    path('list/', views.PropertyList.as_view(), name='list'),
    path('detail/<int:pk>/', views.PropertyDetail.as_view(), name='detail'),
    path('search/', views.searchProperty, name='search'),
    path('login/', views.index, name='login'),
    path('create/', views.PropertyCreate.as_view(), name='create'),
    #api services web
    path('api/', views.PropertyAPI.as_view(), name='api'),
    path('api/<int:pk>', views.PropertyAPI.as_view(), name='api'),

    #path('hello/', hello.as_view(), name='hello'),

]
