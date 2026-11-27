from django.db import models
from django.utils.translation import gettext_lazy as _

class Board(models.Model):
    if models.method == "GET":
        bno = models.AutoField('bno')
        btitle = models.CharField('btitle')
        bwriter = models.CharField('bwriter')
        bdate = models.DateTimeField(auto_now=True)
        bhit = models.IntegerField(_("조회수"),default=0)