from django.urls import path
from .views import TaxisAPIView
from api import views
urlpatterns = [
    path('', TaxisAPIView.as_view()),
    path('<api>/AddEmployee', views.AddEmployee, name="add_employee"),
    path('<api>/<employee_name>/edit', views.edit_employee, name='edit_employee'),
    path('<api>/<employee_name>/delete', views.delete_employee, name='delete_employee'),
]