from django.urls import path
from .views import *

urlpatterns = [
    path("", submitDataList.as_view(), name="pereval-list"),
    path("create/", submitDataCreate.as_view()),
    path("pereval/", UserPerevalList.as_view()),
    path("update-pereval/<int:pk>/", UserPerevalUpdate.as_view()),
    path("delete-pereval/<int:pk>/", UserPerevalDelete.as_view()),
    path("<slug:slug>/", submitDataDetail.as_view(), name="pereval-detail"),

]