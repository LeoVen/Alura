from django.db import models

# Create your models here.

class Profile(models.Model):

	name = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	phone = models.CharField(max_length=15, null=False)

	def invite(self, invited_profile):
		Invitation(requester=self, invited=invited_profile).save()


class Invitation(models.Model):

	requester = models.ForeignKey(Profile, related_name="sent_invitations")
	invited = models.ForeignKey(Profile, related_name="received_invitations")