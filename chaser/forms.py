from flask.ext.wtf import Form
from wtforms import PasswordField, TextField
from wtforms.validators import Required
from models import User


class LoginForm(Form):
    name = TextField('name', validators=[Required()])
    password = PasswordField('password', validators=[Required()])

    def get_user(self):
        return User.query.filter_by(
            user_name=self.name.data,
        ).first()

    def validate(self):
        rv = Form.validate(self)

        if not rv:
            return False

        user = self.get_user()

        if user is None or not user.verify_password(self.password.data):
            self.name.errors += ('Unknown username or password',)
            return False

        self.user = user
        return True
