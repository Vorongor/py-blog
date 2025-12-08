from django import forms
from .models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "content": "Add your comment",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 1, "placehol-der": "Write a comment..."}
            ),
        }
