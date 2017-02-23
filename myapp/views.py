from django.shortcuts import render, get_object_or_404, redirect
from .models import Store
from .models import Menu
from .models import Menu_item
from .forms import StoreForm
from .forms import MenuForm

def store_list(request):
	stores = Store.objects.all().order_by('store_name')
	return render(request, 'stores/store_list.html', {'stores': stores})

def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'stores/store_detail.html', {'store': store})

def store_new(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.user_id = request.user
            store.save()
            return redirect('store_detail', pk=store.pk)
    else:
        form = StoreForm()
    return render(request, 'stores/store_edit.html', {'form': form})

def store_edit(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            store.user_id = request.user
            store.save()
            return redirect('store_detail', pk=store.pk)
    else:
        form = StoreForm(instance=store)
    return render(request, 'stores/store_edit.html', {'form': form})

def menu_new(request, pk):
    print(request)
    if request.method == "POST":
        form = MenuForm(request.POST, Store)
        if form.is_valid():
            store = get_object_or_404(Store, pk=pk)
            menu = form.save(commit=False)
            menu.store = store.id
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'menus/menu_edit.html', {'form': form})



