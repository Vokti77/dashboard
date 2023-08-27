import json
from django.db import models
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)   # T-Shirt
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Use ForeignKey
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

        

class Attachment(models.Model):
    image_name = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='attachments')
    file1 = models.FileField(upload_to='attachments1', default='')
    file2 = models.FileField(upload_to='attachments2', default='')

    def save(self, *args, **kwargs):
        if not self.image_name:  
            base_name = os.path.basename(self.file.name)
            name, extension = os.path.splitext(base_name)
            self.image_name = name
        super(Attachment, self).save(*args, **kwargs)
        

class Clothe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    clothe_name = models.CharField(max_length=50, blank=True)

    SLEEVE_CHOICES = [
        ("full", "full"),
        ("half", "half"),
        ("less", "less"),
        
    ]
    sleeve = models.CharField(max_length=5, choices=SLEEVE_CHOICES, default="full")

    LENTH_CHOICES = [
        ("full", "full"),
        ("half", "half"),
        
    ]
    lenth = models.CharField(max_length=5, choices=LENTH_CHOICES, default="full")

    CKPT_CHOICES = [
        ("0", "0"),
        ("1", "1"),
        
    ]
    ckpt = models.CharField(max_length=5, choices=CKPT_CHOICES, default="0")
    clothes_orginal = models.FileField(upload_to='clothes_orginal')
    clothes = models.FileField(upload_to='clothes')
    clothes_mask = models.FileField(upload_to='clothes_mask')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.clothe_name:  
            base_name = os.path.basename(self.clothes_orginal.name)
            name, extension = os.path.splitext(base_name)
            self.clothe_name = name
        super(Clothe, self).save(*args, **kwargs)

    def __str__(self):
        return self.clothe_name