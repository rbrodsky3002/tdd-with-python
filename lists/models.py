from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class List(models.Model):

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    parent_list = models.ForeignKey(List, default='')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('id',)
        unique_together = ('parent_list', 'text')
