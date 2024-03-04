from django.urls import path

from .views import RecipeListView, RecipeDetailView

app_name = 'ledger'

urlpatterns = [
    path('list', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
