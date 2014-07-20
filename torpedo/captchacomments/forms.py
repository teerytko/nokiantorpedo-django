from django import forms
from django.contrib.comments.forms import CommentForm
from django.contrib.comments.models import Comment
from django.utils.translation import ungettext, ugettext, ugettext_lazy as _

from captcha.fields import CaptchaField


class CommentFormWithCaptcha(CommentForm):
    captcha = CaptchaField(label=_("Captcha"))

    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return Comment