# from django.shortcuts import render
from django.http import HttpResponse
import logging
from myapp.models import Order, Client, Product

logger = logging.getLogger(__name__)


def hello_world(requesr):
    logger.info("Visit page Hello world")
    return HttpResponse('Hello world')


def main(request):
    descryption_main =

    logger.info("Visit page main")
    return HttpResponse(descryption_main)


def about(request):
    about_descryption = '''
    <h2>Шаурма до рассвета,<br>
    выходила из Светы!!!</h2><br>
    '''
    logger.info("Visit page about")
    return HttpResponse(about_descryption)


def all_orders(request):
    order = Order.objects.all()
    return HttpResponse(order)