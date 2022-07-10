from typing import Any
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self) -> dict[str, Any]:
        ctxt = super().get_context_data()
        ctxt["username"] = "eiji"
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self) -> dict[str, Any]:
        ctxt = super().get_context_data()
        ctxt["num_services"] = "{:,}".format(1234567)
        ctxt["skills"] = [
            "Python",
            "Javasctipt",
            "Go"
        ]
        return ctxt