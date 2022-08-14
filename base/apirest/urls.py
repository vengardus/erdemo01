from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('productos/', views.get_productos),
    path('producto/', views.get_producto),
    path('producto/<str:id>', views.get_producto),
    path('additem/', views.add_item),
]
