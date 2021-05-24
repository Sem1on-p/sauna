from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField('Загаловок', max_length = 100)
	description = models.TextField('Краткое описание')
	text = models.TextField('Текст статьи')
	img = models.ImageField('Изображение', upload_to='img/blog/')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'
		