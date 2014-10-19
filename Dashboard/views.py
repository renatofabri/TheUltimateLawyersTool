'''
Created on Oct 18, 2014

@author: renato
'''
from django.shortcuts import render_to_response
from Common.Templates import DASHBOARD_HOME
from TheUltimateLawyersTool.settings import PAGE_TITLE
from django.template.context import RequestContext

VIEW_NAME = 'Dashboard'

def home(request):

    data = {'title': PAGE_TITLE % VIEW_NAME,}

    return render_to_response(DASHBOARD_HOME, data, context_instance=RequestContext(request))


if __name__ == '__main__':
    print "lol"