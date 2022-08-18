'''
created by edgard.ramos (ismytv@gmail.com)
generated by alice.bash.v.2203a
jue 11 ago 2022 23:23:49 -05
'''
from logging import NullHandler
from base.libs.table import Table
from base import config as PARAMS
from base.models import CaInvDet
#from base.business.bcainvcab import BCaInvCab
from base.business.bproducto import BProducto


class BCaInvDet(Table):
    aMessage = []           # lista de mensajes

    def __init__(self):
        self.TO = CaInvDet
        self.message_tablename = self.TO._meta.verbose_name
        self.aMessage = []

    def get_aTO_toArray(self):
        array = list()
        for oTO in self.aTO:
            array.append(self.get_oTO_toDict(oTO))
        return array
    
    def get_oTO_toDict(self, oTO:CaInvDet):
        # acá se genera diccionario con los atributos a retornar

        
        #print('COUNT', oTO.cainvdets.count)}

        #x = oTO.cainvdets.all().count()
        #for i in list(x):
        #    print('X', i.id, i.ca_inv_det_id, i.ns_conteo)
        #print('COUNT', x)

        return {
            'id':oTO.id,
            's_codigo':oTO.s_codigo,
            's_cod_barra': oTO.s_cod_barra,
            's_descripcion': oTO.s_descripcion,
            'unidad_medida_s_codigo': oTO.unidad_medida.s_codigo,
            'unidad_medida_s_descripcion': oTO.unidad_medida.s_descripcion,
            'n_stk_act': oTO.n_stk_act,
            'ns_conteo1': oTO.ns_conteo1,
            'ns_conteo2': oTO.ns_conteo2,
            'count_cainvdetu': oTO.cainvdets.all().count(),
            's_categoria': oTO.s_categoria if oTO.s_categoria else ''
        }

    ''' ----------------------
        Métodos personalizados
    '''
    def _set_oTO(self, oTO:CaInvDet, data:list(), mode, request):
        '''
            Personalizar oTO
        '''
        oTO.ca_inv_cab = data['ca_inv_cab']
        oTO.producto = data['producto']
        oTO.s_codigo = data['s_codigo']
        oTO.s_cod_barra = data['s_cod_barra']
        oTO.s_descripcion = data['s_descripcion']
        oTO.unidad_medida = data['unidad_medida']
        oTO.n_stk_act = data['n_stk_act']
        oTO.s_ubicacion = data['s_ubicacion']
        oTO.ns_conteo1 = data['ns_conteo1']
        oTO.ns_conteo2 = data['ns_conteo2']
        oTO.s_categoria = data['s_categoria']

        if mode != 'new':
            oTO.user_edit_id = request.user.id
        else:
            oTO.user_created_id = request.user.id
            oTO.license_id = request.user.license_id
        return oTO
    
    def validate(self, data:list()):
        self.aMessage = []
        return True

    def save(self, request, mode, id, data:list()):
        ok = False
        if mode == 'new' :
            oTO = self.TO()
            oTO = self._set_oTO(oTO, data, mode, request)
            ok = self.insert(oTO)
        
        else: # edit
            oTO = self.get(id)
            if oTO == None:
                self.message = f'No se encontro registro con id={id}'
                self.error_code = PARAMS.ErrorCode.not_found
            else:
                oTO = self._set_oTO(oTO, data, mode, request,)
                ok = self.update(oTO)
            
        return ok
    
    def get_all(self, license_id:int=None):
        if license_id == None:
            # self.aTO = self.TO.objects.all().order_by('desc')
            self.aTO = self.TO.objects.all()
        else:
            self.aTO = self.TO.objects.all().filter(license_id=license_id)
        return self.aTO

    def get_all_invcab(self, ca_inv_cab, license_id:int=None):
        if license_id == None:
            # self.aTO = self.TO.objects.all().order_by('desc')
            self.aTO = self.TO.objects.all().filter(ca_inv_cab=ca_inv_cab)
        else:
            self.aTO = self.TO.objects.all().filter(license_id=license_id, ca_inv_cab=ca_inv_cab)
        return self.aTO
    
    def get_item(self, ca_inv_cab_id, producto_codigo):
        aTO = self.TO.objects.all().filter(
            ca_inv_cab=ca_inv_cab_id, s_codigo=producto_codigo)
        if aTO:
            return aTO[0]
        return None

    