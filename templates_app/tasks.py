from celery import shared_task
from django.template import Template, Context
from .models import TemplateComponent

@shared_task
def prerender_component(component_id):
    try:
        component = TemplateComponent.objects.get(pk=component_id)
        template = Template(component.html_template)
        context = Context(component.schema)
        rendered = template.render(context)

        component.rendered_html = rendered
        component.save()

    except Exception as e:
        print(f"Error in prerendering: {e}")

