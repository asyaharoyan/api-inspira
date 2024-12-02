from django.urls import path
from posts import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/style/', views.PostStyleChoice.as_view(), name='style_choices'),
    path('posts/area_type/', views.PostAreaChoice.as_view(), name='area_type_choices'),
]
