
from django.urls import path
from .views import CategoryListCreateView, ClothesDetailView, ClothesListView, CategoryRetrieveUpdateDeleteView, SubCategoryListCreateView, SubCategoryRetrieveUpdateDeleteView, UploadView, UploadViewAPI, AttachmentListView, ClothesViewAPI

urlpatterns = [
    # path('output/', views.output, name='output'),
    path('categories', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>', CategoryRetrieveUpdateDeleteView.as_view(), name='category-detail'),
    path('subcategories', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>', SubCategoryRetrieveUpdateDeleteView.as_view(), name='subcategory-detail'),
    path('clothes/', ClothesViewAPI.as_view(), name='clothes'),
    path('clothes_list', ClothesListView.as_view(), name='clothes-list'),
    path('clothe/<int:pk>', ClothesDetailView.as_view(), name='clothes-detail'),
    # ... other URL patterns
    path('mulup', UploadView.as_view(), name="mulup"),
    path('upapi/', UploadViewAPI.as_view(), name='upapi'),
    path('attachments/', AttachmentListView.as_view(), name='attachment-list'),

]
