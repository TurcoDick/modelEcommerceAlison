
# coding=utf-8
# TestCase é uma classe de teste unitário
# o client simulo navegador
from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class IndexViewTestCase(TestCase):

    # este método é executado sempre que inicia um metódo
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    # este método é executado sempre que finaliza um metódo
    def tearDown(self):
        pass

    # testa se o acesso a pagina foi encontrado
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    # testa se o acesso ao template foi bem sucedido
    def test_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'index.html')