from django.urls import path

from . import views

app_name='anagram'
urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate, name='generate'),
    path('<int:word_id>/list/', views.list, name='list'),
]
