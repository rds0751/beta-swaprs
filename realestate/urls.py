from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', include('pages.urls')),
path('accounts/', include('allauth.urls')),
path('admin/', admin.site.urls),

path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
path('ckeditor/', include('ckeditor_uploader.urls')),

# path('lib/', src.profiles.views.library, name='library'),
path('products/', include('src.products.urls')),
path('cart/', include('src.cart.urls')),
path('', include('comments.urls')),
path('', include('log.urls')),
path('', include('news.urls')),
# path('', include('registr.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)