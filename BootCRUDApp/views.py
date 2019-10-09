from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm, UserForm
from .models import ItemModel


# Create your views here.
def index(request):
    return render(request, 'BootCRUDApp/index.html')


# View to create a new item
def list(request):
    item_list = ItemModel.objects.all()
    # print(len(item_list)) # debug
    context = {
        'item_list': item_list
    }
    return render(request, 'BootCRUDApp/list.html', context)


def delete(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    item.delete()
    return redirect('list')
    # return render(request, 'BootCRUDApp/delete.html', {})


# Create a new item
def create(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=True)
            return redirect('list')
    return render(request, 'BootCRUDApp/create.html', {'form': form})


def edit(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'BootCRUDApp/edit.html', {'form': form})


# This view will render a web page displaying a single item for sale. The entry cannot be deleted
def display(request, pk):
    item = ItemModel.objects.get(pk=pk)
    injection_queue = {
        'item': item,
        'title': item.itm_name,
        'subtitle': 'Displayi This is g an Item'

    }
    return render(request, 'BootCRUDApp/display.html', injection_queue)

# Login a user
def logIn(request):
    if request.method == "POST":
        # try to login user
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('list')



    context = {
        'form' : UserForm(),
    }
    return render(request,'BootCRUDApp/login.html',context)

def logOot(request):

    return None

def newUser(request):

    return None