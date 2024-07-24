from django.urls import path

from cinema import views

movie_list = views.MovieViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

movie_detail = views.MovieViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path(
        "genres/",
        views.GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        views.GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "actors/",
        views.ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        views.ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "cinema_halls/",
        views.CinemaHallViewSet.as_view(
            actions=
            {
                "get": "list",
                "post": "create"
            }
        ),
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        views.CinemaHallViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="cinema-hall-detail"
    ),
    path(
        "movies/",
        movie_list,
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        movie_detail,
        name="movie-detail"
    ),
]

app_name = "cinema"
