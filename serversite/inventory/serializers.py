from inventory.models import Category, Sub_Category, Attachment, Clothe
from rest_framework import serializers

class Sub_CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Sub_Category 
        fields = ('id', 'name', 'category', 'category_name', 'create_at', 'update_at')

class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'


class ClothesSerializer(serializers.Serializer):
    # category_name = serializers.ReadOnlyField(source='category.category_name')
    # sub_category_name = serializers.ReadOnlyField(source='sub_category.sub_category_name')
    category_name = serializers.ReadOnlyField(source='category.name')
    sub_category_name = serializers.ReadOnlyField(source='sub_category.name')
    
    image1 = serializers.ListField(child=serializers.FileField())
    image2 = serializers.ListField(child=serializers.FileField(), required=False)
    image3 = serializers.ListField(child=serializers.FileField(), required=False)

    class Meta:
        model = Clothe
        fields = '__all__'


class ClothesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothe
        fields = '__all__'



class AttachmentSerializer(serializers.Serializer):
    attachments = serializers.ListField(child=serializers.FileField())
    file1 = serializers.ListField(child=serializers.FileField(), required=False)
    file2 = serializers.ListField(child=serializers.FileField(), required=False)


class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'