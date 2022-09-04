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
            'additional_equipment',
            'directions',
        ]
   

    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)

    def clean_servings(self):
        """
        Ensures servings is greater than zero
        """
        value = self.cleaned_data.get("serves")
        print(value)
        if value < 1:
            raise forms.ValidationError(
                "The number of servings must be greater than zero"
                )
        return value