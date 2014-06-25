from django_webtest import WebTest
from django.test import TestCase
from lottery.models import Ticket


class ModelTest(TestCase):
    fixtures = ['tickets']

    def test_tostring(self):
        a = Ticket.objects.all()
        self.assertEquals(1, a.count())
        self.assertEquals("123", str(a[0]))


class FrontTest(WebTest):
    fixtures = ['tickets']

    def _submit(self, number):
        index = self.app.get('/')
        form = index.forms[0]
        form['number'] = number
        page = form.submit()
        return page

    def test_won(self):
        page = self._submit('123')
        self.assertTrue('you won' in page.content, 'missing you won %s' % page)

    def test_not_won(self):
        page = self._submit('666')
        self.assertTrue('better luck' in page.content, 'missing better luck %s' % page)
