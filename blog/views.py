from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Post, Category
# Homepage, detail, year, month, category

POSTS_PER_PAGE = 5

# TODO 404 handler page
# TODO Fix colors on heading: match main site, more visible


def index(request, page_number=0):
    # Normally gets returned as a string. Fix this to prevent errors.
    page_number = int(page_number)

    # Indices for slicing the right number of posts.
    start = page_number * POSTS_PER_PAGE
    end = (page_number + 1) * POSTS_PER_PAGE

    posts = Post.objects.filter(published=True).order_by('updated_at').reverse()[start:end]

    context = {'posts': posts}

    # Give link for next page if applicable
    if len(posts) == POSTS_PER_PAGE:
        context['next_page'] = page_number + 1
    else:
        context['next_page'] = 0

    # Give link for previous page if applicable
    context['previous_page'] = page_number - 1

    return render(request, 'blog/blog_home.html', context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.published is False:
        raise Http404("Post is not published.")

    return render(request, 'blog/view_post.html', {'post': post})


def view_category(request, category):
    # TODO allow for multiple pages

    selected_category = get_object_or_404(Category, slug=category)

    posts = Post.objects.filter(category=selected_category, published=True).order_by('updated_at').reverse()

    return render(request, 'blog/view_category.html', {'posts': posts, 'category': selected_category})
