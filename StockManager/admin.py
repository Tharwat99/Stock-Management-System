from django.contrib import admin
from .models import Stock, Category, StockHistory
from .forms import StockCreateForm

class StockInline(admin.TabularInline):
    model = Stock
    extra = 3

class StockAdmin(admin.ModelAdmin):
	list_display	 =  ['id', 'Item_name', 'Category','Price','Rating','Quantity','Added_by','Timestamp','Last_update']
	list_filter 	 =  ['Category','Rating','Added_by']
	search_fields 	 =  ['id', 'Category', 'Item_name']


class StockHistoryAdmin(admin.ModelAdmin):
	list_display	 =  ['id', 'Item_name','Price','Quantity','Receive_qty','Receive_by','Receive_from','Issue_qty','Issue_by','Issue_to','Timestamp','Last_update']
	list_filter 	 =  ['Item_name']
	search_fields 	 =  ['Category', 'Item_name']

class CategoryAdmin(admin.ModelAdmin):
	list_display	 =  ['id', 'Name','Rate', 'stock_count','Timestamp', 'Last_update']
	list_filter 	 =  ['Rate']
	search_fields 	 =  ['id', 'Name', 'Rate']
	inlines = [StockInline]
admin.site.register(Stock, StockAdmin)
admin.site.register(StockHistory, StockHistoryAdmin)
admin.site.register(Category, CategoryAdmin)