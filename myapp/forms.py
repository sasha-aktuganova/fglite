from django import forms

from .models import Store

class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('store_name', 'store_type', 'store_hours', 'store_address', 'store_phone',)