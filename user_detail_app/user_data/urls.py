from .views import UserDataListView, UserDataCreateView, UserDataUpdateView, UserDataDeleteView
from django.urls import path
urlpatterns = [
    path('', UserDataListView.as_view(), name='user_data_list'),
    path('create/', UserDataCreateView.as_view(), name='user_data_create'),
    path('update/<int:pk>/', UserDataUpdateView.as_view(), name='user_data_update'),
    path('delete/<int:pk>/', UserDataDeleteView.as_view(), name='user_data_delete'),
]

