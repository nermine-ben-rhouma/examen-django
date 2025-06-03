from celery import shared_task
from django.template import Template, Context
from .models import TemplateComponent
from textblob import TextBlob

@shared_task
def generate_sentiment_component(text):
    sentiment = TextBlob(text).sentiment.polarity

    label = "Positif" if sentiment > 0 else "Négatif" if sentiment < 0 else "Neutre"
    
    TemplateComponent.objects.create(
        name=f"sentiment-{label}",
        schema={"label": label, "score": round(sentiment, 2)},
        html_template="<div>Sentiment: {{ label }} ({{ score }})</div>"
    )
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

