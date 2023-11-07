from django.db import connections
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
 
 
class Recipe(models.Model):

	class Type(models.TextChoices):
		VEG = 'Veg', _('Veg')
		NON_VEG = 'Non-Veg', _('Non-Veg')
		EGG = 'Egg', _('Egg')
		VEGAN = 'Vegan', _('Vegan')

	Recipe_id = models.AutoField(primary_key=True)
	Recipe_name = models.CharField(max_length=100)
	Recipe_description = models.TextField()
	Recipe_type = models.CharField(max_length=100, choices=Type.choices, default=Type.VEG)
	Recipe_category = models.CharField(max_length=100)
	img = models.ImageField(default='recipe_default.jpg', upload_to='recipe_imgs')
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		db_table="recipes"
	
	def __str__(self):
		return str(self.Recipe_name)

class Recipe_prep_details(models.Model):
	Recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, primary_key=True)
	preparation_time = models.CharField(max_length=100)
	num_of_servings = models.IntegerField()
	ingredients = models.TextField()
	instructions = models.TextField()

	class Meta:
		db_table="recipe_prep_details"

	def __str__(self):
		return str(self.Recipe.Recipe_name)


class Nutri_content(models.Model):
	Recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, primary_key=True)
	calories_per_serving = models.CharField(max_length=100)
	carbs = models.CharField(max_length=100)
	proteins = models.CharField(max_length=100)
	saturated_fats = models.CharField(max_length=100)
	trans_fats = models.CharField(max_length=100)
	cholestrol = models.CharField(max_length=100)

	class Meta:
		db_table="nutri_content"

	def __str__(self):
		return str(self.Recipe_id)


class feedback(models.Model):
	Full_name = models.CharField(max_length=100, null=True, blank=True)
	Email = models.CharField(max_length=100)
	Message = models.TextField()

	def __str__(self):
		return f'{self.Full_name}'