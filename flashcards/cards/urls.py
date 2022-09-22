from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.CardListViews.as_view(),
        name="card-list"),
    path(
        "novo",
        views.CardCreateView.as_view(),
        name="card-create"),
    path(
        "editar/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),
    path(
        "caixa/<int:num_caixa>",
        views.Caixas.as_view(),
        name="caixa"
    ),
]
