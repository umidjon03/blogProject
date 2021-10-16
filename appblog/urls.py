from django.urls import path
from .views import ( \
    BlogPostView,
    BlogDetailView,
    BlogPostCreateView,
    BlogEditView,
    BlogDeleteView,
)

urlpatterns = [
    path('', BlogPostView.as_view(), name='main'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path('post/create/', BlogPostCreateView.as_view(), name='creater'),
    path('post/<int:pk>/edit', BlogEditView.as_view(), name='update'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='deleter'),
]
