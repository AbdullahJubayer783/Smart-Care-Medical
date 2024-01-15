from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register('list',views.DoctorViewSet)
router.register('specialization',views.SpecializationViewSet)
router.register('available_time',views.AvailableTimeViewSet)
router.register('designation',views.DesignationViewSet)
router.register('reviews',views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]