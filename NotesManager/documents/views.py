import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import CustomUser
from documents.models import Document
from .serializers import DocumentSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def document_list(request):
    if request.method == 'GET':
        data = request.query_params
        title = data.get("title")
        user_id = data.get('user_id')
        documents = Document.objects.filter(title=title).order_by('-version')
        if not documents:
            return Response(json.dumps({
                "write_access": False,
                "content": ''}),
                content_type="application/json")
        doc_admin = str(documents[0].author.id)
        if doc_admin == user_id:
            write_access = True
        else:
            write_access = False
        return Response(json.dumps({
            "write_access": write_access,
            "content": documents[0].content}),
            content_type="application/json")

    elif request.method == 'POST':
        user_id = request.data.get('user_id')
        title = request.data['title']
        content = request.data['content']
        user = get_object_or_404(CustomUser, pk=user_id)
        latest_version = Document.objects.filter(title=title).order_by('-version').first()
        latest_version = latest_version or 0
        Document.objects.create(author=user, title=title, content=content, version=latest_version.version + 1 if latest_version else 1)

        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def document_versions(request, title):
    docs = Document.objects.filter(title=title).order_by('-version')
    versions = [doc.version for doc in docs]
    return Response({'message': versions})

@api_view(['POST'])
def delete_document(request):
    data = request.data
    title = data.get("title")
    user_id = data.get('user_id')
    docs = Document.objects.filter(title=title)
    if not docs:
        return Response({'message': 'No document with title'}, status=status.HTTP_400_BAD_REQUEST)
    doc = docs[0]
    doc_admin = str(doc.author.id)
    if doc_admin == user_id:
        for doc in docs:
            doc.delete()
        return Response({'message': 'Deleted successfully'})
    return Response({'message': 'User is not admin of the document'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def revert_document(request):
    data = request.data
    title = data.get("title")
    user_id = data.get('user_id')
    docs = Document.objects.filter(title=title).order_by('-version')
    if not docs:
        return Response({'message': 'No document with title'}, status=status.HTTP_400_BAD_REQUEST)
    doc = docs[0]
    doc_admin = str(doc.author.id)
    if doc_admin == user_id:
        doc.delete()
        return Response({'message': 'Reverted successfully'})
    return Response({'message': 'User is not admin of the document'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def switch_document_version(request, title, version):
    document = Document.objects.filter(title=title, version=version).first()
    if document:
        serializer = DocumentSerializer(document)
        return Response(serializer.data)
    else:
        return Response({'message': 'Document version not found.'}, status=status.HTTP_404_NOT_FOUND)
