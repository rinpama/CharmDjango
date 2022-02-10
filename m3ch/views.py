from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import Blogform


# Create your views here.
@login_required
def top(request):
    params = {
        'title': 'これは、M3ch　です。'
    }
    return render(request, 'm3ch/top.html', params)


def index(request):
    blogs = Blog.objects.order_by('id')
    form = Blogform()
    context = {
        'blogs': blogs,
        'form': form,
    }
    return render(request, 'm3ch/index.html', context)


def detail(request, blog_id):
    blog_text = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog_text': blog_text
    }
    return render(request, 'm3ch/detail.html', context)


def add_form(request):
    if request.method == 'POST':
        form = Blogform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('m3ch:index')
    else:
        form = Blogform()
    context = {
        'form': form,
    }
    return render(request, 'm3ch/form.html', context)
