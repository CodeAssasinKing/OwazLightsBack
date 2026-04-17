import os
from django.http import FileResponse
from core.views import StandardPagination
from rest_framework.generics import ListAPIView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from products.models import Products, ProductCategory, ProductSubcategory, ProductSize
from products.serializers import (
    ProductsSerializer,
    ProductSubcategorySerializer,
    ProductCategorySerializer,
    ProductSizeSerializer,
)


class ProductsListView(ListAPIView):
    def get_queryset(self):

        queryset = (
            Products.objects.select_related("category", "size")
            .prefetch_related("gallery", "innovations", "video", "news")
            .all()
            .order_by("-date")
        )
        subcategory_id = self.request.query_params.get("subcategory", None)
        category_id = self.request.query_params.get("category", None)
        size_id = self.request.query_params.get("size", None)
        name = self.request.query_params.get("name", None)
        if subcategory_id:
            subcategory = ProductSubcategory.objects.get(id=subcategory_id)
            queryset = queryset.filter(subcategory=subcategory)

        if category_id:
            category = ProductCategory.objects.get(id=category_id)
            queryset = queryset.filter(category=category)

        if size_id:
            size = ProductSize.objects.get(id=size_id)
            queryset = queryset.filter(size=size)

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    serializer_class = ProductsSerializer
    pagination_class = StandardPagination


@api_view(["GET"])
@permission_classes([AllowAny])
def get_product_categories(request):
    categories = ProductCategory.objects.all().order_by("priority")
    serializer = ProductCategorySerializer(
        categories, many=True, context={"request": request}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_product_subcategories(request, id):
    category = ProductCategory.objects.get(id=id)
    subcategories = ProductSubcategory.objects.filter(category=category).order_by(
        "priority"
    )
    serializer = ProductSubcategorySerializer(
        subcategories, many=True, context={"request": request}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_sizes(request):
    sizes = ProductSize.objects.all()
    serializer = ProductSizeSerializer(sizes, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_exact_product(request, id):
    product = Products.objects.get(id=id)
    serialized_data = ProductsSerializer(product, context={"request": request})
    return Response(serialized_data.data, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.utils.encoding import smart_str
from django.db.models import Q
from .models import ProductDocumentations
from .serializers import ProductDocumentationsSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def files_list_view(request):
    """Get files with optional search by name and description"""
    queryset = ProductDocumentations.objects.filter(is_active=True).order_by(
        "-created_at"
    )

    name = request.query_params.get("name", None)
    description = request.query_params.get("description", None)
    search = request.query_params.get("search", None)

    # Unified search
    if search:
        search = smart_str(search).strip()
        print(f"Unified search for: '{search}'")
        queryset = queryset.filter(
            Q(name__icontains=search)
            | Q(description__icontains=search)
            | Q(name_en__icontains=search)
            | Q(name_tk__icontains=search)
        )
        print(f"Found: {queryset.count()} results")

    # Separate name search
    if name:
        name = smart_str(name).strip()
        print(f"Searching by name: '{name}'")
        queryset = queryset.filter(name__icontains=name)
        print(f"Found by name: {queryset.count()}")
        for item in queryset:
            print(f"  - {item.name}")

    # Separate description search
    if description:
        description = smart_str(description).strip()
        print(f"Searching by description: '{description}'")
        queryset = queryset.filter(description__icontains=description)
        print(f"Found by description: {queryset.count()}")

    # Serialize with request context
    serializer = ProductDocumentationsSerializer(
        queryset, many=True, context={"request": request}
    )

    print(f"Returning {len(serializer.data)} items")

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_file_detail(request, id):
    """Get single file by ID"""
    try:
        file = ProductDocumentations.objects.get(id=id, is_active=True)
        serializer = ProductDocumentationsSerializer(file, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ProductDocumentations.DoesNotExist:
        return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([AllowAny])
def download_file(request, id):
    """Download file by ID - supports all file types"""
    try:
        file_obj = ProductDocumentations.objects.get(id=id, is_active=True)

        if not file_obj.file:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Get the file path and original filename
        file_path = file_obj.file.path
        original_filename = os.path.basename(file_obj.file.name)

        # Check if file exists
        if not os.path.exists(file_path):
            return Response(
                {"error": "File does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        # Get the file extension
        file_extension = os.path.splitext(original_filename)[1].lower()

        # Set content type based on file extension
        content_type_map = {
            ".pdf": "application/pdf",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".doc": "application/msword",
            ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ".xls": "application/vnd.ms-excel",
            ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ".txt": "text/plain",
            ".zip": "application/zip",
            ".rar": "application/x-rar-compressed",
            ".mp4": "video/mp4",
            ".mp3": "audio/mpeg",
        }

        content_type = content_type_map.get(file_extension, "application/octet-stream")

        # Open and return the file with correct filename
        file_handle = open(file_path, "rb")
        response = FileResponse(file_handle, content_type=content_type)

        # Use the original filename from the uploaded file
        response["Content-Disposition"] = f'attachment; filename="{original_filename}"'
        response["Content-Length"] = file_obj.file.size
        response["X-File-Extension"] = file_extension

        return response

    except ProductDocumentations.DoesNotExist:
        return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
        return Response(
            {"error": "Error downloading file"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
