from django.urls import path, include
from . import views
from .views import UserRegistrationView

urlpatterns = [
    path('rejestracja/', UserRegistrationView.as_view(), name='user-registration'),
    path('producenci/', views.producent_list),
    path('producenci/<int:pk>/', views.producent_detail),
    path('producenci/update/<int:pk>/', views.producent_update_delete),
    path('producenci/delete/<int:pk>/', views.producent_update_delete),
    path('gatunki/', views.gatunek_list),
    path('gatunki/<int:pk>/', views.gatunek_detail),
    path('gatunki/update/<int:pk>/', views.gatunek_update_delete),
    path('gatunki/delete/<int:pk>/', views.gatunek_update_delete),
    path('wytwornie/', views.wytwornia_list),
    path('wytwornie/<int:pk>/', views.wytwornia_detail),
    path('wytwornie/update/<int:pk>/', views.wytwornia_update_delete),
    path('wytwornie/delete/<int:pk>/', views.wytwornia_update_delete),
    path('albumy/', views.album_list),
    path('albumy/<int:pk>/', views.album_detail),
    path('albumy/update/<int:pk>/', views.album_update_delete),
    path('albumy/delete/<int:pk>/', views.album_update_delete),
    path('festiwale/', views.festiwal_list),
    path('festiwale/<int:pk>/', views.festiwal_detail),
    path('festiwale/update/<int:pk>/', views.festiwal_update_delete),
    path('festiwale/delete/<int:pk>/', views.festiwal_update_delete),
    path('producenci/<int:author_id>/albumy/', views.albumy_po_autorze),
    path('gatunki/<int:genre_id>/albumy/', views.albumy_po_gatunku),
]