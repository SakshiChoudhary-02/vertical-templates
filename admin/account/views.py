from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from admin.account.forms import CategoryForm, UsersInfoForm, CardsForm
from admin.account.models import Category, UsersInfo, Cards


def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(request.POST)
            Category.objects.create(**form.cleaned_data)
            form.save()
            return HttpResponseRedirect('category/create.html')
    else:
        form = CategoryForm()
    return render(request, 'category/create.html', {'form': form})


class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')



class UserDetail(View):
    def get(self, request):
        # user_info = UsersInfo.objects.all()
        user_info = UsersInfoForm()
        return render(request, "userdetail.html", {'form': user_info})

    def post(self, request):
        user_info = UsersInfoForm(request.POST)
        if request.method == 'POST':
            if user_info.is_valid():
                user_info.save()
            #return render(request, 'userdetail.html', {'form': user_info})
            return render(request, 'card.html', {'form': user_info})


class Card(ListView):
    model = Cards
    template_name = 'card.html'
    context_object_name = 'card'


class CardDetail(DetailView):
    model = Cards
    template_name = 'carddetail.html'
    context_object_name = 'Cards'


# class CardDetail(DetailView):
#     def get(self, request):
#         cards = CardsForm()
#         return render(request, "carddetail.html", {'form': cards})
#
#     def post(self, request):
#         cards = CardsForm(request.POST)
#         if request.method == 'POST':
#             if cards.is_valid():
#                 cards.save()
#             return render(request, 'carddetail.html', {'form': cards})


class AddCard(CreateView):
    model = Cards
    template_name = 'addcard.html'
    fields = '__all__'


class EditCard(UpdateView):
    model = Cards
    template_name = 'editcard.html'


class DeleteCard(DeleteView):
    model = Cards
    template_name = 'deletecard.html'
    fields = '__all__'
    k_url_kwarg = 'pk'
    success_url = reverse_lazy('account:card')
