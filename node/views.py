# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

from node.forms import CreateSocketForm

import simplejson

def view_home_page(request, home_page_template):
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
