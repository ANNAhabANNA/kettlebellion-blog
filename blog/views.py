from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, WorkoutForm

def about(request):
    """
    Renders about.html 
    """
    return render(request, "about.html")

def add_workout(request):
    """
    Renders add_workout.html
    """
    workout_form = WorkoutForm(request.POST or None, request.FILES or None)
    context = {
        'workout_form': workout_form,
    }

    if request.method == "POST":
        workout_form = WorkoutForm(request.POST, request.FILES)
        if workout_form.is_valid():
            workout_form = workout_form.save(commit=False)
            workout_form.author = request.user
            workout_form.status = 1
            workout_form.save()
            return redirect('home')
    else:
        workout_form = WorkoutForm()
    return render(request, 'add_workout.html', context)

#Generic class-based view
class PostList(generic.ListView):
    """
    Creates the post list
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):
    """
    Creates the post detail
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists:
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists:
            liked = True
        
        #Variable for saving data from the crispy form
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class PostLike(View):

    """
    Creates the post like
    """
    
    def post(self, request, slug, *args, **kwargs):
        #Gets the relevant post
        post = get_object_or_404(Post, slug=slug)
        #Checks if the is already liked
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        #Reloads post_detail.html to see the result
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    