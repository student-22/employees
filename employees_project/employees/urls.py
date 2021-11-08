from django.urls import path
from .views import index, EmployeeListView, EmployeeCreateView

urlpatterns = [
    # path("", index),
    path("list/", EmployeeListView.as_view()),
    path("create/", EmployeeCreateView.as_view()),
]