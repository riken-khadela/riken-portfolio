from django.db import models
from django.utils.text import slugify

# Create your models here.


class project(models.Model):
    
    MainTitle = models.CharField(max_length=30,unique=True)
    slug = models.SlugField(unique=True, max_length=255)
    img1 = models.URLField(blank=True)
    UseFor = models.TextField(null=True,blank=True)
    
    SmallDiscription = models.TextField(null=True,blank=True)
    technologies = models.TextField(null=True,blank=True)
    img2 = models.URLField(blank=True)
    
    Challanges = models.TextField(null=True,blank=True)
    Solution = models.TextField(null=True,blank=True)
    img3 = models.URLField(blank=True)
    Conclusion = models.TextField(null=True,blank=True)
    
    github = models.CharField(max_length=255,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/project/{self.slug}/"