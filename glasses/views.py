from rest_framework import generics
from .models import Eyewear
from .serializers import EyewearSerializer

class EyewearListView(generics.ListAPIView):
    queryset = Eyewear.objects.all()
    serializer_class = EyewearSerializer

class EyewearCreateView(generics.CreateAPIView):
    queryset = Eyewear.objects.all()
    serializer_class = EyewearSerializer

class EyewearDetailView(generics.RetrieveAPIView):
    queryset = Eyewear.objects.all()
    serializer_class = EyewearSerializer

class EyewearUpdateView(generics.UpdateAPIView):
    queryset = Eyewear.objects.all()
    serializer_class = EyewearSerializer

class EyewearDeleteView(generics.DestroyAPIView):
    queryset = Eyewear.objects.all()
    serializer_class = EyewearSerializer









# from django.shortcuts import render, get_object_or_404, redirect
# from django.views import View
# from django.db.models import Q
# from .models import Eyewear
# from .forms import EyewearForm, ContactForm
# from .forms import ContactForm
# from django.core.paginator import Paginator
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
#
# class HomeView(View):
#     def get(self, request):
#         return render(request, "home.html")
#
# from django.views import View
# from django.shortcuts import render
#
# class AboutView(View):
#     def get(self, request):
#         return render(request, "about.html")
#
#
# class ListView(View):
#     def get(self, request):
#         glasses = Eyewear.objects.all()
#         paginator = Paginator(glasses, 2)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#         return render(request, "list.html", {"page_obj": page_obj})
#
# class CreateView(View):
#     def get(self, request):
#         form = EyewearForm()
#         return render(request, "create.html", {"form": form})
#
#     def post(self, request):
#         form = EyewearForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("list")
#         return render(request, "create.html", {"form": form})
#
# class UpdateView(View):
#     def get(self, request, pk):
#         glass = get_object_or_404(Eyewear, id=pk)
#         form = EyewearForm(instace=glass)
#         return render(request, 'update.html', {'glass': glass, 'form': form})
#
#     def post(self, request, pk):
#         glass = get_object_or_404(Eyewear, id=pk)
#         form = EyewearForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('list')
#         return render(request, 'update.html', {'glass': glass, 'form': form})
#
#
# class DetailView(View):
#     def get(self, request, pk):
#         glass = get_object_or_404(Eyewear, id=pk)
#         return render(request, 'details.html', {'glass': glass})
#
#     def post(self, request, pk):
#         glass = get_object_or_404(Eyewear, id=pk)
#         form = EyewearForm(request.POST, instance=glass)
#         if form.is_valid():
#             form.save()
#             return redirect('detail', pk=glass.id)
#         return render(request, 'update.html', {'glass':glass, 'form':form})
#
# class DeleteView(View):
#     def get(self, request, pk):
#         glass = get_object_or_404(Eyewear, id=pk)
#         return render(request, 'delete.html', {'glass':glass})
#
#     def post(self, request, pk):
#         glass = Eyewear.objects.filter(id=pk)
#         if glass:
#             glass.delete()
#         return redirect('list')
#
#
# class SearchView(View):
#     def get(self, request):
#         query = request.GET.get('q', '')
#         glasses = Eyewear.objects.filter(Q(name__icontains=query) | Q(brand__icontains=query) | Q(price__icontains=query )) if query else Eyewear.objects.all()
#
#         return render(request, 'search.html', {'glasses': glasses, 'query': query})
#
# class ContactView(View):
#     def get(self, request):
#         form = ContactForm()
#         return render(request, "contact.html", {'form': form})
#
#     def post(self, request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone_number = form.cleaned_data['phone_number']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             return redirect('home')
#         return render(request, "contact.html", {'form': form})
#
#
#
