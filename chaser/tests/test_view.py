import json
import unittest
from mock import patch, Mock
from chaser.controller import MotorInputError
from chaser.views import state, _game_control


class ViewsTestCase(unittest.TestCase):

    def setUp(self):
        from chaser import app
        self.client = app.test_client(use_cookies=True)

    @patch('chaser.views.controller')
    @patch('chaser.views.jsonify')
    def test_get_state(self, jsonify, controller):
        controller.state = 'OTHER'
        jsonify.return_value = '{"state": "OTHER"}'
        value = state()
        expected = {'state': 'OTHER'}
        self.assertEqual(value, (json.dumps(expected), 200))
        jsonify.assert_called_with(expected)

    @patch('chaser.views.controller')
    @patch('chaser.views.request')
    def test_game_control(self, request, controller):
        request.form = {'key': 'value'}
        response = _game_control()
        controller.motor.assert_called_with('value')
        self.assertEqual(response, ('', 200))

    @patch('chaser.views.controller')
    @patch('chaser.views.request')
    @patch('chaser.views.jsonify')
    def test_game_control_error(self, jsonify, request, controller):
        request.form = {'key': 'value'}
        controller.motor.side_effect = MotorInputError
        jsonify.return_value = '{"state": "OTHER"}'
        response = _game_control()
        self.assertEqual(response, ('{"state": "OTHER"}', 400))

    def test_login_get(self):
        result = self.client.get('/login')
        self.assertEqual(result.status_code, 200)
        self.assertTrue('login-form' in result.get_data())

    @patch('chaser.views.LoginForm')
    @patch('chaser.views.render_template')
    def test_login_post_invalid(self, render_template, MockLoginForm):
        form = Mock()
        form.validate_on_submit.return_value = False
        MockLoginForm.return_value = form
        render_template.return_value = '', 200

        self.client.post('/login', data={'name': 'red', 'password': 'dawn'})
        render_template.assert_called_with('login.html', title='Sign In', form=form)

    @patch('chaser.views.LoginForm')
    @patch('chaser.views.render_template')
    def test_login_post_valid(self, render_template, MockLoginForm):
        user = Mock()
        user.is_active.return_value = True
        user.get_id.return_value = 7
        form = Mock()
        form.validate_on_submit.return_value = True
        form.user = user
        MockLoginForm.return_value = form
        response = self.client.post('/login', data={'name': 'red', 'password': 'dawn'})
        self.assertEqual(response.status_code, 302)

