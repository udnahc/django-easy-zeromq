from django.db import models

# Create your models here.

class ProjectManager(models.Manager):
    pass

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    objects = ProjectManager()

    def __str__(self):
        return self.name
    
class NodeManager(models.Manager):
    pass

class Node(models.Model):
    project_id = models.ForeignKey(Project, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    socket_type = models.CharField(max_length=50, null=False)
    connects_to = models.CharField(max_length=100)
    binds_to = models.CharField(max_length=100)
    worker_file = models.CharField(max_length=100, null=False)
    objects = NodeManager()

    def __str__(self):
        return "%s for (%s)" % (self.name, self.project_id.name)


class MasterLog(models.Model):
    project = models.ForeignKey(Project, null=False)
    node = models.ForeignKey(Node, null=False)
    log_message = models.TextField(null=False)

    def __str__(self):
        return "(%s:%s:%s):%s" % (self.project.name, self.node.name,self.node, self.node.connects_to, self.log_message)
