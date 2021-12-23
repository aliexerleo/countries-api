from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=60)
    flag = models.ImageField(
        upload_to = 'picture', 
		blank=True,
		null=True,
		help_text="flag of country")    
    
    continet = models.CharField(max_length=50)