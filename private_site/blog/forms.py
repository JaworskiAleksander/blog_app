from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    """
    create form in order to acquire post from user
    """

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):
    """ 
    create form in order to acquire comment from user
    """
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':   forms.TextInput(attrs={'class': 'textinputclass'}),
            'text' :    forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

