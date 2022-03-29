from os import stat
from django.conf import settings
from django.conf.urls.static import static
from unicodedata import name
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from posts import views
from .sitemaps import CategorySitemap, PostSitemap

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt',views.robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name="post_detail"),
    path('<slug:slug>/', views.category, name="category_detail"),
]   + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
