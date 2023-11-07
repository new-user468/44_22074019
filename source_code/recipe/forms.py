from django import forms
from .models import Recipe, Nutri_content, Recipe_prep_details, feedback

# class Form1(forms.ModelForm):
# 	class Meta:
# 		model = Recipe
# 		fields = ['Recipe_name', 'Recipe_description', 'Recipe_category', 'Recipe_type']

class Form1(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Soup', 'Soup'),
        ('Salad', 'Salad'),
        ('Starter', 'Starter'),
        ('Meal', 'Meal'),
        ('Dessert', 'Dessert'),
        ('Drink', 'Drink'),
        ('Bakery', 'Bakery'),
    ]

    class Meta:
        model = Recipe
        fields = ['Recipe_name', 'Recipe_description', 'Recipe_category', 'Recipe_type']

    Recipe_category = forms.ChoiceField(choices=CATEGORY_CHOICES)


class Form2(forms.ModelForm):
	class Meta:
		model = Recipe_prep_details
		fields = ['preparation_time', 'num_of_servings', 'ingredients', 'instructions']

class Form3(forms.ModelForm):
	class Meta:
		model = Nutri_content
		fields = ['calories_per_serving', 'carbs', 'proteins', 'saturated_fats', 'trans_fats', 'cholestrol']

class feedback_form(forms.ModelForm):
	class Meta:
		model = feedback
		fields = '__all__'