from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes',blank=True)
    description = models.TextField(blank=True)
    workout_length = models.IntegerField(default=0)
    workout_level = models.CharField(max_length=200)
    directions = models.TextField()
    additional_equipment = models.CharField(max_length=200)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", '-')
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Posts in descending order.
        """
        ordering = ['created_on']
    
    def __str__(self):
        """
        Returns a string with comment and author.
        """
        return f"Comment {self.body} by {self.name}"