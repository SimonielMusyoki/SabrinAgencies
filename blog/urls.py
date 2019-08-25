from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('blog/', BlogPostListView.as_view(), name='blog'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('projects/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', Contact.as_view(), name='blog-contact'),
    path('messages/', MessagesListView.as_view(), name='messages'),

    path('properties/', PropertiesListView.as_view(), name='properties'),
    path('property/<int:pk>/', PropertiesDetailView.as_view(), name='property-detail'),
    path('property/<int:pk>/update/', PropertiesUpdateView.as_view(), name='property-update'),
    path('property/<int:pk>/delete/', PropertiesDeleteView.as_view(), name='property-delete'),
    path('property/new/', PropertiesCreateView.as_view(), name='property-create'),

    path('units/', UnitsListView.as_view(), name='units'),
    path('unit/<int:pk>/', UnitsDetailView.as_view(), name='unit-detail'),
    path('unit/<int:pk>/update/', UnitsUpdateView.as_view(), name='unit-update'),
    path('unit/<int:pk>/delete/', UnitsDeleteView.as_view(), name='unit-delete'),
    path('unit/new/', UnitsCreateView.as_view(), name='unit-create'),

    path('tenants/', TenantListView.as_view(), name='tenants'),
    path('tenant/<int:pk>/', TenantDetailView.as_view(), name='tenant-detail'),
    path('tenant/<int:pk>/update/', TenantUpdateView.as_view(), name='tenant-update'),
    path('tenant/<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant-delete'),
    path('tenant/new/', TenantCreateView.as_view(), name='tenant-create'),

    path('lease/', LeaseListView.as_view(), name='lease'),
    path('lease/<int:pk>/', LeaseDetailView.as_view(), name='lease-detail'),
    path('lease/<int:pk>/update/', LeaseUpdateView.as_view(), name='lease-update'),
    path('lease/<int:pk>/delete/', LeaseDeleteView.as_view(), name='lease-delete'),
    path('lease/new/', LeaseCreateView.as_view(), name='lease-create'),

    path('payments/', PaymentListView.as_view(), name='payments'),
    path('payment/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('payment/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payment/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),
    path('payment/new/', PaymentCreateView.as_view(), name='payment-create'),

    path('vendors/', VendorListView.as_view(), name='vendors'),
    path('vendor/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendor/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor-update'),
    path('vendor/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor-delete'),
    path('vendor/new/', VendorCreateView.as_view(), name='vendor-create'),

    path('expenses/', ExpenseListView.as_view(), name='expenses'),
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expense/<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('expense/new/', ExpenseCreateView.as_view(), name='expense-create'),

]
