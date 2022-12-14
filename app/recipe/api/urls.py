"""Url mappings for the recipe app."""


from django.urls import include, path
from recipe.api import views as api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("recipes", api_views.RecipeViewSet)
router.register("tags", api_views.TagViewSet)
router.register("ingredients", api_views.IngredientViewSet)
app_name = "recipe"

urlpatterns = [
    path("", include(router.urls)),
]
