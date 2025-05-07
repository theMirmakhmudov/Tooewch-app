from django.urls import path
from .views import (
    PatientCreateAPIView,
    PatientListReadAPIView,
    PatientReadDetailAPIView
)

urlpatterns = [
    path('auth/user/create', PatientCreateAPIView.as_view(), name='patient-create'),
    path('auth/user/list', PatientListReadAPIView.as_view(), name='patient-list'),
    path('auth/user/<int:user_id>', PatientReadDetailAPIView.as_view(), name='patient-by-id')
]
