from django.db import models
from django.utils.text import slugify

# Create your models here.


class project(models.Model):
    
    MainTitle = models.CharField(max_length=30,unique=True)
    MainTitleSummery = models.CharField(max_length=255,null=True,blank=True)
    slug = models.SlugField(unique=True, max_length=255,blank=True)
    WhatIsAboutThisProject = models.TextField(null=True,blank=True)
    SmallDiscription = models.TextField(null=True,blank=True)
    technologies = models.TextField(null=True,blank=True)
    
    Img1Title = models.CharField(null=True,blank=True,max_length=255)
    img1 = models.URLField(blank=True)
    img1Text = models.TextField(null=True,blank=True)
    
    
    Img2Title = models.CharField(null=True,blank=True,max_length=255)
    img2 = models.URLField(blank=True)
    img2Text = models.TextField(null=True,blank=True)
    
    
    ChallangesTitle = models.CharField(null=True,blank=True,max_length=255)
    Challanges = models.TextField(null=True,blank=True)
    Solution = models.TextField(null=True,blank=True)
    
    Img3Title = models.CharField(null=True,blank=True,max_length=255)
    img3 = models.URLField(blank=True)
    img3Text = models.TextField(null=True,blank=True)
    
    Conclusion = models.TextField(null=True,blank=True)
    
    github = models.URLField(max_length=255,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.MainTitle)
        super(project, self).save(*args, **kwargs)

    def __str__(self):
        return self.MainTitle

    def get_absolute_url(self):
        return f"/project/{self.slug}/"