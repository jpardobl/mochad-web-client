from django.db import models


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=4)
    cmds = models.ManyToManyField("X10Command")

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.address)


class X10Command(models.Model):
    name = models.CharField(max_length=20)
    cmd_line = models.CharField(max_length=20)

