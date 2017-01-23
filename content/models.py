from django.db import models
from content.utils import generate_loremipsum

class FieldContent(models.Model):
    fieldname = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        abstract = True

class MenuContent(FieldContent):
    pass

class MapContent(FieldContent):
    pass

class SocialContent(FieldContent):
    twiter = models.URLField()
    facebook = models.URLField()
    googleplus = models.URLField()
    linkedin = models.URLField()


class TitleContent(FieldContent):
    content = models.CharField(null=False, blank=False, max_length=255)

    def generate_random_field(self, fieldname):
        content = generate_loremipsum(25)
        field = TitleContent(fieldname=fieldname, content=content)
        field.save()
        return field


class TextContent(FieldContent):
    content = models.TextField()

    def generate_random_field(self, fieldname):
        content = generate_loremipsum(60)
        field = TextContent(fieldname=fieldname, content=content)
        field.save()
        return field


class IconContent(FieldContent):
    icon = models.CharField(max_length=50)

    def generate_random_field(self, fieldname):
        description = generate_loremipsum(10)
        icon = "fa-paper-plane"
        field = IconContent(fieldname=fieldname, icon=icon)
        field.save()
        return field

class LinkContent(FieldContent):
    description = models.CharField(max_length=255, null=False, blank=True)
    url = models.URLField(max_length=255, null=False, blank=False)

    def generate_random_field(self, fieldname):
        description = generate_loremipsum(10)
        url = "http://www.loremipsum.com"
        field = LinkContent(fieldname=fieldname, url=url, description=description)
        field.save()
        return field


class ImageContent(FieldContent):
    image = models.FileField(null=True, blank=True, upload_to='.')
    alt = models.CharField(null=True, blank=True, max_length=255)

    def generate_random_field(self, fieldname):
        alt = generate_loremipsum(5)
        field = ImageContent(fieldname=fieldname, alt=alt)
        field.save()
        return field


