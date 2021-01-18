from django.db import models
from django.utils.translation import gettext_lazy as _

class Stock(models.Model):
	Category       = models.ForeignKey('Category', on_delete = models.CASCADE,  blank = True, null = True, help_text=_('Category of this item.'), verbose_name=_('Category'))
	Item_name      = models.CharField(max_length = 50  , blank = False, null = True, help_text=_('Name of this item.'), verbose_name=_('Item name'))
	Quantity       = models.IntegerField(default = '0' , blank = False, null = True, help_text=_('Quantity of this item.'), verbose_name=_('Quantity'))
	Price		   = models.IntegerField(default = '0' , blank = False, null = True, help_text=_('Price of this item.'), verbose_name=_('Price'))
	Rating         = models.IntegerField(default = '0' , blank = False, null = True, help_text=_('Rating value of this item.'), verbose_name=_('Rating'))
	Added_by       = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person or Worker who added this item.'), verbose_name=_('Added by'))
	Receive_qty    = models.IntegerField(default = '0' , blank = True, null = True, help_text=_('The receive quantity of this item .'), verbose_name=_('Receive quantity'))
	Receive_by     = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person That receive quantity of this item.'), verbose_name=_('Receive by '))
	Receive_from   = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person or Place that receive item from.'), verbose_name=_('Receive from'))
	Issue_qty      = models.IntegerField(default = '0' , blank = True, null = True, help_text=_('The issue quantity of this item .'), verbose_name=_('Issue quantity'))
	Issue_by       = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person That issue quantity of this item.'), verbose_name=_('Issue by'))
	Issue_to	   = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person or Place that issue item to.'), verbose_name=_('Issue to'))
	Timestamp      = models.DateTimeField(auto_now_add = True, auto_now = False, help_text=_('Created Time of this item.'), verbose_name=_('Created Time'))	
	Last_update    = models.DateTimeField(auto_now_add = False, auto_now = True, help_text=_('Last update time of this item.'), verbose_name=_('Last update'))
	class Meta:
		verbose_name = _('stocks')
		verbose_name_plural = _('stocks')
	def __str__(self):
		return self.Item_name
class StockHistory(models.Model):
	Item_id		   = models.IntegerField( blank = False, null = True, help_text=_('Item id.'), verbose_name=_('Id'))
	Item_name      = models.CharField(max_length = 50  , blank = False, null = True, help_text=_('Name of this item.'), verbose_name=_('Item name'))
	Quantity       = models.IntegerField(default = '0' , blank = False, null = True, help_text=_('Quantity of this item.'), verbose_name=_('Quantity'))
	Price		   = models.IntegerField(default = '0' , blank = False, null = True, help_text=_('Price of this item.'), verbose_name=_('Price'))
	Receive_qty    = models.IntegerField(default = '0' , blank = True, null = True, help_text=_('The receive quantity of this item .'), verbose_name=_('Receive quantity'))
	Receive_by     = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person That receive quantity of this item.'), verbose_name=_('Receive by '))
	Receive_from   = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person or Place that receive item from.'), verbose_name=_('Receive from'))
	Issue_qty      = models.IntegerField(default = '0' , blank = True, null = True, help_text=_('The issue quantity of this item .'), verbose_name=_('Issue quantity'))
	Issue_by       = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person That issue quantity of this item.'), verbose_name=_('Issue by'))
	Issue_to	   = models.CharField(max_length = 50  , blank = True, null = True, help_text=_('Person or Place that issue item to.'), verbose_name=_('Issue to'))
	Timestamp      = models.DateTimeField(auto_now_add = True, auto_now = False, help_text=_('Created Time of this item.'), verbose_name=_('Created Time'))	
	Last_update    = models.DateTimeField(auto_now_add = False, auto_now = True, help_text=_('Last update time of this item.'), verbose_name=_('Last update'))
	class Meta:
		verbose_name = _('stocks history')
		verbose_name_plural = _('stocks history')
	def __str__(self):
		return self.Item_name
	
class Category(models.Model):	
	Name = models.CharField(max_length = 50  , blank = False, null = True, help_text=_('Category Name.'), verbose_name=_('Name'))
	Rate = models.IntegerField(default = '0' , blank = False, null = True, help_text=_('Category Rate.'), verbose_name=_('Rate'))
	Timestamp      = models.DateTimeField(auto_now_add = True, auto_now = False, help_text=_('Created Time of this item.'), verbose_name=_('Created Time'))	
	Last_update    = models.DateTimeField(auto_now_add = False, auto_now = True, help_text=_('Last update time of this item.'), verbose_name=_('Last update'))
	
	class Meta:
		verbose_name = _('Categories')
		verbose_name_plural = _('Categories')
	def stock_count(self):
		return self.stock_set.filter(Category_id = self.id).count()
	def __str__(self):
		return self.Name

	