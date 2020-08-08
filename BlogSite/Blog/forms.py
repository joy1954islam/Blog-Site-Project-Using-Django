from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for Title in self.fields.keys():
            self.fields[Title].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Post
        fields = ['Title','content',]

