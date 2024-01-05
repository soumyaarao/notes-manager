import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser
from .models import Document

class DocumentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-registration')
        self.login_url = reverse('user-login')
        self.document_url = reverse('document-list')
        self.delete_url = reverse('delete-document')
        self.revert_url = reverse('revert-document')
        self.document_versions_url = reverse('document-versions', args=['Test Document'])
        self.switch_document_version_url = reverse('switch-document-version', args=['Test Document', 1])
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}
        self.document_data = {'title': 'Test Document', 'content': 'This is a test document.'}
        self.user_id = None

    def _create_user_and_login(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        login_response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)

        self.user_id = CustomUser.objects.get(username=self.user_data['username']).id

    def _create_dummy_document_with_other_role_id(self, times=1):
        user_data = {'username': 'dummy', 'password': 'dummy'}
        response = self.client.post(self.register_url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        login_response = self.client.post(self.login_url, user_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        uid = CustomUser.objects.get(username=user_data['username']).id
        self.document_data['user_id'] = uid
        for _ in range(times):
            _ = self.client.post(self.document_url, self.document_data, format='json')
        return uid


    def test_create_document(self):
        self._create_user_and_login()

        self.document_data['user_id'] = self.user_id
        response = self.client.post(self.document_url, self.document_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 1)

        self.assertEqual(Document.objects.get().title, 'Test Document')

    def test_get_document_list(self):
        self._create_user_and_login()

        self.document_data['user_id'] = self.user_id
        self.client.post(self.document_url, self.document_data, format='json')

        query_params = {'user_id': self.user_id, 'title': self.document_data['title']}

        response = self.client.get(self.document_url, data=query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.data)

        write_access = data["write_access"]
        content = data["content"]

        self.assertEqual(write_access, True)
        self.assertEqual(content, 'This is a test document.')

    def test_get_document_list_with_read_access(self):
        _ = self._create_dummy_document_with_other_role_id()
        self._create_user_and_login()

        query_params = {'user_id': self.user_id, 'title': self.document_data['title']}

        response = self.client.get(self.document_url, data=query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.data)

        write_access = data["write_access"]
        content = data["content"]

        self.assertEqual(write_access, False)
        self.assertEqual(content, 'This is a test document.')

    def test_get_document_versions(self):
        self._create_user_and_login()

        self.document_data['user_id'] = self.user_id
        response = self.client.post(self.document_url, self.document_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(self.switch_document_version_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(response.data['version'], 1)

    def test_get_all_document_versions(self):
        self._create_user_and_login()

        for version in range(1, 4):
            self.document_data['user_id'] = self.user_id
            response = self.client.post(self.document_url, self.document_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(self.document_versions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['message']), 3)

    def test_revert_version(self):
        # Twice to create 2 versions
        uid = self._create_dummy_document_with_other_role_id(times=2)
        data = self.document_data
        data['user_id'] = uid

        response = self.client.post(self.revert_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        docs = Document.objects.all()
        self.assertEqual(len(docs), 1)
        self.assertEqual(docs[0].version, 1)
        self.assertEqual(data['message'], 'Reverted successfully')


    def test_delete_documents(self):
        uid = self._create_dummy_document_with_other_role_id()
        data = self.document_data
        data['user_id'] = uid

        response = self.client.post(self.delete_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data


        self.assertEqual(len(Document.objects.all()), 0)
        self.assertEqual(data['message'], 'Deleted successfully')

