from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.PropertiesListAPIView.as_view(), name="all-properties"),
    path(
        "agents/", views.AgentsPropertyListAPIViews.as_view(), name="agent-properties"
    ),
    path("create/", views.create_property_api_view, name="create-property"),
    path(
        "details/<slug:slug>/",
        views.PropertyDetailView.as_view(),
        name="property-details",
    ),
    path("update/<slug:slug>/", views.update_property_api_view, name="property-update"),
    path("delete/<slug:slug>/", views.delete_property_api_view, name="delete-property"),
    path("search/", views.PropertySearchAPIView.as_view(), name="property-search"),
]
