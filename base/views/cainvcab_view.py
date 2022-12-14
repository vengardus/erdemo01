'''
created by edgard.ramos (ismytv@gmail.com)
generated by alice.bash.v.2203a
jue 11 ago 2022 17:15:49 -05
'''
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.generic.base import TemplateView

from base.libs.template import Template
from base.libs.listview import ListView
from base import config as PARAMS
from base.business.bcainvcab import BCaInvCab
from base.models import CaInvCab
from base.forms.cainvcab_form import CaInvCabForm



class CaInvCabView(TemplateView):
    template_name = PARAMS.Template.cainvcab_list

    def get_context_data(self, **kwargs):
        oListView = ListView(CaInvCab)
        
        #context = super().get_context_data(**kwargs)
        #oListView.context.update(context)
        
        oListView.template_container = PARAMS.TemplateContainerMain
        oListView.template = PARAMS.Template.cainvcab_list
        oListView.actions['action_new'] = reverse('cainvcab_form', args=['new', 0])

        print(oListView.context)

        oListView.set_context()

        return oListView.context
    

@login_required(login_url='login')
def cainvcab_list(request):
    oListView = ListView(CaInvCab)
    oListView.template_container = PARAMS.TemplateContainerMain
    oListView.template = PARAMS.Template.cainvcab_list
    #oListView.listview_title ='Inventarios'
    #oListView.listview_btn_new_text = 'Add Inventario'
    oListView.actions['action_new'] = reverse('cainvcab_form', args=['new', 0])
    oListView.set_context()
    return render(request, oListView.template, context=oListView.context)


@login_required(login_url='login')
def cainvcab_form(request, mode, id):
    url_return = 'cainvcab_list'
    url_detail = 'cainvdet_list'
    oBModel = BCaInvCab()

    if mode != 'new':
        oTO = oBModel.get(id)
        if oTO == None:
            messages.error(request, f'Error. No se encontraron datos para el id = {id}' )
            return redirect(url_return)
    
    if request.method == 'POST':
        if mode == 'new':
            form = CaInvCabForm(request, request.POST)
        else:
            form = CaInvCabForm(request, request.POST, instance=oTO)
        if not form.is_valid():
            messages.error(request, 'Error en ingreso de datos')
        elif not oBModel.save(request, mode, id, form.cleaned_data):
            messages.error(request, oBModel.message)
        else:
            messages.success(request, oBModel.message)
            return redirect(url_return)
    else:
        if mode == 'new':
            form = CaInvCabForm(request)
        else:
            form = CaInvCabForm(request, instance=oTO)

    oTemplate = Template(CaInvCab)
    oTemplate.template_container = PARAMS.TemplateContainerMain
    oTemplate.template = PARAMS.Template.cainvcab_form
    oTemplate.set_template_title(mode)
    oTemplate.actions['action_cancel'] = reverse(url_return)
    oTemplate.actions['action_detail'] = reverse(url_detail, args=[id])

    oTemplate.data['mode'] = mode
    oTemplate.data['id'] = id
    oTemplate.form = form
    oTemplate.set_context()

    return render(request, oTemplate.template, context=oTemplate.context)
