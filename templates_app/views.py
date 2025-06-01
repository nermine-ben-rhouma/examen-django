from rest_framework import viewsets
from .models import TemplateComponent
from .serializers import TemplateComponentSerializer
from django.http import HttpResponse
from django.template import Template, Context
from django.views import View
from .models import TemplateComponent
import json

class RenderComponentView(View):
    def get(self, request, pk):
        try:
            component = TemplateComponent.objects.get(pk=pk)
            schema_dict = component.schema
            template_string = component.html_template

            template = Template(template_string)
            context = Context(schema_dict)

            rendered = template.render(context)
            return HttpResponse(rendered)

        except TemplateComponent.DoesNotExist:
            return HttpResponse("Component not found", status=404)
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=500)


class TemplateComponentViewSet(viewsets.ModelViewSet):
    queryset = TemplateComponent.objects.all()
    serializer_class = TemplateComponentSerializer

# Create your views here.
