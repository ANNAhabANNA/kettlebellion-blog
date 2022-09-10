from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
    is_approved = models.BooleanField(default=False)

    class Meta:
        """
        Workouts in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Shows the title
        """
        return self.title
    
    def number_of_likes(self):
        """
        Adds total of likes 
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        """
        Saves form input
        """
        if not self.slug:
            self.slug = self.title.replace(" ", '-')
        super().save(*args, **kwargs)

    def allowed_to_edit(self, request,slug):
        """
        Authenticates for editing
        """
        if self.author:
            return True
        else:
            return False

    def allowed_to_delete(self, request, slug):
        """
        Authenticates for deletion
        """       
        if self.author:
            return True
        else:
            return False


class Comment(models.Model):
    """
    Comment class
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Comments in ascending order.
        """
        ordering = ['created_on']
    
    def __str__(self):
        """
        Returns a string with comment and author.
        """
        return f"Comment {self.body} by {self.name}"