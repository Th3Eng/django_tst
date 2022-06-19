from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:month>', views.months_by_num),
    # name='months' to use in the reverse function in the views file
    #  to get the url path of the month challenge page automatically. eg:challenge/january
    path('<str:month>', views.months, name='challenges_path'),
]
