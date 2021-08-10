from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=50, null=False, blank=False)
    Image = models.ImageField(upload_to='product', null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    # Price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.Name + ' -- ' + self.category