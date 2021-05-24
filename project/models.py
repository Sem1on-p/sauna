from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Project(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    main_img = models.ImageField('Главное изображение', upload_to='img/project')
    img2 = models.ImageField('Главное изображение', upload_to='img/project', blank=True)
    img3 = models.ImageField('Главное изображение', upload_to='img/project', blank=True)
    img4 = models.ImageField('Главное изображение', upload_to='img/project', blank=True)
    img5 = models.ImageField('Главное изображение', upload_to='img/project', blank=True)
    img6 = models.ImageField('Главное изображение', upload_to='img/project', blank=True)
    img7 = models.ImageField('Главное изображение', upload_to='img/project', blank=True)
    img8 = models.ImageField('Главное изображение', upload_to='img/project', blank=True)
    img9 = models.ImageField('Главное изображение', upload_to='img/project', blank=True)

    def __str__(self):
        return self.title

    def img_list(self):
        return [self.img2, self.img3, self.img4, self.img5, self.img6]

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
