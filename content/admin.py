from django.contrib import admin

from content.models import TitleContent, TextContent, LinkContent, ImageContent

admin.site.register(TitleContent)
admin.site.register(TextContent)
admin.site.register(LinkContent)
admin.site.register(ImageContent)