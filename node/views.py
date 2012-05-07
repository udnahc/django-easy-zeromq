# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

from node.forms import CreateSocketForm

import simplejson
from zmq_utils.client import Client

def view_home_page(request, home_page_template):
    print "Home Page: Setting default project id as 1"
    project_id = 1
    from node.models import Project, Node
    project = Project.objects.get(id=project_id)
    nodes_list = Node.objects.filter(project_id=project_id)
    return render_to_response(home_page_template, locals())

def view_create_node(request, create_node_template):
    create_socket_form = CreateSocketForm()
    return render_to_response(create_node_template, locals())

def view_save_node(request):
    if request.method == 'POST':
        create_socket_form = CreateSocketForm(request.POST)
        if create_socket_form.is_valid():
            description = create_socket_form.cleaned_data['description']
            socket_name = create_socket_form.cleaned_data['socket_name']
            port = create_socket_form.cleaned_data['port']
            socket_type  = create_socket_form.cleaned_data['socket_type']
            python_package = create_socket_form.cleaned_data['python_package']
            values = {'description': description, 'socket_name': socket_name, 'port': port, 'socket_type': socket_type, 'python_package': python_package }
            # This has to be saved in the db
            return HttpResponse(simplejson.dumps(values))
        else:
            return HttpResponse(False)

def view_start_everything(request):
    ''' The web ui has sent a start signal '''
    client = Client()
    client.send_start_signal()    
    return HttpResponse(True)

def view_stop_everything(request):
    ''' The web ui has sent a stop signal '''
    from zmq_utils.client import Client
    client = Client()
    client.send_stop_signal()    
    print "Sent stop signal "
    return HttpResponse(True)

def view_start_processes(request):
    ''' The web ui has sent a start process signal'''
    client = Client()
    client.send_start_process_signal()    
    print "Sent start process signal "
    return HttpResponse(True)

def view_stop_processes(request):
    ''' The web ui has sent a stop all processes signal '''
    client = Client()
    client.send_stop_process_signal()    
    print "Sent stop process signal "
    return HttpResponse(True)

