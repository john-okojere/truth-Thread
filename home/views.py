from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.defaultfilters import urlize
from django_user_agents.utils import get_user_agent
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import forms, models

def homepage(request):
    return render(request, 'home/index.html')

def categoriesList(request):
    categories = models.Category.objects.all().order_by('-date')
    blog = models.Blog.objects.all().order_by('-date')[:5]
    return render(request, 'home/categories.html',{'blog':blog, 'categories':categories})

@login_required
def addCategory(request):
    if request.user.is_staff == False:
        return redirect('blogs')
    if request.method == "POST":
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            data = form.save()
            messages.success(request, f"New category created: {data.name}")
    else:
        form = forms.CategoryForm()
    return redirect('blogs')

def viewCategory(request, name):
    category = models.Category.objects.get(name=name)
    blog = models.Blog.objects.filter(category=category).order_by('-date')
    return render(request, 'home/category.html',{'blog':blog, 'category':category})

def blogs(request):
    blogs = models.Blog.objects.all().order_by('-date')
    # Number of items to show per page
    items_per_page = 3
    paginator = Paginator(blogs, items_per_page)

    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        blog = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page
        blog = paginator.page(paginator.num_pages)

    return render(request, 'home/blog.html',{'blog':blog})

@login_required
def addblog(request):
    if request.user.is_staff == False:
        return redirect('blogs')
    if request.method == "POST":
        form = forms.BlogForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.views = 0
            form.save()
            return redirect('blogs')
    else:
        form = forms.BlogForm()
    return render(request, 'home/blogform.html', {'form':form})

@login_required
def addcomment(request, uid):
    blog = models.Blog.objects.get(uid=uid)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.blog = blog
            f.user = request.user
            form.save()
            return JsonResponse({'message':"sent"})
    return JsonResponse({'message':"failed"})

@login_required
def getComment(request, uid):
    blog  = models.Blog.objects.get(uid = uid)
    comment = models.Comment.objects.filter(blog = blog).last()
    if comment:
        data = {
            'id': comment.id,
            'user': f'{comment.user.last_name} {comment.user.first_name}',
            'comment': comment.comment,
            'date': "now",
        }
        return JsonResponse(data, safe=False, status=200)
    data={'message':'empty'}
    return JsonResponse(data, safe=False, status=200)

def blogview(request, uid):
    blog = models.Blog.objects.get(uid=uid)
    comment = models.Comment.objects.filter(blog=blog)
    form = forms.CommentForm(request.POST)
    user_agent = get_user_agent(request)
    device = user_agent.device
    operating_system = user_agent.os
    browser = user_agent.browser
    view = models.views.objects.create(blog=blog,device=device,os=operating_system,browser=browser)
    view.save()
    blog.views += blog.blog_view.all().count()  
    blog.save()
    blog.text = urlize(blog.text)
    return render(request, 'home/blogview.html', {'blog':blog, 'form':form, 'comment':comment})

def About(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Perform a search across multiple models and fields
        blog = models.Blog.objects.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(category__name__icontains=query))
        category = models.Category.objects.filter(name__icontains=query)

    context = {'query': query, 'blog': blog, 'category':category}
    return render(request, 'home/search.html', context)