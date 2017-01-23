from __future__ import unicode_literals

from django.db import models
from django.utils.text import Truncator
from loremipsum import generate_paragraph
from singleton_models.models import SingletonModel

from content.models import TextContent, ImageContent, TitleContent, LinkContent, IconContent


class Menu(models.Model):
    descripcion = models.CharField(max_length=255)
    url = models.URLField()

class Configuracion(models.Model):
    favicon = models.ImageField()


class PaginaHome(models.Model):
    texto1_logo = models.OneToOneField(TitleContent, null=True, related_name='texto1logo')
    texto1_banner = models.OneToOneField(TitleContent, null=True, related_name='texto1banner')
    boton1_enlace = models.OneToOneField(LinkContent, blank=True, null=True, related_name='boton1enlace')
    boton1_texto = models.OneToOneField(TitleContent, blank=True, null=True, related_name='boton1texto')
    #
    highlights1_icon = models.OneToOneField(IconContent, blank=True, null=True, related_name='highlights1icon')
    highlights1_titulo = models.OneToOneField(TitleContent, blank=True, null=True, related_name='highlights1titulo')
    highlights1_texto = models.OneToOneField(TextContent, blank=True, null=True, related_name='highlights1texto')
    #
    main_imagen = models.OneToOneField(ImageContent, blank=True, null=True, related_name='mainimage')

    highlights2_icon = models.OneToOneField(IconContent, blank=True, null=True, related_name='highlights2icon')
    highlights2_titulo = models.OneToOneField(TitleContent, blank=True, null=True, related_name='highlights2titulo')
    highlights2_texto = models.OneToOneField(TextContent, blank=True, null=True, related_name='highlights2texto')

    highlights3_icon = models.OneToOneField(IconContent, blank=True, null=True, related_name='highlights3icon')
    highlights3_titulo = models.OneToOneField(TitleContent, blank=True, null=True, related_name='highlights3titulo')
    highlights3_texto = models.OneToOneField(TextContent, blank=True, null=True, related_name='highlights3texto')

    posts1_imagen = models.OneToOneField(ImageContent, blank=True, null=True, related_name='posts1_imagen')
    posts1_titulo = models.OneToOneField(TitleContent, blank=True, null=True, related_name='posts1_titulo')
    posts1_texto = models.OneToOneField(TextContent, blank=True, null=True, related_name='posts1_texto')

    posts2_imagen = models.OneToOneField(ImageContent, blank=True, null=True, related_name='posts2_imagen')
    posts2_titulo = models.OneToOneField(TitleContent, blank=True, null=True, related_name='posts2_titulo')
    posts2_texto = models.OneToOneField(TextContent, blank=True, null=True, related_name='posts2_texto')

    posts3_imagen = models.OneToOneField(ImageContent, blank=True, null=True, related_name='posts3_imagen')
    posts3_titulo = models.OneToOneField(TitleContent, blank=True, null=True, related_name='posts3_titulo')
    posts3_texto = models.OneToOneField(TextContent, blank=True, null=True, related_name='posts3_texto')

    posts4_imagen = models.OneToOneField(ImageContent, blank=True, null=True, related_name='posts4_imagen')
    posts4_titulo = models.OneToOneField(TitleContent, blank=True, null=True, related_name='posts4_titulo')
    posts4_texto = models.OneToOneField(TextContent, blank=True, null=True, related_name='posts4_texto')

    giganticheading_titulo_grande = models.OneToOneField(TitleContent, blank=True, null=True, related_name='giganticheadingtitulogrande')
    giganticheading_titulo_pequeno = models.OneToOneField(TitleContent, blank=True, null=True, related_name='giganticheadingtitulopequeno')

    CTA_titulo = models.OneToOneField(TitleContent, blank=True, null=True, related_name='CTAtitulo')
    CTA_enlace = models.OneToOneField(LinkContent, blank=True, null=True, related_name='CTAurl')
    CTA_texto = models.OneToOneField(TextContent, blank=True, null=True, related_name='CTAtext')

    def save(self, *args, **kwargs):
        if not self.id:

            titlecontent = TitleContent()
            linkcontent = LinkContent()
            iconcontent = IconContent()
            textcontent = TextContent()
            imagecontent = ImageContent()

            self.texto1_logo = titlecontent.generate_random_field('texto1_logo')
            self.texto1_banner = titlecontent.generate_random_field('texto1_banner')

            self.main_imagen = imagecontent.generate_random_field('main_imagen')
            self.boton1_enlace = linkcontent.generate_random_field('boton1_enlace')
            self.boton1_texto = titlecontent.generate_random_field('boton1_texto')

            self.highlights1_icon = iconcontent.generate_random_field('highlights1_icon')
            self.highlights1_titulo = titlecontent.generate_random_field('highlights1_titulo')
            self.highlights1_texto = textcontent.generate_random_field('highlights1_texto')

            self.highlights2_icon = iconcontent.generate_random_field('highlights2_icon')
            self.highlights2_titulo = titlecontent.generate_random_field('highlights2_titulo')
            self.highlights2_texto = textcontent.generate_random_field('highlights2_texto')

            self.highlights3_icon = iconcontent.generate_random_field('highlights3_icon')
            self.highlights3_titulo = titlecontent.generate_random_field('highlights3_titulo')
            self.highlights3_texto = textcontent.generate_random_field('highlights3_texto')

            self.giganticheading_titulo_grande = titlecontent.generate_random_field('giganticheading_titulo_grande')
            self.giganticheading_titulo_pequeno = titlecontent.generate_random_field('giganticheading_titulo_pequeno')

            self.posts1_imagen = imagecontent.generate_random_field('posts1_imagen')
            self.posts1_titulo = titlecontent.generate_random_field('posts1_titulo')
            self.posts1_texto = textcontent.generate_random_field('posts1_texto')

            self.posts2_imagen = imagecontent.generate_random_field('posts2_imagen')
            self.posts2_titulo = titlecontent.generate_random_field('posts2_titulo')
            self.posts2_texto = textcontent.generate_random_field('posts2_texto')

            self.posts3_imagen = imagecontent.generate_random_field('posts3_imagen')
            self.posts3_titulo = titlecontent.generate_random_field('posts3_titulo')
            self.posts3_texto = textcontent.generate_random_field('posts3_texto')

            self.posts4_imagen = imagecontent.generate_random_field('posts4_imagen')
            self.posts4_titulo = titlecontent.generate_random_field('posts4_titulo')
            self.posts4_texto = textcontent.generate_random_field('posts4_texto')

            self.CTA_titulo = titlecontent.generate_random_field('CTA_titulo')
            self.CTA_enlace = linkcontent.generate_random_field('CTA_enlace')
            self.CTA_texto = textcontent.generate_random_field('CTA_texto')

        super(PaginaHome, self).save(*args, **kwargs)

