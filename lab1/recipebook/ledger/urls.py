from django.urls import path
from ledger.views import recipe_list

app_name = 'ledger'

urlpatterns = [
    path('list/', recipe_list, name='recipe_list'),
]