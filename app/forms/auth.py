from app.models.user import User

__author__ = 'larry'
__date__ = '2018/7/23 16:32'

from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError, EqualTo


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                        Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不能为空，请输入您的密码'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要2个字符，最多不超过10个字符')])

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('该昵称已被占用')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该电子邮箱已被注册')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                        Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不能为空，请输入您的密码'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度为6-32位字符'),
        EqualTo('password2', message='两次输入的密码不一样， 请重新输入')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])


class ChangePasswordForm(Form):
    old_password = PasswordField(validators=[
        DataRequired(), Length(6, 32)])
    new_password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度为6-32位字符'),
        EqualTo('new_password2', message='两次输入的密码不一样， 请重新输入')])
    new_password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])
