from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add),
    path('', views.home),
    path('update/<int:tid>',views.update),
    path('delete/<int:tid>',views.delete),
    path('htol/', views.htol),
    path('ltoh/', views.ltoh),
    path('AtoZ/', views.AtoZ),
    path('ZtoA/', views.ZtoA),
    path("AatoZz/",views.AatoZz),
    path("ZztoAa/",views.ZztoAa),
    path('lowtohigh/',views.lowtohigh),
    path('hightolow/',views.hightolow),
    path('CAtoZ/',views.CAtoZ),
    path('CZtoA/',views.CZtoA),
    path('catfilter/<str:cat>',views.catfilter),
    path('run/',views.run),
    path('register/',views.register),
    path("errorshow/",views.errorshow)
]