from django.shortcuts import render, get_object_or_404
from .models import Store
from .models import Menu
from .models import Menu_item

def store_list(request):
	stores = Store.objects.all().order_by('store_name')
	return render(request, 'shared/store_list.html', {'stores': stores})

def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'shared/store_detail.html', {'store': store})
