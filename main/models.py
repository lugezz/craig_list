from re import search
from tabnanny import verbose
from django.db import models

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        res = self.search[:20] + "..." if len(self.search)> 20 else self.search

        return res
    
    class Meta:
        verbose_name_plural = 'Searches'
