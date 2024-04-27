from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Recipes
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

#handles the creation of a post
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

#handles the creation of the recommendation
def CreateRecommendation(request):
    MealRecommendation = None
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #extract data
            title = form.cleaned_data['title']
            ingredients = form.cleaned_data['ingredients']
            tools = form.cleaned_data['tools']

            MealRecommendation = GetFoodRec(title, ingredients, tools)

            if MealRecommendation:                
                #save recipe to database
                Recipes.objects.create(
                    title = title,
                    ingredients = ingredients,
                    tools = tools,
                    recommendation = MealRecommendation,
                )
                #redirect to recipe page
                return redirect('my_recipes')
            else:
                #show error
                print("Error: Recommendation could not be generated.")
    else:
        form = PostForm()

    return render(request, 'recommender/create_recommendation.html', {'form': form})

#retrieve recipes from database and posts it to template
def recipes_page(request):
    recipes = Recipes.objects.all()
    return render(request, 'recommender/my_recipes.html', {'recipes': recipes})

#method to delete a recipe
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('my_recipes')
    else:
        pass