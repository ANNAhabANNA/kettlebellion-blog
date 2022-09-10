from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    blog_fields = ('content')
    summernote_fields = ('content')
    actions = ['approve_workouts']

    def approve_workouts(self, request, queryset):
        queryset.update(status=1)
    
    #def approve_workouts(self, request, queryset):
        #queryset.update(is_approved = True)
#@admin.action(description = 'Mark selected stories as published')
#def make_published(modeladmin, request, queryset):
    #queryset.update(status='p')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Defines the features and control over the comments in
    the admin panel.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Approves comments
        """
        queryset.update(approved=True)
    
