from django.urls import path

from .views import HomeView, ListView, CreateView, DetailView, UpdateView, DeleteView, SearchView, ContactView, AboutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("list/", ListView.as_view(), name="list"),
    path("about/", AboutView.as_view(), name="about"),
    path("create/", CreateView.as_view(), name="create"),
    path("detail/<int:pk>/", DetailView.as_view(), name="detail"),
    path("update/<int:pk>/", UpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteView.as_view(), name="delete"),
    path("search/", SearchView.as_view(), name="search"),
    path("contact/", ContactView.as_view(), name="contact"),
]
