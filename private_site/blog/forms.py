from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    """
    
    Arguments:
        forms {[type]} -- [description]
    """

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):
    """ Handle form required to receive data from users
    
    Arguments:
        forms {[type]} -- [description]
    """
    class Meta():
        model = Comment
        fields = ('')

        widgets = {
            'author':   forms.TextInput(attrs={'class': 'textinputclass'}),
            'text' :    forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

