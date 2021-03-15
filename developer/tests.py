from django.test import TestCase
from .models import Developer
from django.urls import reverse

# Create your tests here.


class DevTestCase(TestCase):

    def setUp(self):
        Developer.objects.create(first_name="UwU", last_name="OwO")
    
    def test_is_free_with_no_tasks(self):
        """
         is_free() returns True for developer with no tasks.
        """
        #dev = Developer.objects.create(first_name="abc", last_name="def")
        dev = Developer.objects.get(first_name="UwU")
        self.assertIs(dev.is_free(), True)

    def test_is_free_with_one_tasks(self):
        """
        is_free() returns False for developer with at least one tasks.
        """
        #dev = Developer.objects.create(first_name="ghi",last_name="jkl")
        dev = Developer.objects.get(first_name="UwU")
        dev.tasks.create(title="cours Django", description="Faire le cours sur Django")
        self.assertIs(dev.is_free(), False)

class DeveloperIndexViewTests(TestCase):
    def test_no_developers(self):
        """
        If no developers exist, an appropriate message is displayed.
        """ 
        response = self.client.get(reverse('developer:index'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Il n'y a aucune dévelopeur enregistré!")
        self.assertQuerysetEqual(response.context['developers'], [])

    def test_one_developer(self):
        """
         A developer is displayed on the index page.
        """
        dev = Developer.objects.create(first_name="Jonathan", last_name="Lechien")
        response = self.client.get(reverse('developer:index'))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context['developers'],[f'<Developer: {dev.first_name} {dev.last_name}>'])
        self.assertContains(response, dev.first_name)

class DevDetailView(TestCase):
    def test_existing_developer(self):
        """
        The detail view of a developer displays the developer's text.
        """
        dev = Developer.objects.create(first_name="Jonathan", last_name="Lechien")
        url = reverse('developer:detail', args=(dev.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['developer'], dev)
        self.assertContains(response, dev.first_name)
        self.assertContains(response, dev.last_name)

    def test_non_existing_developer(self):
        """
        The detail view of a non existing developer should return 404 status_code response.
        """
        url = reverse('developer:detail', args=(1,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)