import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django import forms
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
from .models import Clothe

class ClothesForm(forms.ModelForm):
    attachments = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)
    file1 = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)
    file2 = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)

    class Meta:
        model = Clothe
        fields = ('category', 'sub_category', 'sleeve', 'lenth', 'ckpt', 'attachments', 'file1', 'file2')

class UploadForm(forms.Form):
    name = forms.CharField(max_length=100)
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    file1 = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    file2 = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
