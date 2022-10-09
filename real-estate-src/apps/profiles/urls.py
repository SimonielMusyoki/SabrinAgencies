from django.urls import path
from .views import (
    AgentListAPIViews,
    TopAgentsListAPIView,
    GetProfileAPIView,
    UpdateProfileAPIView,
)

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/", UpdateProfileAPIView.as_view(), name="updated_profile"
    ),
    path("agents/all/", AgentListAPIViews.as_view(), name="all_agents"),
    path("top-agents/all/", TopAgentsListAPIView.as_view(), name="all_top_agents"),
]
