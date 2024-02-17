from django.urls import path, include

from .views import PresenceView


urlpatterns = [
    path("update_presence_state/", PresenceView.as_view({"post": "update_users_presence_state"}), name="update_users_presence_state"),
    path("get_all_present_users/", PresenceView.as_view({"get": "get_all_present_users"}), name="get_all_present_users")

]