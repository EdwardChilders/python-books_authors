from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('view_book/<int:book_id>', views.view_book),
    path('add_book', views.add_book),
    path('add_auth_to_book', views.add_auth_to_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<int:auth_id>', views.view_auth),
    path('add_book_to_auth', views.add_book_to_auth),
]
