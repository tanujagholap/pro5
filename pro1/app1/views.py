from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_url')
def create_view(request):
    template_name = 'app1/create.html'
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieve_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def retrieve_view(request):
    template_name = 'app1/retrieve.html'
    obj = Create.objects.all()
    context = {'form': obj}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def update_view(request, pk):
    template_name = 'app1/create.html'
    obj = Create.objects.get(id=pk)
    form = CreateForm(instance=obj)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('retrieve_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def delete_view(request, pk):
    obj = Create.objects.get(id=pk)
    template_name = 'app1/confirm.html'
    if request.method == 'POST':
        obj.delete()
    return render(request, template_name)

