# from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def hello_world(requesr):
    logger.info("Visit page Hello world")
    return HttpResponse('Hello world')


def main(request):
    descryption_main = "Вот так вот"
    logger.info("Visit page main")
    return HttpResponse(descryption_main)


def about(request):
    about_descryption = '''
    <h2>Светит биполярная звездаааааа,<br>
    снова мне то хорошо то плохо,<br>
    выпиваю антидипрессант, чтоб не слышать хохот через слезы,<br>
    надежда, что лди умрут и воскреснут,<br>
    снова, не снова, надоело, не надоело...<br>
    </h2><br>
    '''
    logger.info("Visit page about")
    return HttpResponse(about_descryption)