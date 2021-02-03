from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    url(r'^update/', views.update, name='update'),
    url(r'^results/', views.ResultsView.as_view(), name='results')
]
