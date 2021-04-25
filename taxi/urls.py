from django.urls import path,include
from .views import TaxisListView

urlpatterns = [
    path('', TaxisListView.as_view(), name='home'),
    #path('User/','User'),
]
