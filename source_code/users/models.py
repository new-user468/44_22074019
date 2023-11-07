from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pic = models.ImageField(default='profile_default.jpeg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		pic = Image.open(self.pic.path)

		if pic.width > 300 or pic.height > 300:
			output_size = (300, 300)
			pic.thumbnail(output_size)
			pic.save(self.pic.path)

