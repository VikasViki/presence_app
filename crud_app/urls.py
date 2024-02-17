
from .views import health_check, CrudView
from django.urls import path, include

urlpatterns = [
    path("health_check/", health_check, name="health_check"),
    path("add_record/", CrudView.as_view({"post": "add_record"})),
    path("read_record/", CrudView.as_view({"get": "read_record"}))

]