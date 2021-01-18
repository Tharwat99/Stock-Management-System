from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class StockmanagerConfig(AppConfig):
    name = 'StockManager'
    verbose_name = _('Stock Manager')
