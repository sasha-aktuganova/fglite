from django.shortcuts import render
from .models import Store
from .models import Menu
from .models import Menu_item

def store_list(request):
	stores = Store.objects.all().order_by('store_name')
	return render(request, 'stores/store_list.html', {'stores': stores})
