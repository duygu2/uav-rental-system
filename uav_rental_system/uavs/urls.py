from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home),
    path('uavs/',views.uav_list),
    path('uavs/add/',views.uav_create, name='uav-add'),
    path('uavs/<int:id>/', views.uav_list_by_id, name='uav-list-by-id'),
    path('uavs/<int:id>/update/', views.uav_update, name='uav-update'),
    path('uavs/<int:id>/delete/', views.uav_delete, name='uav-delete'),
    path('brands/', views.brand_list, name='brand-list'), 
    path('brands/add/', views.brand_add, name='brand-add'),  
    path('brands/<int:id>/update/', views.brand_update, name='brand-update'),  
    path('brands/<int:id>/delete/', views.brand_delete, name='brand-delete'),
    path('categories/', views.category_list, name='category-list'),
    path('categories/add/', views.category_add, name='category-add'),
    path('categories/<int:id>/update/', views.category_update, name='category-update'),
    path('categories/<int:id>/delete/', views.category_delete, name='category-delete'),
]
