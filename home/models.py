from django.db import models
import uuid
from users import models as user_model

class Category(models.Model):
    name = models.CharField(max_length=255 , unique=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'
    

class Blog(models.Model):
    uid = models.UUIDField( default=uuid.uuid4, editable=False)
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Blog/%y/%m/%d", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cat_blog")
    text = models.TextField()
    views = models.IntegerField() 
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.blog}'
    
class views(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_view')
    device = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    browser = models.CharField(max_length=255)    
    
    def __str__(self):
        return f'{self.blog}'
