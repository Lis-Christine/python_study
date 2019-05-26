from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('search', views.search, name='search'),
    path('board_main/<int:num>', views.board_main, name='board_main'),
    path('create', views.create, name='create'),
    path('update/<int:num>', views.update, name='update'),
    path('delete/<int:num>', views.delete, name='delete'),
]
