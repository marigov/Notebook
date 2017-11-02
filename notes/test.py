# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import RequestFactory
from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateNoteForm,SignUpForm, NotesSearchForm
from random import randint

from notes.forms import CreateNoteForm
from .views import profile
import unittest
#from selenium import webdriver

class Tests(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def testLogin(self):

        response = self.client.post('/login/', self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, "/")


    def testNoLogin(self):
        self.wrongCredentials = {
            'username': 'test',
            'password': 'pass'}

        response = self.client.post('/login/', self.wrongCredentials, follow=False)

        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTrue(response.status_code == 200)

    def testInitialPage(self):
        request = self.factory.get('/')
        request.user = self.user

        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def testCreateNoteValid(self):
        form_data = {'title': '"Title', "content":"Content..."}
        form = CreateNoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def testCreateNoteInvalid(self):
        form_data = {'ti': '"Title', "co":"Content..."}
        form = CreateNoteForm(data=form_data)
        self.assertFalse(form.is_valid())

    def testCreateUserValid(self):

        form = SignUpForm({
            'username': "marigov",
            'first_name': "Miquel",
            'last_name': "Rigo",
            'password1': "miquel1234",
            'password2': "miquel1234",
            "email":"marigov@mac.com",
        })
        self.assertTrue(form.is_valid())

    def testCreateUserInvalid(self):

        form = SignUpForm({
            'username': "marigov",
            'first_name': "Miquel",
            'last_name': "Rigo",
            'password1': "miquel12334",
            'password2': "miquel1234",
            "email":"marigov@mac.com",
        })
        self.assertFalse(form.is_valid())

    def testUserAlreadyExists(self):
        self.credentials = {
            'username': 'johny',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        form = SignUpForm({
            'username': "johny",
            'first_name': "Miquel",
            'last_name': "Rigo",
            'password1': "miquel12334",
            'password2': "miquel1234",
            "email": "marigov@mac.com",
        })
        self.assertFalse(form.is_valid())



# class UserRegister(TestCase):
#
#     def setUp(self):
#         webdriver.driver = webdriver.PhantomJS()
#         webdriver.driver.set_window_size(1120, 550)
#         webdriver.driver.get("http://127.0.0.1:8000/signup/")
#
#     def test(self):
#         username = webdriver.driver.find_element_by_id("id_username")
#         first_name = webdriver.driver.find_element_by_id("id_first_name")
#         last_name = webdriver.driver.find_element_by_id("id_last_name")
#         email = webdriver.driver.find_element_by_id("id_email")
#         password_1 = webdriver.driver.find_element_by_id("id_password1")
#         password_2 = webdriver.driver.find_element_by_id("id_password2")
#
#         username.send_keys("username1234"+str(randint(0,1000)))
#         first_name.send_keys("Miquel")
#         last_name.send_keys("Rigo")
#         email.send_keys("marigov@mac.com")
#         password_1.send_keys("miquel1234.")
#         password_2.send_keys("miquel1234.")
#
#         webdriver.driver.find_element_by_id("id_submit").submit()
#         webdriver.driver.get("http://127.0.0.1:8000/")
#         self.assertEquals(webdriver.driver.current_url,"http://127.0.0.1:8000/")
#
#     def tearDown(self):
#
#         webdriver.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main()
