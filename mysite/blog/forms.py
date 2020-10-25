from django import forms
from .models import Comment


# form to share post link via email
class EmailPostForm(forms.Form):
    # analogy in HTML: <input type="text">
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    # <textarea> instead of using <input> tag by pasting [widget] attribute
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


# for comments I will use ModelForm because I need to build
# a form dynamically from Comment model
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


# search form
class SearchForm(forms.Form): 
    query = forms.CharField()
