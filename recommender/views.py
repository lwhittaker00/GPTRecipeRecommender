from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from .utils import GetFoodRec
from django.http import JsonResponse

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'recommender/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'recommender/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'recommender/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'recommender/post_edit.html', {'form': form})

def CreateRecommendation(request):
    MealRecommendation = None 
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #extract data 
            title = form.cleaned_data['title']
            ingredients = form.cleaned_data['ingredients']
            tools = form.cleaned_data['tools']

            #generate recommendation
            MealRecommendation = GetFoodRec(title, ingredients, tools)

            #send to template
            return render(request, 'recommender/your_template.html', {'form': form, 'Meal Recommendation': MealRecommendation})
    else:
        form = PostForm()
    return render(request, 'recommender/your_template.html', {'form': form, 'Meal Recommendation': MealRecommendation})