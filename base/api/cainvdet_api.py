'''
created by edgard.ramos (ismytv@gmail.com)
generated by alice.bash.v.2203a
jue 11 ago 2022 23:23:49 -05
'''
from datetime import datetime
import json
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages

from base.libs.controller import Controller
from base.business.bcainvdet import BCaInvDet
from base.business.bcainvdetu import BCaInvDetU


def cainvdet_controller(request):
    oController = ControllerCustom(json.load(request), request)
    context = oController.do_action()
    context = JsonResponse(context)
    return context

class ControllerCustom(Controller):

    def __init__(self, data, request):
        # print(data)
        super().__init__(data)
        self.request = request
        self.set_actions()
        self.url_action_new = 'cainvdet_form'

    def set_actions(self):
        super().set_actions()
        
        # FUNCIONALIDAD PERSONALIZADA
        # ---------------------------
        self.actions['action_list_cainvdetu'] = self.action_list_cainvdetu

    def action_save(self):
        return super().action_save()

    def action_edit(self):
        id = self.data['id']
        self.context['action_new'] = reverse(self.url_action_new, args=['edit', id])
        return self.context
        
    def action_delete(self):
        oBModel = BCaInvDet()
        if not oBModel.delete(self.data['id']):
            self.context['status'] = oBModel.error_code
            messages.error(self.request, oBModel.message)
        else:
            oBModel.get_all(self.request.user.license_id)
            self.context['aDataTable'] = oBModel.get_aTO_toArray()
            self.context['action_new'] = reverse(self.url_action_new, args=['new', 0])
            messages.success(self.request, oBModel.message)
            
        self.context['aMessage'].append(oBModel.message)
        return self.context

    def action_refresh(self):
        time1 = datetime.now()

        show_grid_header = self.data['show_grid_header']
        oBModel = BCaInvDet()
        oBModel.get_all_invcab(self.data['ca_inv_cab_id'], self.request.user.license_id)

        time2 = datetime.now()

        self.context['aDataTable'] = oBModel.get_aTO_toArray()

        time3 = datetime.now()

        self.context['action_new'] = reverse(self.url_action_new, args=['new', 0]); #'cainvdet_form'
        self.context['aHeader'] = self.set_grid_columns() if show_grid_header else []
        
        time4 = datetime.now()
        print('1) ', time1)
        print('2) ', time2)
        print('3) ', time3)
        print('4) ', time4)
        print('Back ', time4-time1)

        return self.context
   
    
    # FUNCIONALIDAD PERSONALIZADA
    # ---------------------------
    def set_grid_columns(self):
        '''
        Retorna lista de tuplas, puede tener una o mas tuplas (de momento se consideran hasta 2)
        La primera tupla tiene las etiquetas para pantallas grandes (width>=768)
        La segunda tupla tiene las etiquetas para pantallas pequeñas
        '''
        return [ 
                ('Codigo', 'Descripcion', 'Unid/Categ', 'Stock', 'Conteo1', 'Conteo2', 'Acción'),
        ]

    def action_list_cainvdetu(self):
        cainvdet_id = self.data['cainvdet_id']
        oBCaInvDet = BCaInvDet()
        oTOCaInvDet = oBCaInvDet.get(cainvdet_id)
        oBCaInvDetU = BCaInvDetU()
        oBCaInvDetU.get_all_parent(cainvdet_id)

        self.context['aCaInvDetU'] = oBCaInvDetU.get_aTO_toArray()
        self.context['cainvdet'] = {
            's_codigo': oTOCaInvDet.producto.s_codigo if oTOCaInvDet!=None else '',
            's_descripcion': oTOCaInvDet.producto.s_descripcion if oTOCaInvDet!=None else '',
        }
  
        return self.context
    