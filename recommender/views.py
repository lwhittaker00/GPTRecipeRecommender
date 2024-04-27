from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from .utils import GetFoodRec

#retrieves posts from database and passes to template
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'recommender/post_list.html', {'posts': posts})

#retrieves pk from database and saves
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'recommender/post_detail.html', {'post': post})

#handles the creation of the recommendation
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #extract data
            title = form.cleaned_data['title']
            ingredients = form.cleaned_data['ingredients']
            tools = form.cleaned_data['tools']

            MealRecommendation = GetFoodRec(title, ingredients, tools)

            if MealRecommendation:                
                #save recipe to database
                post = Post.objects.create(
                    title = title,
                    ingredients = ingredients,
                    tools = tools,
                    recommendation = MealRecommendation,
                )

                post.created_date = timezone.now()
                post.save()
                #redirect to recipe list page
                return redirect('post_detail', pk=post.pk)
            else:
                #show error
                print("Error: Recommendation could not be generated.")
    else:
        form = PostForm()
    return render(request, 'recommender/post_edit.html', {'form': form})

#handles edit of existing post
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

#handles deletion of existing post
def delete_recommendation(request, post_id):
    recommendation = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        recommendation.delete()
        return redirect('post_list')
    else:
        pass