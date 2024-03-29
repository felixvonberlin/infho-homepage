from django.urls import path

from blog import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.PostListView.as_view(), name="posts-page"),
    path('post/<slug:slug>/', views.SinglePostView.as_view(), 
         name='post-detail-page')
]
