from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('productos/', views.get_productos),
    path('producto/', views.get_producto),
    path('producto/<str:id>', views.get_producto),
    path('additem/', views.add_item),
    path('getinvcab/', views.get_invcab),
    path('getinvdet/<str:id_invcab>/<str:producto_codigo>', views.get_invdet),
    path('getlistinvdet/<str:id_invcab>', views.get_list_invdet),
    path('getlistinvdetu/<int:id_invcab>/<str:s_ubicacion>/<int:id_conteo>', views.get_list_invdetu),
    path('getlistinvdetugroup/<str:id_invcab>', views.get_list_invdetu_group),
]
