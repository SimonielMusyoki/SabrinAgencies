from django.urls import path
from properties.views import (
    PropertiesCreateView,
    PropertiesDeleteView,
    PropertiesListView,
    PropertiesUpdateView,
    PropertiesDetailView,
    propertiesCreateView
)

urlpatterns = [
    path('',PropertiesListView.as_view(), name='properties'),
    path('new/',PropertiesCreateView.as_view(), name='property_add'),
    path('<int:pk>/update/',PropertiesUpdateView.as_view(), name='property_update'),
    path('<int:pk>/',PropertiesDetailView.as_view(), name='property_detail'),
    path('<int:pk>/delete/',PropertiesDeleteView.as_view(), name='property_delete'),

]