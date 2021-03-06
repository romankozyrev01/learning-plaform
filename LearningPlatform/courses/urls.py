from django.urls import path, include
from rest_framework import routers

from .views import CoursesViewSet


app_name = 'courses'
router = routers.SimpleRouter()
router.register(r'', CoursesViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('<int:pk>/lessons/', include('lessons.urls')),
    path('quizes/', include('quizzes.urls'))
]
