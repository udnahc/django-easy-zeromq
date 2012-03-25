from django.contrib import admin
from node.models import Project
from node.models import Node
from node.models import MasterLog

admin.site.register(Project)
admin.site.register(Node)
admin.site.register(MasterLog)
