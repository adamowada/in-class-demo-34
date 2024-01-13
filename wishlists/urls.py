from django.urls import path
from .views import WishlistList, WishlistDetail


urlpatterns = [
    path('', WishlistList.as_view()),  # don't need the `name='wishlist_list'`
    path('<int:pk>/', WishlistDetail.as_view()),
]
