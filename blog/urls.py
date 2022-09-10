from . import views
from django.urls import path

urlpatterns = [
    # as_view method to render class as a view
    path("", views.PostList.as_view(), name="home"),
    path('about/', views.about, name='about'),
    path('share-a-workout/', views.add_workout, name="add_workout"),
    path('edit-a-workout/<slug:slug>', views.edit_workout, name='edit_workout'),
    path('delete-a-workout/<slug:slug>', views.delete_workout,
         name='delete_workout'),
    path('<slug:slug>/', views.PostDetail.as_view(), 
    name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

]