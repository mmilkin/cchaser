import unittest
from mock import patch, Mock
from chaser.forms import LoginForm


class FormTestCase(unittest.TestCase):

    @patch('chaser.forms.Form.validate')
    @patch('chaser.forms.User.query')
    def test_valid(self, query_user, validate):
        validate.return_value = True
        mock_user = Mock(name='mock_user')
        mock_user.verify_password.return_value = True

        form = LoginForm(csrf_enabled=False)
        form.name.data = 'Steve'
        query = Mock()
        query.first.return_value = mock_user

        query_user.filter_by.return_value = query

        self.assertTrue(form.validate())
        query_user.filter_by.assert_called_with(user_name='Steve')
        self.assertEqual(form.user, mock_user)

    @patch('chaser.forms.Form.validate')
    @patch('chaser.forms.User.query')
    def test_invalid_bad_password(self, query_user, validate):
        validate.return_value = True
        mock_user = Mock(name='mock_user')
        mock_user.verify_password.return_value = False

        form = LoginForm(csrf_enabled=False)
        form.name.data = 'Steve'
        query = Mock()
        query.first.return_value = mock_user

        query_user.filter_by.return_value = query

        self.assertFalse(form.validate())
        query_user.filter_by.assert_called_with(user_name='Steve')
        self.assertEqual(form.name.errors, ('Unknown username or password',))


    @patch('chaser.forms.Form.validate')
    @patch('chaser.forms.User.query')
    def test_invalid_no_user(self, query_user, validate):
        validate.return_value = True

        form = LoginForm(csrf_enabled=False)
        form.name.data = 'Steve'
        query = Mock()
        query.first.return_value = None

        query_user.filter_by.return_value = query

        self.assertFalse(form.validate())
        query_user.filter_by.assert_called_with(user_name='Steve')
        self.assertEqual(form.name.errors, ('Unknown username or password',))

    @patch('chaser.forms.Form.validate')
    def test_invalid_parent_form(self, validate):
        validate.return_value = False
        form = LoginForm(csrf_enabled=False)
        self.assertFalse(form.validate())
