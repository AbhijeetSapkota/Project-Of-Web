from django import forms
from mainapp.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'description',
            'location',
            'contact_info',
            'is_anonymous',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def clean(self):
        return super().clean()
