from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.ForeignKey('auth.User')
    author_cognome=models.CharField(max_length=200)
    author_nome= models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    publisher= models.CharField(max_length=200)
    pub_year = models.IntegerField()
    language= models.CharField(max_length=100)
    translation = models.BooleanField(default=False)
    notes = models.TextField()
    acquisition_year = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    catalog_date = models.DateTimeField(
            blank=True, null=True)
    in_library = models.BooleanField(default=True)
    borrowed = models.BooleanField(default=False)
    borrower = models.CharField(max_length=100,default="Nemo")


    def catalogare(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
