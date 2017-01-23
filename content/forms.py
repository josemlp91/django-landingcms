
from django.forms import ModelForm
from content.models import TitleContent, TextContent, LinkContent, ImageContent

class TitleContentForm(ModelForm):
    class Meta:
        model = TitleContent
        fields = ['content']

class TextContentForm(ModelForm):
    class Meta:
        model = TextContent
        fields = ['content']

class LinkContentForm(ModelForm):
    class Meta:
        model = LinkContent
        fields = ['url', 'description']

class ImageContentForm(ModelForm):
    class Meta:
        model = ImageContent
        fields = ['image', 'alt']