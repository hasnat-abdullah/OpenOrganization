from django.shortcuts import HttpResponse
import os
from django.views import View
from logs.log import *


class LogView(View):
    '''
    To see desired dates log
    '''

    def get(self, request, date_n_type):

        if '.log' not in date_n_type:
            file_name= date_n_type+".log"
        else:
            file_name=date_n_type
        try:
            ROOT_DIR = os.path.abspath(os.path.dirname(__name__))  # This is your Project Root
            text = open(os.path.join(ROOT_DIR, 'log_files',file_name), 'r')
            #logger
            Log.info("Success| Data successfully returned.", request)
            return HttpResponse(text.read(),content_type="text/plain",)
        except Exception as ex:
            #logger
            Log.error("Error| File does not exist.", request)
            return HttpResponse("File does not exist.")


