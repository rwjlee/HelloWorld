from django.urls import path
from . import views

app_name = 'bill_tracker'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_bill', views.add_bill, name = 'add_bill'),
    path('delete_bill/<int:bill_id>', views.delete_bill, name='delete_bill'),
    path('edit_page/<int:bill_id>', views.edit_page, name='edit_page'),
    path('edit_bill', views.edit_bill, name = 'edit_bill')
]