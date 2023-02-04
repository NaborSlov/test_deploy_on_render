from django.urls import path

from framework.views import FrameworkListView, FrameworkListLanguageView

urlpatterns = [
    path("", FrameworkListView.as_view()),
    path("<str:language>/", FrameworkListLanguageView.as_view()),
]
