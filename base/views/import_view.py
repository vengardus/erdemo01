from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from base.libs.template import Template
from base import config as PARAMS
from erdemo01.settings import BASE_DIR

@login_required(login_url='login')
def import_data(request):
    oTemplate = Template(None)
    oTemplate.template_title = f'{PARAMS.AppName} - Import'
    oTemplate.template_container = PARAMS.TemplateContainerMain
    oTemplate.template = PARAMS.Template.import_form
    oTemplate.set_context()

    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            print('myfile', myfile)
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('uploadfile', uploaded_file_url)
            print(excel_file) 
            print('base_die:', BASE_DIR)
            print('excelfile:', excel_file)
            print('root:', BASE_DIR+excel_file)
            
            #empexceldata = pd.read_csv(BASE_DIR+excel_file,encoding='utf-8')

            empexceldata = pd.read_excel(open(BASE_DIR+excel_file, 
                                    'rb'),
                                    sheet_name='producto',
                                    dtype={},
                                    na_values='')

            print(type(empexceldata))
            #dbframe = empexceldata
            #for dbframe in dbframe.itertuples():
                 
            #    print(dbframe)
 
            return render(request, oTemplate.template, context=oTemplate.context)
            
    except Exception as identifier:            
        print(identifier)
     

    return render(request, oTemplate.template, context=oTemplate.context)

