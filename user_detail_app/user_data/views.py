# from django.views import ListView
# from .models import UserData
# class UserDataListView(ListView):
#     model = UserData
#     template_name = 'home.html'
#     context_object_name='users'

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import UserData

class UserDataListView(ListView):
    model = UserData
    template_name = 'user_data_list.html'
    context_object_name = 'users'
class UserDataCreateView(CreateView):
    model = UserData
    template_name = 'user_data_form.html'
    fields = '__all__'
    success_url = reverse_lazy('user_data_list')

class UserDataUpdateView(UpdateView):
    model = UserData
    template_name = 'user_data_form.html'
    fields = '__all__'
    success_url = reverse_lazy('user_data_list')

class UserDataDeleteView(DeleteView):
    model = UserData
    template_name = 'user_data_confirm_delete.html'
    success_url = reverse_lazy('user_data_list')


