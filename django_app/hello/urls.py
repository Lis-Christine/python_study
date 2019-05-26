from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
#    path('form', views.form, name='form'),
#    path('<int:id>/<nickname>/', views.index, name="index"),
#    path('pentain_<int:id>_07040010_<nickname>/', views.index, name="index"),
]