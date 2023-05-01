from django.urls import path

from app.views import StudentCreateView, StudentDeleteView, StudentListView, StudentUpdateView


urlpatterns = [
    path("", StudentListView.as_view(), name = "home"),
    path("record/add/", StudentCreateView.as_view(), name = "record_new"),
    path("record/<int:pk>/delete/", StudentDeleteView.as_view(), name = "record_delete"),
    path("record/<int:pk>/edit/", StudentUpdateView.as_view(), name = "record_update"),
]