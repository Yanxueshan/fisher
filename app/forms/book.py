from wtforms import StringField, IntegerField, Form
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    recipient_name = StringField(validators=[
        DataRequired(), Length(2, 20, message='收件人姓名长度必须在2至20个字符之间')])

    mobile = StringField(validators=[
        DataRequired(), Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号码')])
    message = StringField()
    address = StringField(validators=[
        DataRequired(), Length(10, 70, message='地址还不到10个字吗？请尽量写详细写吧')])
