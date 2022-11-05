from rest_framework.renderers import JSONRenderer


class CustomJsonRenderer(JSONRenderer):
    def get_indent(self, accepted_media_type, renderer_context):
        return 2
