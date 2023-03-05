import uuid

from django.utils.text import slugify


def unique_slug_gen(instance, model):
    slug = slugify(instance.name + str(uuid.uuid4()))

    while model.objects.filter(slug=slug).exists():
        slug = slugify(instance.name + str(uuid.uuid4()))
    return slug
