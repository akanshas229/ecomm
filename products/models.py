# from django.db import models

# class Mobile(models.Model):
#     Image = models.ImageField(upload_to='electronics/mobiles', null=True, blank=True, )
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     Price = models.CharField(max_length=50, null=True, blank=True)
#     slug = models.CharField(max_length=50, null=True, blank=True)
#     def __str__(self):
#         return self.Name

# class Tablet(models.Model):
#     Image = models.ImageField(upload_to='electronics/mobiles', null=True, blank=True, )
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     Price = models.CharField(max_length=50, null=True, blank=True)
#     slug = models.CharField(max_length=50, null=True, blank=True)
#     def __str__(self):
#         return self.Name
    


# Create your models here.
# CHOICE_FIELDS = (
#         ("mobile","mobile"),
#         ("computer","computer"),
#         ("tv","tv"),
#         ("camera","camera"),
#         ("headphones","headphones"),
#         ("speakers","speakers"),
#     )
# class Electronics(models.Model):
#     catagory = models.CharField(max_length=50, choices=CHOICE_FIELDS, default='mobile')
#     Image = models.ImageField(upload_to='electronics', null=True, blank=True, )
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name
		
	
# SPORTSWEAR = (
#     ("upper","upper"),
#     ("bottom-wear","bottom-wear"),
# )	
# class Sports(models.Model):
#     category = models.CharField(max_length=50, choices=SPORTSWEAR, default='upper')
#     Image = models.ImageField(upload_to='sports', null=True, blank=True)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name

# MENS = (
#     ("shirt","shirt"),
#     ("t-shirt","t-shirt"),
#     ("bottom-wear","bottom-wear"),
# )
# class Men(models.Model):
#     category = models.CharField(max_length=50, choices=MENS, default='shirt')
#     Image = models.ImageField(upload_to='men', null=True, blank=True,)
#     Name = models.CharField(max_length=50, null=True, blank=True)

#     def __str__(self):
#         return self.Name + ' -- ' + self.category
    


# WOMENS = (
#     ("top","top"),
#     ("shirt","shirt"),
#     ("t-shirt","t-shirt"),
#     ("bottom-wear","bottom-wear"),
# )
# class Women(models.Model):
#     category = models.CharField(max_length=50, choices=WOMENS, default='top')
#     Image = models.ImageField(upload_to='women', null=True, blank=True,)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name

# class Kid(models.Model):
#     Image = models.ImageField(upload_to='kid', null=True, blank=True)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name

# class Fashion(models.Model):
#     Image = models.ImageField(upload_to='fashion', null=True, blank=True,)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name

# class Household(models.Model):
#     Image = models.ImageField(upload_to='household', null=True, blank=True,)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name

# class Interior(models.Model):
#     Image = models.ImageField(upload_to='interior', null=True, blank=True)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name
     
# class Clothing(models.Model):
#     Image = models.ImageField(upload_to='clothing', null=True, blank=True)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name     

# class Bag(models.Model):
#     Image = models.ImageField(upload_to='bag', null=True, blank=True)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name

# class Shoe(models.Model):
#     Image = models.ImageField(upload_to='shoe', null=True, blank=True)
#     Name = models.CharField(max_length=50, null=True, blank=True)
#     def _str_(self):
#         return self.Name