from django import forms
from .models import Stock, StockHistory, Category
from django.utils.translation import gettext_lazy as _
import string
class StockCreateForm(forms.ModelForm):
	class Meta:
		model  = Stock
		fields = ['Category', 'Item_name', 'Quantity', 'Price']
		labels = {
        	"Category": _('Category'),
            'Item_name': _('Item name'),
            'Quantity' : _('Quantity'),
            'Price' : _('Price')
        }
	Item_name  = forms.CharField(required  = False,label  = _('Item name'),help_text=_('Name of this item.') ,widget = forms.TextInput(attrs = {'autocomplete':'off'}))
	def clean_Category(self):
		Category = self.cleaned_data.get('Category')
		if not	Category :
			raise forms.ValidationError(_('This field is required'))	
		return Category
	def clean_Item_name(self):
		Item_name = self.cleaned_data.get('Item_name')
		if not Item_name :
			raise forms.ValidationError(_('This field is required'))
		obj = Stock.objects.filter(Item_name__icontains = Item_name)
		if obj :
			raise forms.ValidationError(_('This stock is already created'))	
		if Item_name.isdigit():
			raise forms.ValidationError(_('This field allowed string values'))	
		return Item_name
	def clean_Quantity(self):
		Quantity = self.cleaned_data.get('Quantity')
		if not	Quantity :
			raise forms.ValidationError(_('This field is required'))
		if Quantity <  0: 
			raise forms.ValidationError(_('This field allowed integer number values'))	
		return Quantity
	def clean_Price(self):
		Price = self.cleaned_data.get('Price')
		if not	Price :
			raise forms.ValidationError(_('This field is required'))
		if Price <  0: 
			raise forms.ValidationError(_('This field allowed integer number values'))	
		return Price

class CatCreateForm	(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['Name']
		labels = {
        	"Name": _('Name'),
        }
	def clean_Name(self):
		Name = self.cleaned_data.get('Name')
		if not Name :
			raise forms.ValidationError(_('This field is required'))
		obj = Category.objects.filter(Name__icontains = Name)
		if obj :	
			raise forms.ValidationError(_('This category is already created'))	
		if Name.isdigit():
			raise forms.ValidationError(_('This field allowed string values'))
		return Name		

class StockSearchForm(forms.ModelForm):
	class Meta:		
		model  = Stock
		fields = ['Category','Item_name','Start_date','End_date','Export_to_csv']

	Item_name  = forms.CharField(required  = False,label  = _('Item name'),help_text=_('Name of this item.') ,widget = forms.TextInput(
			attrs = {
			'autocomplete':'off',
			}
		))	
	Start_date     = forms.DateTimeField(required = False, label = _('Start_date'))
	End_date 	   = forms.DateTimeField(required = False, label =  _('End_date')) 
	Export_to_csv  = forms.BooleanField(required  = False, label = _('Export data as csv file'))
class StockHistorySearchForm(forms.ModelForm):
	class Meta:		
		model  = StockHistory
		fields = ['Item_name','Start_date','End_date']

	Item_name      = forms.CharField(required = False,label  = _('Item name'),help_text=_('Name of this item.') ,widget = forms.TextInput(
			attrs = {
			'autocomplete':'off',
			}
		))		
	Start_date     = forms.DateTimeField(required = False, label = _('Start_date'))
	End_date 	   = forms.DateTimeField(required = False, label =  _('End_date')) 
	Export_to_csv  = forms.BooleanField(required  = False, label = _('Export data as csv file'))

class StockUpdateForm(forms.ModelForm):
	class Meta:		
		model  = Stock
		fields = ['Category', 'Item_name', 'Quantity', 'Price']	

class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['Issue_qty', 'Issue_to']
	def clean_Issue_qty(self):
		Issue_qty = self.cleaned_data.get('Issue_qty')
		if not	Issue_qty :
			raise forms.ValidationError(_('This field is required'))
		if Issue_qty <  0: 
			Issue_qty = 0	
		return Issue_qty
		

class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['Receive_qty', 'Receive_from']

	def clean_Receive_qty(self):
		Receive_qty = self.cleaned_data.get('Receive_qty')
		if not	Receive_qty :
			raise forms.ValidationError(_('This field is required'))
		if Receive_qty <  0: 
			Receive_qty = 0	
		return Receive_qty