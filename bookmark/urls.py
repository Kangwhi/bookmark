from django.urls import path
from .views import *

urlpatterns = [
    # as_view는 클래스 뷰를 함수형 뷰로 변환
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'), # int: int에 한정되게 함 pk: primary key
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete')
]