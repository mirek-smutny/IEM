# Generated by Django 3.0.8 on 2020-08-04 14:38

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackoutReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'blackout_reason',
            },
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('path', models.CharField(max_length=60)),
                ('command', models.CharField(max_length=60)),
                ('parameters', models.CharField(max_length=60, null=True)),
                ('env', models.CharField(max_length=300, null=True)),
            ],
            options={
                'db_table': 'command',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'component',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='IncidentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'incident_category',
            },
        ),
        migrations.CreateModel(
            name='IncidentPriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('level', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'incident_priority',
            },
        ),
        migrations.CreateModel(
            name='IncidentSLA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('resolve_time', models.IntegerField(null=True)),
                ('time_unit', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'incident_sla',
            },
        ),
        migrations.CreateModel(
            name='IncidentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'incident_status',
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric', models.CharField(max_length=40)),
                ('interval', models.CharField(max_length=40)),
                ('output_type', models.CharField(max_length=40)),
                ('warning_operator', models.CharField(max_length=40, null=True)),
                ('warning_threshold', models.CharField(max_length=40, null=True)),
                ('critical_operator', models.CharField(max_length=40, null=True)),
                ('critical_threshold', models.CharField(max_length=40, null=True)),
                ('occurence_limit', models.CharField(max_length=40, null=True)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Command')),
            ],
            options={
                'db_table': 'metric',
            },
        ),
        migrations.CreateModel(
            name='MetricCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'metric_category',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('host', models.CharField(max_length=60)),
                ('tcp_udp', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'target',
            },
        ),
        migrations.CreateModel(
            name='TargetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'target_type',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'template',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TemplateMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Metric')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Template')),
            ],
            options={
                'db_table': 'template_metric',
            },
        ),
        migrations.CreateModel(
            name='TargetTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Target')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Template')),
            ],
            options={
                'db_table': 'target_template',
            },
        ),
        migrations.CreateModel(
            name='TargetProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('value', models.CharField(max_length=200)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Target')),
            ],
            options={
                'db_table': 'target_property',
            },
        ),
        migrations.CreateModel(
            name='TargetMetricCollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=40)),
                ('collect_date', models.DateTimeField(verbose_name='collect date')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Metric')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Target')),
            ],
            options={
                'db_table': 'target_metric_collect',
            },
        ),
        migrations.CreateModel(
            name='TargetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Group')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Target')),
            ],
            options={
                'db_table': 'target_group',
            },
        ),
        migrations.CreateModel(
            name='TargetCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=200)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Target')),
            ],
            options={
                'db_table': 'target_credential',
            },
        ),
        migrations.AddField(
            model_name='target',
            name='target_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.TargetType'),
        ),
        migrations.AddField(
            model_name='metric',
            name='metric_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.MetricCategory'),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateTimeField(verbose_name='collect date')),
                ('notification_sent', models.BooleanField(null=True)),
                ('acknowledge', models.BooleanField(null=True)),
                ('last_update', models.DateTimeField(null=True, verbose_name='last update')),
                ('resolve_date', models.DateTimeField(null=True, verbose_name='resolve date')),
                ('close_date', models.DateTimeField(null=True, verbose_name='close date')),
                ('incident_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.IncidentCategory')),
                ('incident_priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IEMW.IncidentPriority')),
                ('incident_sla', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IEMW.IncidentSLA')),
                ('incident_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.IncidentStatus')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Metric')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Target')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'incident',
            },
        ),
        migrations.CreateModel(
            name='Blackout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(null=True, verbose_name='start date')),
                ('end_date', models.DateTimeField(null=True, verbose_name='end date')),
                ('blackout_reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.BlackoutReason')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IEMW.Target')),
            ],
            options={
                'db_table': 'blackout',
            },
        ),
    ]
