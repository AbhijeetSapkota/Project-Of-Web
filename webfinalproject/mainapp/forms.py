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
        cleaned = super().clean()
        category = cleaned.get('category')

        if category == Post.CATEGORY_CONFESSION:
            cleaned['location'] = ''
            cleaned['contact_info'] = ''

        return cleaned
