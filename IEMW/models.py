from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Component(models.Model):
    component = models.CharField(max_length = 40)
    class Meta:
        db_table = "component"

# User Management

class User(AbstractUser):
    class Meta:
        db_table = "user"
    pass

# Target Management

class Group(models.Model):
    name = models.CharField(max_length = 40)
    class Meta:
        db_table = "group"

class TargetType(models.Model):
    name = models.CharField(max_length = 40)
    class Meta:
        db_table = "target_type"

class Target(models.Model):
    name = models.CharField(max_length = 60)
    target_type = models.ForeignKey(TargetType, on_delete = models.CASCADE)
    host = models.CharField(max_length = 60)
    port = models.IntegerField
    tcp_udp = models.CharField(max_length = 3)
    class Meta:
        db_table = "target"

class TargetGroup(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    class Meta:
        db_table = "target_group"

class TargetCredential(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    user = models.CharField(max_length = 40)
    password = models.CharField(max_length = 200)
    class Meta:
        db_table = "target_credential"
        
class TargetProperty(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    name = models.CharField(max_length = 40)
    value = models.CharField(max_length = 200)
    class Meta:
        db_table = "target_property"

# Blackout Management

class BlackoutReason(models.Model):
    name = models.CharField(max_length = 60)
    class Meta:
        db_table = "blackout_reason"

class Blackout(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    start_date = models.DateTimeField('start date', null=True)
    end_date = models.DateTimeField('end date', null=True)
    blackout_reason = models.ForeignKey(BlackoutReason, on_delete=models.CASCADE)
    class Meta:
        db_table = "blackout"

# Metric Management

class MetricCategory(models.Model):
    name = models.CharField(max_length = 40)
    class Meta:
        db_table = "metric_category"

class Command(models.Model):
    name = models.CharField(max_length = 60)
    path = models.CharField(max_length = 60)
    command = models.CharField(max_length = 60)
    parameters = models.CharField(max_length = 60, null=True)
    env = models.CharField(max_length = 300, null=True)
    class Meta:
        db_table = "command"

class Metric(models.Model):
    metric_category = models.ForeignKey(MetricCategory, on_delete=models.CASCADE)
    metric = models.CharField(max_length = 40)
    interval = models.CharField(max_length = 40)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    output_type = models.CharField(max_length = 40)
    warning_operator = models.CharField(max_length = 40, null=True)
    warning_threshold = models.CharField(max_length = 40, null=True)
    critical_operator = models.CharField(max_length = 40, null=True)
    critical_threshold = models.CharField(max_length = 40, null=True)
    occurence_limit = models.CharField(max_length = 40, null=True)
    class Meta:
        db_table = "metric"

class TargetMetricCollect(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    value = models.CharField(max_length = 40)
    collect_date = models.DateTimeField('collect date')
    class Meta:
        db_table = "target_metric_collect"

# Template Management

class Template(models.Model):
    name = models.CharField(max_length = 40)
    class Meta:
        db_table = "template"

class TemplateMetric(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    class Meta:
        db_table = "template_metric"

class TargetTemplate(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    class Meta:
        db_table = "target_template"

# Incident Management
class IncidentStatus(models.Model):
    name = models.CharField(max_length = 40)
    class Meta:
        db_table = "incident_status"

class IncidentPriority(models.Model):
    name = models.CharField(max_length = 40)
    level = models.IntegerField(null=True)
    class Meta:
        db_table = "incident_priority"
        
class IncidentSLA(models.Model):
    name = models.CharField(max_length = 40)
    resolve_time = models.IntegerField(null=True)
    time_unit = models.CharField(max_length = 10, null=True)
    class Meta:
        db_table = "incident_sla"

class IncidentCategory(models.Model):
    category = models.CharField(max_length = 40)
    class Meta:
        db_table = "incident_category"
        
class Incident(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    incident_category = models.ForeignKey(IncidentCategory, on_delete=models.CASCADE)
    open_date = models.DateTimeField('collect date')
    incident_sla = models.ForeignKey(IncidentSLA, on_delete=models.CASCADE, null=True) 
    incident_status = models.ForeignKey(IncidentStatus, on_delete=models.CASCADE) 
    notification_sent = models.BooleanField(null=True)
    incident_priority = models.ForeignKey(IncidentPriority, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    acknowledge = models.BooleanField(null=True)
    last_update = models.DateTimeField('last update', null=True)
    resolve_date = models.DateTimeField('resolve date', null=True)
    close_date = models.DateTimeField('close date', null=True)
    class Meta:
        db_table = "incident"
    
