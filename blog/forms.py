from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class WorkoutForm(forms.ModelForm):
    """
    Recipe Input Form
    """
    class Meta:
        """
        Meta class
        """
        model = Post
        fields = [
            'title',
            'workout_level',
            'workout_length',
            'content',
        ]
   

    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)

    def workout_length(self):
        """
        Ensures workout length is greater than zero
        """
        value = self.cleaned_data.get("length")
        print(value)
        if value < 1:
            raise forms.ValidationError(
                "The workout lenght must be greater than zero"
                )
        return value