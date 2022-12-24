example = "EXAMPLE"
code = 228
from .models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["example"] = example
        context["code"] = code
        return context
