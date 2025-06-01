from django.db import models

class TemplateComponent(models.Model):
    name = models.CharField(max_length=100, unique=True)
    schema = models.JSONField()
    html_template = models.TextField()
    rendered_html = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
