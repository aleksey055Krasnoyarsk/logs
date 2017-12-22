# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.utils import timezone
from .models import Logs
import logging



def logs(request):
	return render(request, 'logs/index.html', {})



def readlog(request):
	logger = logging.getLogger(__name__)
	logging.basicConfig(filename='logs/templates/logs/logs.html',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s \n')
	logging.error('Сообщение системы.\n')
	return render(request, 'logs/logs.html', {})
    
