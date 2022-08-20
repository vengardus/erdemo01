'''
created by edgard.ramos (ismytv@gmail.com)
generated by alice.bash.v.2203a
sáb 20 ago 2022 10:33:09 -05
'''
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from base.libs.template import Template
from base.libs.listview import ListView
from base import config as PARAMS
from base.business.bstock import BStock
from base.models import Stock
from base.forms.stock_form import StockForm


@login_required(login_url='login')
def stock_list(request):
    oListView = ListView(Stock)
    oListView.template_container = PARAMS.TemplateContainerMain
    oListView.template = PARAMS.Template.stock_list
    oListView.actions['action_new'] = reverse('stock_form', args=['new', 0])
    oListView.set_context()
    return render(request, oListView.template, context=oListView.context)


@login_required(login_url='login')
def stock_form(request, mode, id):
    url_return = 'stock_list'
    oBModel = BStock()

    if mode != 'new':
        oTO = oBModel.get(id)
        if oTO == None:
            messages.error(request, f'Error. No se encontraron datos para el id = {id}' )
            return redirect(url_return)
    
    if request.method == 'POST':
        if mode == 'new':
            form = StockForm(request.POST)
        else:
            form = StockForm(request.POST, instance=oTO)
        if not form.is_valid():
            messages.error(request, 'Error en ingreso de datos')
        elif not oBModel.save(request, mode, id, form.cleaned_data):
            messages.error(request, oBModel.message)
        else:
            messages.success(request, oBModel.message)
            return redirect(url_return)
    else:
        if mode == 'new':
            form = StockForm()
        else:
            form = StockForm(instance=oTO)

    oTemplate = Template(Stock)
    oTemplate.template_container = PARAMS.TemplateContainerMain
    oTemplate.template = PARAMS.Template.stock_form
    oTemplate.set_template_title(mode)
    oTemplate.actions['action_cancel'] = reverse(url_return)
    oTemplate.data['mode'] = mode
    oTemplate.data['id'] = id
    oTemplate.form = form
    oTemplate.set_context()

    return render(request, oTemplate.template, context=oTemplate.context)
