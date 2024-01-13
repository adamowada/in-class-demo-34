# Instead of using vanilla django views, use DRF views for our API
from rest_framework import generics
from .serializers import WishlistSerializer
from .models import Wishlist
from .permissions import IsOwnerOrReadOnly


# have a list view
class WishlistList(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()  # gets all the Wishlists
    serializer_class = WishlistSerializer


# have a detail view
class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly,]
    queryset = Wishlist.objects.all()  # gets all the Wishlists
    serializer_class = WishlistSerializer
