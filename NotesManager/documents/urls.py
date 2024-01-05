from django.urls import path
from .views import document_list, document_versions, switch_document_version, revert_document, delete_document

urlpatterns = [
    path('documents/', document_list, name='document-list'),
    path('documents/delete', delete_document, name='delete-document'),
    path('documents/revertlatest', revert_document, name='revert-document'),
    path('documents/<str:title>/versions/', document_versions, name='document-versions'),
    path('documents/<str:title>/versions/<int:version>/', switch_document_version, name='switch-document-version'),
]
