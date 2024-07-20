from django.urls import path
from .views import BookListView
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
]