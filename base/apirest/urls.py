from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('productos/', views.get_productos),
    path('producto/', views.get_producto),
    path('producto/<str:id>', views.get_producto),
    path('additem/', views.add_item),
    path('getinvcab/', views.get_invcab),
    path('getinvdet/<str:id_invcab>/<str:producto_codigo>', views.get_invdet)
]
