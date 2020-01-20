from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='index'),
path('/add',views.addition,name='addition'),
path('/addlogic',views.addlogic,name='addlogic'),
path('/fact',views.fact,name='fact'),
path('/factlogic',views.factlogic,name='factlogic')

] 