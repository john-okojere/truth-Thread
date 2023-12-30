from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('About', views.About, name='About'),

    path('addCategory', views.addCategory, name='addCategory'),
    path('Category/list', views.categoriesList, name='ListCategory'),
    path('Category/<str:name>', views.viewCategory, name='viewCategory'),

    path('blogs', views.blogs, name='blogs'),
    path('new', views.addblog, name='addBlog'),
    path('view/<uuid:uid>', views.blogview, name='blogview'),

    path('comment/add/<uuid:uid>', views.addcomment, name='addComment'),
    path('comment/get/<uuid:uid>', views.getComment, name='getComment'),

    path('search/', views.search, name='search'),
]
