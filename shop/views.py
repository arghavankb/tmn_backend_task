from rest_framework.viewsets import ModelViewSet
from .models import Product, ProductImage
from .permissions import AdminModifyAuthenticatedReadOnly
from .serializers import ProductSerializer, ProductImageSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related("images").all()
    serializer_class = ProductSerializer
    permission_classes = [AdminModifyAuthenticatedReadOnly]


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [AdminModifyAuthenticatedReadOnly]

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs["product_pk"])
