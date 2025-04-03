from django.urls import path
from .views import EyewearListView, EyewearCreateView, EyewearDetailView, EyewearUpdateView, EyewearDeleteView

urlpatterns = [
    path('eyewear/', EyewearListView.as_view(), name='eyewear-list'),
    path('create/', EyewearCreateView.as_view(), name='eyewear-create'),
    path('detail/<int:pk>/', EyewearDetailView.as_view(), name='eyewear-detail'),
    path('update/<int:pk>/update/', EyewearUpdateView.as_view(), name='eyewear-update'),
    path('delete/<int:pk>/delete/', EyewearDeleteView.as_view(), name='eyewear-delete'),
]
