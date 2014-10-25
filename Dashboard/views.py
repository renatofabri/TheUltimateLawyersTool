'''
Created on Oct 18, 2014

@author: renato
'''
from django.shortcuts import render_to_response
from Common.Templates import DASHBOARD_HOME
from TheUltimateLawyersTool.settings import PAGE_TITLE
from django.template.context import RequestContext
from CourtService.TJSP import TJSP

VIEW_NAME = 'Dashboard'

def home(request):

    tjsp = TJSP()
    complete_page = tjsp.getLawsuitById('2014', '1')

    data = {'title': PAGE_TITLE % VIEW_NAME,
            'content': complete_page.text}

    return render_to_response(DASHBOARD_HOME, data, context_instance=RequestContext(request))
