from loremipsum import generate_paragraph
from django.utils.text import Truncator

def generate_loremipsum(len):
    sentences_count, words_count, paragraph = generate_paragraph()
    return Truncator(paragraph).chars(len)

