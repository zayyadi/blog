from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# from users.models import NewUser
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Q
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.models import Tag
from .models import Article, Category

from .forms import ApprovalForm, ArticleForm, CommentForm, CategoryForm


def check_super(user):
    return user.is_superuser


@login_required
def addCategory(request):
    form = CategoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save_m2m()

        messages.success(request, "Category created successfully")
        return redirect("blog:articles")
    context = {
        "form": form,
    }
    return render(request, "blog/addCategory.html", context)


def articles(request, slug=None):
    articles = Article.objects.all().filter(status="published")
    paginator = Paginator(articles, 5)
    page = request.GET.get("page")
    tag = None
    if slug:
        get_object_or_404(Tag, slug=slug)
    # Article.tags.most_common()[:2]
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        "articles": articles,
        "tag": tag,
        "page": page,
    }

    return render(request, "blog/articles.html", context)


@login_required
def LikeView(request, slug):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, slug=slug)
        article.likes.add(request.user)
        return redirect("blog:detail", article.slug)
    else:
        messages.error(request, "You must be logged in to like posts.")
        return redirect(reverse("blog:detail", args=[slug]))


def about(request):
    return render(request, "blog/about.html")


@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {"articles": articles}
    return render(request, "blog/dashboard.html", context)


@login_required
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    common_tags = Article.tags.most_common()[:4]
    if form.is_valid():
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.author = request.user
        article.save()
        form.save_m2m()

        messages.success(request, "Article created successfully")
        return redirect("blog:dashboard")
    context = {
        "common_tags": common_tags,
        "form": form,
    }
    return render(request, "blog/addarticle.html", context)


# def detail(request, post):
#     # article = Article.objects.filter(id = id).first()
#     article = get_object_or_404(Article, slug=post, status="published")
#     allcomments = article.comments.filter(active=True)
#     page = request.GET.get("page", 1)

#     paginator = Paginator(allcomments, 10)
#     try:
#         comments = paginator.page(page)
#     except PageNotAnInteger:
#         comments = paginator.page(1)
#     except EmptyPage:
#         comments = paginator.page(paginator.num_pages)
#     article_tags = Article.tags.values_list("id", flat=True)
#     similar_posts = Article.objects.filter(tags__in=article_tags).exclude(id=article.id)
#     similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
#         "-same_tags", "-publish"
#     )[:3]

#     comments = article.comments.filter(active=True)

#     user_comment = None

#     if request.method == "POST":
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             user_comment = comment_form.save(commit=False)
#             user_comment.post = article
#             user_comment.save()
#             return HttpResponseRedirect(request.path_info)
#     else:
#         comment_form = CommentForm()

#     context = {
#         "comments": user_comment,
#         "comments": comments,
#         "comment_form": comment_form,
#         "allcomments": allcomments,
#         "article": article,
#         "similar_posts": similar_posts,
#     }

#     return render(request, "blog/detail.html", context)


def detail(request, post):
    # Retrieve the article by slug and ensure it's published
    article = get_object_or_404(Article, slug=post, status="published")
    allcomments = article.comments.filter(
        active=True, parent=None
    )  # Only top-level comments for pagination

    # Set up pagination for top-level comments
    page = request.GET.get("page", 1)
    paginator = Paginator(allcomments, 10)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    # Get related posts based on shared tags
    article_tags = article.tags.values_list("id", flat=True)
    similar_posts = Article.objects.filter(tags__in=article_tags).exclude(id=article.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )[:3]

    user_comment = None
    if request.method == "POST":
        # Handle comment form submission
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = article
            user_comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()

    context = {
        "comments": user_comment,  # Paginated top-level comments
        "comments": comments,  # Paginated top-level comments
        "allcomments": allcomments,
        "comment_form": comment_form,  # Form for new comments
        "article": article,  # Current article details
        "similar_posts": similar_posts,  # Articles with similar tags
    }

    return render(request, "blog/detail.html", context)


@user_passes_test(check_super)
@login_required
def list_unpublished(request):
    unpub = Article.unpublished.all()
    return render(request, "blog/list_unpub.html", {"unpub": unpub})


@user_passes_test(check_super)
@login_required
def approve_post(request, slug):
    post = get_object_or_404(Article, slug=slug)
    form = ApprovalForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save()
        messages.success(request, "Article has been Updated")
        return redirect("blog:dashboard")
    return render(request, "blog/approve.html", {"form": form})


@login_required
def updateArticle(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Article has been Updated")
        return redirect("blog:dashboard")
    return render(request, "blog/update.html", {"form": form})


@login_required
def deleteArticle(request, slug):
    article = get_object_or_404(Article, slug=slug)

    article.delete()

    messages.success(request, "Article Deleted Successfully")

    return redirect("blog:dashboard")


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Article.tags.most_common()[:4]
    article = Article.objects.filter(tags=tag)
    context = {
        "tag": tag,
        "common_tags": common_tags,
        "article": article,
    }
    return render(request, "blog/tag_list.html", context)


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    article = Article.objects.filter(category=category)

    context = {"category": category, "article": article}

    return render(request, "blog/category.html", context)


def category_list(request):
    category_list = Category.objects.exclude(name="default")
    context = {
        "category_list": category_list,
    }
    return context


# def post_search(request):
#     form = PostSearchForm()
#     q = ""
#     c = ""
#     results = []
#     query = Q()

#     if "q" in request.GET:
#         form = PostSearchForm(request.GET)
#         if form.is_valid():
#             q = form.cleaned_data["q"]
#             c = form.cleaned_data["c"]

#             if c is not None:
#                 query &= Q(category=c)
#             if q is not None:
#                 query &= Q(title__contains=q)

#             results = Article.objects.filter(query)

#     return render(request, "search.html", {"form": form, "q": q, "results": results})


def search_posts(request):
    query = request.GET.get("q")
    if query:
        results = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )  # Search in title or content
    else:
        results = Article.objects.none()

    return render(request, "search_results.html", {"results": results, "query": query})
