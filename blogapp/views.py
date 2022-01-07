from django.shortcuts import render, redirect
from .models import Blogs
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import ModelForm


def fun(request):
    blg = Blogs.objects.all()
    paginator = Paginator(blg, 2)
    bn = Blogs.objects.filter(popular=True)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'b': blg, 'pg': pro, 'bn': bn})


def post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        bg = Blogs(title=title, desc=desc, image=image)
        bg.save()
        return redirect('/')
    return render(request, 'post.html')


def update(request, id):
    ob = Blogs.objects.get(id=id)
    form = ModelForm(request.POST or None, request.FILES, instance=ob)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form})


def single(request, id):
    obj = Blogs.objects.get(id=id)
    return render(request, 'single_post.html', {'i': obj})


def delete(request, id):
    if request.method == "POST":
        ob = Blogs.objects.get(id=id)
        ob.delete()
        return redirect('/')
    return render(request, 'delete.html')

# Create your views here.
