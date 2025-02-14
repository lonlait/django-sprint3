from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        include(('blog.urls', 'blog'), namespace='main_blog')
    ),  # Уникальный namespace
    path(
        'pages/',
        include(('pages.urls', 'pages'), namespace='pages_app')
    ),
    path(
        'blog/',
        include(('blog.urls', 'blog'), namespace='blog_section')
    ),
]

