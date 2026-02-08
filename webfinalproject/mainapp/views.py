from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from mainapp.forms import PostForm
from mainapp.models import Post

def home(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    category = request.GET.get('category')
    posts = Post.objects.select_related('user').order_by('-created_at')

    if category in {Post.CATEGORY_LOST, Post.CATEGORY_FOUND}:
        posts = posts.filter(category=category)

    context = {
        'posts': posts[:50],
        'category': category,
        'categories': Post.CATEGORY_CHOICES,
    }
    return render(request, 'home.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(f"{reverse('post_detail')}?id={post.pk}")
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


def post_detail(request):
    post_id = request.GET.get('id')
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def my_posts(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_posts.html', {'posts': posts})
