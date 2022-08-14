from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..business.bcainvcab import BCaInvCab
from base.business.bproducto import BProducto
from .serializer import ProductoSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/productos',
        'GET /api/productos/:id',
        
    ]
    return Response(routes)

@api_view(['GET'])
def get_productos(request):
    oBProducto = BProducto()
    productos = oBProducto.get_all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_producto(request, id=None):
    if request.method == 'GET':
        oBProducto = BProducto()
        producto = oBProducto.get(id)
        serializer = ProductoSerializer(producto, many=False)
        data_response = {
            'status' : status.HTTP_200_OK if producto is not None else status.HTTP_204_NO_CONTENT,
            'data' : serializer.data if producto is not None else {}
        }
        return Response(data_response)
    
    elif request.method == 'POST':
        print('POST', request.data)
        return Response({})


@api_view(['POST'])
def add_item(request):
    print('POST', request.data)
    try:
        data = request.data
        ca_inv_cab_id = data['ca_inv_cab_id']
        id_conteo = data['id_conteo']
        producto_codigo = data['producto_codigo']
        s_ubicacion = data['s_ubicacion']
        cantidad = data['cantidad']

        if len(s_ubicacion) == 0:
            s_ubicacion = 'UNICA'

        oBCaInvCab = BCaInvCab()
        if not oBCaInvCab.add_item(
            ca_inv_cab_id, 
            producto_codigo, 
            s_ubicacion, 
            cantidad, 
            id_conteo):
            status_id = status.HTTP_404_NOT_FOUND
            message = oBCaInvCab.message 
        else:
            status_id = status.HTTP_200_OK
            message = 'OK'

        data_response = {
            'status' : status_id,
            'data' : {
                'data' : data
            },
            'message': message
        }
    except Exception as e:
        data_response = {
            'status' : status.HTTP_400_BAD_REQUEST ,
            'data' : {},
            'message': f'Ocurrió un error except. {e}' 
        }

    return Response(data_response)