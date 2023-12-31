from home import forms, models
def context(request):
    categoryForm = forms.CategoryForm()
    categories = models.Category.objects.all().order_by('name')
    catList = []
    for cat in categories:
        if len(catList) > 4:
            if cat.cat_blog.all().count() > 0:
                catList.append(cat)
        else:
                catList.append(cat)
    blog = models.Blog.objects.all().order_by('-date')[:4]
    trend = models.Blog.objects.all().order_by('-views')[:6]
    context = {
        'categoryForm':categoryForm,
        'categories':catList,
        'recent_blog':blog,
        'trend':trend,
    }
    return context