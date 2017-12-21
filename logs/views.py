from django.shortcuts import render
from django.utils import timezone
from .models import Logs
import logging



def logs(request):
	return render(request, 'logs/index.html', {})


logging.basicConfig(filename='log_filename.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')