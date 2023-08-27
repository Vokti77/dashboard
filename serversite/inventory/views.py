from rest_framework import generics
from .models import Category, Sub_Category, Clothe, Attachment
from django.views.generic.edit import FormView
from rest_framework.generics import ListAPIView
from .forms import ClothesForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.views.decorators.csrf import csrf_exempt
from inventory.serializers import AttachmentSerializer, AttachmentsSerializer, ClothesSerializer
from .serializers import CategotySerializer, Sub_CategorySerializer, ClothesDetailsSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategotySerializer

class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategotySerializer

class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_CategorySerializer

class SubCategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_CategorySerializer



class UploadView(FormView):
    template_name = 'upload.html'
    form_class = ClothesForm
    success_url = '/output/'

    def form_valid(self, form):
        attachments = form.cleaned_data['attachments']
        files1 = form.cleaned_data['file1']
        files2 = form.cleaned_data['file2']

        for idx in range(min(len(attachments), len(files1), len(files2))):
            attachment = Clothe.objects.create(
                clothes_orginal=attachments[idx],
                clothes=files1[idx] if idx < len(files1) else None,
                clothes_mask=files2[idx] if idx < len(files2) else None,
            )

        return super(UploadView, self).form_valid(form)
    

class ClothesViewAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClothesSerializer(data=request.data)

        if serializer.is_valid():
            image1 = serializer.validated_data['image1']
            image2 = serializer.validated_data.get('image2', [])
            image3 = serializer.validated_data.get('image3', [])

            for idx in range(min(len(image1), len(image2), len(image3))):
                # category_id = request.data[f'category{idx}']  # Adjust the field name based on your frontend form
                # sub_category_id = request.data[f'sub_category{idx}']  # Adjust the field name
                Clothe.objects.create(
                    # category_id=category_id,
                    # sub_category_id=sub_category_id,
                    clothes_orginal=image1[idx],
                    clothes=image2[idx] if idx < len(image2) else None,
                    clothes_mask=image3[idx] if idx < len(image3) else None,
                )

            return Response({'message': 'Files uploaded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
from rest_framework.generics import ListCreateAPIView

# class ClothesViewAPI(ListCreateAPIView):
#     queryset = Clothe.objects.all()
#     serializer_class = ClothesSerializer

#     def get_queryset(self):
#         return Clothe.objects.select_related('category', 'sub_category')

class ClothesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothe.objects.all()
    serializer_class = ClothesDetailsSerializer

class ClothesListView(ListAPIView):
    queryset = Clothe.objects.all()
    serializer_class = ClothesDetailsSerializer


class UploadViewAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AttachmentSerializer(data=request.data)

        if serializer.is_valid():
            attachments = serializer.validated_data['attachments']
            files1 = serializer.validated_data.get('file1', [])
            files2 = serializer.validated_data.get('file2', [])

            for idx in range(min(len(attachments), len(files1), len(files2))):
                Attachment.objects.create(
                    file=attachments[idx],
                    file1=files1[idx] if idx < len(files1) else None,
                    file2=files2[idx] if idx < len(files2) else None,
                )

            return Response({'message': 'Files uploaded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttachmentListView(ListAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentsSerializer