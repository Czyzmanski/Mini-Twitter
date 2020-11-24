from django import forms


class PostForm(forms.Form):
    text = forms.CharField(label='Text', max_length=500)
