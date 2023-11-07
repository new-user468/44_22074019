from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from recipe.models import Recipe, Recipe_prep_details, Nutri_content, feedback
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import Form1, Form2, Form3, feedback_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
class RecipeListView(ListView):
	model = Recipe
	template_name = 'recipe/home.html'
	context_object_name = 'Recipe'
	paginate_by=8

class UserRecipeListView(ListView):
	model = Recipe
	template_name = 'recipe/user_recipe.html'
	context_object_name = 'Recipe'
	paginate_by=8

	def get_queryset(self):
		usr = get_object_or_404(User, username=self.kwargs.get('usr_name'))
		return Recipe.objects.filter(user=usr)

class RecipeDetailView(DetailView):
	model = Recipe
	template_name = 'recipe/single_recipe.html'

def contact(request):
	if request.method == 'POST':
		form = feedback_form(request.POST)
		form.save()
		messages.success(request, f'Your message has been sent!')
		return redirect('recipe-contact')
	else:
		form = feedback_form()
	return render(request,'recipe/contact.html', {'title' : 'Contact', 'form':form})

def about(request):
	return render(request,'recipe/about.html', {'title' : 'About'})

from django.shortcuts import render
from .models import Recipe

def category(request, cat_name):
    recipes = Recipe.objects.filter(Recipe_category=cat_name)
    context = {
        'recipes': recipes,
        'title': cat_name,
        'cat_name': cat_name
    }
    return render(request, 'recipe/category.html', context)


# def category(request, cat_name):
# 	var = {
# 	'Recipe': Recipe.objects.all(),
# 	'title': cat_name,
# 	'cat_name': cat_name
# 	}
# 	return render(request, 'recipe/category.html', var)

def type(request, typ_name):
	var = {
	'Recipe': Recipe.objects.all(),
	'title': typ_name,
	'typ_name': typ_name
	}
	return render(request, 'recipe/type.html', var)


@login_required
# def RecipeCreateView(request):
# 	if request.method == 'POST':
# 		form1 = Form1(request.POST)
# 		form1.instance.user = request.user
# 		form2 = Form2(request.POST)
# 		form2.instance.Recipe = form1.instance
# 		form3 = Form3(request.POST)
# 		form3.instance.Recipe = form1.instance
# 		if form1.is_valid() and form2.is_valid() and form3.is_valid():
# 			form1.save()
# 			form2.save()
# 			form3.save()
# 			name = form1.cleaned_data.get('Recipe_name')
# 			messages.success(request, f'Your recipe "{name}" has been uploaded!')
# 			return redirect('recipe-detail', pk=form1.instance.Recipe_id)

# 	else:
# 		form1 = Form1()
# 		form2 = Form2()
# 		form3 = Form3()

# 	var = {'form1': form1, 'form2':form2, 'form3': form3, 'submit_label': 'Upload'}

# 	return render(request, 'recipe/recipe_form.html', var)

@login_required
def RecipeCreateView(request):
    if request.method == 'POST':
        form1 = Form1(request.POST)
        form1.instance.user = request.user
        form2 = Form2(request.POST)
        form2.instance.Recipe = form1.instance
        form3 = Form3(request.POST)
        form3.instance.Recipe = form1.instance
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            name = form1.cleaned_data.get('Recipe_name')
            messages.success(request, f'Your recipe "{name}" has been uploaded!')
            return redirect('recipe-detail', pk=form1.instance.Recipe_id)

    else:
        form1 = Form1()
        form2 = Form2()
        form3 = Form3()

    var = {'form1': form1, 'form2': form2, 'form3': form3, 'submit_label': 'Upload'}

    return render(request, 'recipe/recipe_form.html', var)




@login_required
def RecipeUpdateView(request, pk):
	r = Recipe.objects.filter(Recipe_id=pk).first()
	if r.user == request.user:
		if request.method == 'POST':
			form1 = Form1(request.POST, instance=r)
			form1.instance.user = request.user
			form2 = Form2(request.POST, instance=r.recipe_prep_details)
			form2.instance.Recipe = form1.instance
			form3 = Form3(request.POST, instance=r.nutri_content)
			form3.instance.Recipe = form1.instance
			if form1.is_valid() and form2.is_valid() and form3.is_valid():
				form1.save()
				form2.save()
				form3.save()
				name = form1.cleaned_data.get('Recipe_name')
				messages.success(request, f'Your recipe {name} has been updated!')
				return redirect('recipe-home')

		else:
			form1 = Form1(instance=r)
			form2 = Form2(instance=r.recipe_prep_details)
			form3 = Form3(instance=r.nutri_content)

		var = {'form1': form1, 'form2':form2, 'form3': form3, 'submit_label': 'Update'}

		return render(request, 'recipe/recipe_form.html', var)

	else:
		return HttpResponse('<h1> 403 Forbidden </h1>')



class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Recipe
	success_url = "/"

	def test_func(self):
		if self.request.user == self.get_object().user:
			return True
		return False