from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='create_author'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='view_author'),
    path('authors/<int:pk>/books/edit', views.AuthorBooksUpdateView.as_view(), name='update_authorbooks'),
]
