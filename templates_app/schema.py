import graphene
from graphene_django.types import DjangoObjectType
from .models import TemplateComponent

class TemplateComponentType(DjangoObjectType):
    class Meta:
        model = TemplateComponent

class Query(graphene.ObjectType):
    all_components = graphene.List(TemplateComponentType)

    def resolve_all_components(root, info):
        return TemplateComponent.objects.all()

schema = graphene.Schema(query=Query)
