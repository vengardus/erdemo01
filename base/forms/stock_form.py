'''
created by edgard.ramos (ismytv@gmail.com)
generated by alice.bash.v.2203a
sáb 20 ago 2022 10:33:09 -05
'''
from django import forms
from django.utils.translation import gettext_lazy as _
#from django.core.exceptions import ValidationError
from base.models import Stock

 
class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_data()

    def set_data(self):
        self.fields['stock'].widget.attrs['autofocus'] = True

    class Meta:
        model = Stock
        fields = ['stock']

        error_messages = {
            'stock': {
                'unique': _("Ya existe rubro con esa descripción."),
            },
        }

    def clean(self):
        return super().clean()
    
    def clean_desc(self):
        data = self.cleaned_data['desc'].strip().upper()
        try:
            reg = Stock.objects.get(desc=data)
            if not self.instance.id or self.instance.id != reg.id:
                raise forms.ValidationError('Ya existe otro registro con esa descripción')
        except Stock.DoesNotExist:
            pass

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data