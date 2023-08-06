
from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI',views.PathogenicView)

urlpatterns = [
    #path('form/',views.myform, name="myform"),
    path('api/', include(router.urls)),
    # Redirect /predict/ to /api/MyAPI/predict/
    path('predict/', views.predictPathogenic)
]
