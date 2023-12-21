from django.urls import path

from .views import UserViewSet, CodeGenerateViewSet, RegularUserViewSet, BranchListAPIView

urlpatterns = [
    path('user/', UserViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('user/<int:pk>/', UserViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),
    path('code/', CodeGenerateViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('code/<int:pk>/', CodeGenerateViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),
        path('regular/', RegularUserViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('regular/<int:pk>/', RegularUserViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),
    path('branches/', BranchListAPIView.as_view(), name='branch-list'),
 

]