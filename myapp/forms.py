from django import forms

from .models import Store
from .models import Menu

class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('store_name', 'store_type', 'store_hours', 'store_address', 'store_phone',)

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('menu_type',)