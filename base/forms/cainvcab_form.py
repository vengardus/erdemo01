'''
created by edgard.ramos (ismytv@gmail.com)
generated by alice.bash.v.2203a
jue 11 ago 2022 17:15:50 -05
'''
from django import forms
from django.utils.translation import gettext_lazy as _
#from django.core.exceptions import ValidationError
from base.models import CaInvCab, Empleado

 
class CaInvCabForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.set_data()

    def set_data(self):
        self.fields['empleado'].queryset = Empleado.objects.filter(license_id=self.request.user.license_id).order_by('s_nombre_completo')
        self.fields['s_descripcion'].widget.attrs['autofocus'] = True

    class Meta:
        model = CaInvCab
        fields = ['empleado', 's_descripcion', 's_fecha_inicio', 'estado_inventario']

        error_messages = {
            's_descripcion': {
                'unique': _("Ya existe rubro con esa descripción."),
            },
        }

    def clean(self):
        return super().clean()
    
    def clean_desc(self):
        data = self.cleaned_data['s_descripcion'].strip().upper()
        try:
            reg = CaInvCab.objects.get(desc=data)
            if not self.instance.id or self.instance.id != reg.id:
                raise forms.ValidationError('Ya existe otro registro con esa descripción')
        except CaInvCab.DoesNotExist:
            pass

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data