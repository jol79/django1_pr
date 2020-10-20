from django import forms


# form to share post link via email
class EmailPostForm(forms.Form):
    # analogy in HTML: <input type="text">
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    # <textarea> instead of using <input> tag by pasting [widget] attribute
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
