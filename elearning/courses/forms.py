from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):                #helper form by django
    content = forms.CharField(widget=forms.Textarea(attrs={


        'class':'form-control',
        'placeholder':'Type your comment',
        'id':'usercomment',
        'rows':'4'



    }))
    class Meta:
        model = Comment
        fields={'content',}