from home import forms, models
def context(request):
    categoryForm = forms.CategoryForm()
    categories = models.Category.objects.all().order_by('name')
    catList = []
    for cat in categories:
        if cat.cat_blog.all().count() > 0:
            catList.append(cat)
    blog = models.Blog.objects.all().order_by('-date')[:4]
    trend = models.Blog.objects.all().order_by('-views')[:4]
    context = {
        'categoryForm':categoryForm,
        'categories':catList,
        'recent_blog':blog,
        'trend':trend,
    }
    return context