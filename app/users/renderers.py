from rest_framework import renderers
import json
from django.core.serializers.json import DjangoJSONEncoder

class UserRenderer(renderers.JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ""
        if "ErrorDetail" in str(data):
            response = json.dumps({"errors": data},cls=DjangoJSONEncoder)
        else:
            response = json.dumps(data,cls=DjangoJSONEncoder)

        return response
