from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from mainapp.forms import PostForm
from mainapp.models import Post

def home(request):
    category = request.GET.get('category')
    posts = Post.objects.select_related('user').order_by('-created_at')

    if category in {Post.CATEGORY_LOST, Post.CATEGORY_FOUND, Post.CATEGORY_CONFESSION}:
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
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


def post_detail(request, pk: int):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def category_feed(request, category_slug: str):
    slug_map = {
        'lost': Post.CATEGORY_LOST,
        'found': Post.CATEGORY_FOUND,
        'confession': Post.CATEGORY_CONFESSION,
    }
    category = slug_map.get(category_slug)
    posts = Post.objects.select_related('user').order_by('-created_at')
    if category:
        posts = posts.filter(category=category)

    context = {
        'posts': posts[:50],
        'category': category,
        'categories': Post.CATEGORY_CHOICES,
    }
    return render(request, 'home.html', context)


@login_required
def my_posts(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_posts.html', {'posts': posts})
