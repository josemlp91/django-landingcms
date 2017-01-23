import sys
import importlib

from models import *
from forms import *

class CMSContentManager(object):

    field_types = {
        'menu': 'MenuContent',
        'map': 'MapContent',
        'social': 'SocialContent',
        'title': 'TitleContent',
        'text': 'TextContent',
        'icon': 'IconContent',
        'link': 'LinkContent',
        'image': 'ImageContent',
        'admin': ''
    }

    field_form_class = {
        'menu': 'MenuContentForm',
        'map': 'MapContentForm',
        'social': 'SocialContentForm',
        'title': 'TitleContentForm',
        'text': 'TextContentForm',
        'icon': 'IconContentForm',
        'link': 'LinkContentForm',
        'image': 'ImageContentForm',
    }


    @staticmethod
    def get_content_class(type, field_types=field_types):

        try:
            classtype = field_types[type]
            cls = getattr(sys.modules[__name__], classtype)
            return cls
        except:
            print "No existe clase asosociada al contenido"

    @staticmethod
    def get_content_formclass(type, field_form_class=field_form_class):
        try:
            classtype = field_form_class[type]
            cls = getattr(sys.modules[__name__], classtype)
            return cls
        except:
            print "No existe formulario asosociada al contenido"


