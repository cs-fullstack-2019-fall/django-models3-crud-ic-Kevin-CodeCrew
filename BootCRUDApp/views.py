from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import ItemForm
from .models import ItemModel

# Create your views here.
def index(request):
    return render(request, 'BootCRUDApp/index.html')


# View to create a new item
def list(request):
    item_list = ItemModel.objects.all()
    # print(len(item_list)) # debug
    return render(request, 'BootCRUDApp/list.html', {'item_list': item_list})


def delete(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    item.delete()
    return HttpResponseRedirect('/list/')
    # return render(request, 'BootCRUDApp/delete.html', {})


# Create a new item
def create(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/list/')
    return render(request, 'BootCRUDApp/create.html', {'form': form})


def edit(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/')
    return render(request, 'BootCRUDApp/edit.html', {'form': form})


def display(request, pk):
    item = ItemModel.objects.get(pk=pk)

    return render(request, 'BootCRUDApp/display.html', {'item': item})
