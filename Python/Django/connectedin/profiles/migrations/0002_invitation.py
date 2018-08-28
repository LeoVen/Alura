# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invited', models.ForeignKey(related_name='received_invitations', to='profiles.Profile')),
                ('requester', models.ForeignKey(related_name='sent_invitations', to='profiles.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
