from django.shortcuts import render, get_object_or_404, redirect
from .models import Store
from .models import Menu
from .models import Menu_item
from .forms import StoreForm

def store_list(request):
	stores = Store.objects.all().order_by('store_name')
	return render(request, 'shared/store_list.html', {'stores': stores})

def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'shared/store_detail.html', {'store': store})

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
    return render(request, 'shared/store_edit.html', {'form': form})

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
    return render(request, 'shared/store_edit.html', {'form': form})

def menu_new(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.user_id = request.user
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'menus/menu_edit.html', {'form': form})



