from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView, CreateView
from .models import CategoryModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# models.py, admin.py, views.py, urls.py

# def home_page(request):
#     return HttpResponse("<h1>Hello</h1>")
from products.models import ProductModel

from django.contrib.auth import login
from django.shortcuts import render, redirect

def login(request):
    return HttpResponse("Авторизация")



class RegisterUser(CreateView):
   form_class = UserCreationForm
   template_name = 'register.html'
   success_url = reverse_lazy('login')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = "Регистрация"
       return context





def index_page(request):
    # products = ProductModel.objects.all().filter(title__icontains="Iphone12")
    # products = ProductModel.objects.all().order_by('-id')

    return render(request, 'index.html', )


# def shop_page(request):
#     products = ProductModel.objects.all()
#     return render(request, 'shop.html', {'products': products})


class ShopPageView(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        category = self.request.GET.get('category')

        if q:
            qs = qs.filter(title__icontains=q)

        elif category:
            qs = qs.filter(category_id=category)

        return qs


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'





# context ={}
#
#     # add the dictionary during initialization
#     form = GeeksForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context['form']= form
#     return render(request, "create_view.html", context)
def send_form(request):
    context = {}

    form = FormModelForm(request.POST)
    if form.is_valid():
        form.save()

    context['blabla'] = form
    return render(request, 'forms.html', context)
