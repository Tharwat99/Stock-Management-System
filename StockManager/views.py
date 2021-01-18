from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Stock, StockHistory, Category
from .forms import StockCreateForm,StockSearchForm, StockUpdateForm, IssueForm , ReceiveForm, StockHistorySearchForm, CatCreateForm
from django.http import HttpResponse
import csv

@login_required
def stocks(request):
	title = ' ITEMS'
	form = StockSearchForm(request.POST or None)
	if form.is_valid():
		if request.method == 'POST':
			Category = form['Category'].value()
			Start_date = form['Start_date'].value()
			End_date   = form['End_date'].value()
			objs = Stock.objects.filter(Item_name__icontains = form['Item_name'].value()).order_by('-Last_update')		
			if Start_date and End_date :
				objs = objs.filter(Timestamp__range = [Start_date, End_date]) 		
			if  Category :
				objs = objs.filter(Category = Category)
			if form['Export_to_csv'].value() == True:
				response = HttpResponse(content_type = 'text/csv')
				response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
				writer = csv.writer(response)
				writer.writerow(['Category', 'Item', 'Quantity'])
				for obj in objs:
					writer.writerow([obj.Category, obj.Item_name, obj.Quantity])
				return response		
	else:
		objs   = Stock.objects.order_by('-Last_update')  
	context = {
		'title'  : title,
		'objs'   : objs,
		'form'   : form,
	}
	return render(request, 'list_items.html',context)
@login_required
def stock_history(request):
	title = 'HISTORY'
	form = StockHistorySearchForm(request.POST or None)
	if form.is_valid():
		if request.method == 'POST':
			Start_date = form['Start_date'].value()
			End_date   = form['End_date'].value()
			objs = StockHistory.objects.filter(Item_name__icontains = form['Item_name'].value()).order_by('-Last_update')
			if Start_date and End_date :
				objs = objs.filter(Last_update__range = [Start_date, End_date]) 		
			if form['Export_to_csv'].value() == True:
				response = HttpResponse(content_type = 'text/csv')
				response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
				writer = csv.writer(response)
				writer.writerow(['Category', 'Item', 'Quantity','Issue_qty', 'Receive_qty'])
				for obj in objs:
					writer.writerow([obj.Category, obj.Item_name, obj.Quantity])
					return response				
	else:
		objs  = StockHistory.objects.order_by('-Last_update')  
	context = {
		'title'  : title,
		'objs'   : objs,
		'form'   : form,
	}
	return render(request, 'list_history.html',context)
@login_required
def detail_item(request, pk):
	title = 'Welcome, To Detail Item Page'
	obj = get_object_or_404(Stock,id = pk)
	context = {
		'title' : title, 
		'obj'   : obj,
	}
	return render(request, 'detail.html',context)

@login_required
def add_item(request):
	title = 'Add Stock'
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		instance.Added_by = str(request.user)
		instance.save()
		messages.success(request, "Successfully Added")
		return redirect('/')
	context ={
		'title'  : title,
		'form'   : form,
	}
	return render(request, 'add_item.html',context)

@login_required
def update_item(request, pk):
	title = 'Update Stock'
	delete = True
	obj = get_object_or_404(Stock,id = pk)
	form = StockUpdateForm(instance = obj)
	if request.method == "POST":
		form = StockUpdateForm(request.POST, instance = obj)
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully Updated")
			return redirect('/')
	context = {
		'title'  : title,
		'form' : form,
		'delete' : delete,
		'obj'    : obj,
	}
	return render (request, 'add_item.html',context)	
@login_required
def delete_item(request, pk):
	obj = get_object_or_404(Stock,id = pk)
	if request.method == 'POST':
		obj.delete()
		messages.success(request, "Successfully Deleted")
		return redirect('/')
	context ={
		'title' : 'Delete Stock',
		'obj' : obj
	}	
	return render(request, 'delete.html',context)	

@login_required
def issue_item(request, pk):
	obj = get_object_or_404(Stock,id = pk)
	form = IssueForm(request.POST or None, instance = obj)
	if form.is_valid():
		instance = form.save(commit = False)
		if instance.Quantity < instance.Issue_qty:
			instance.Issue_qty = instance.Quantity 
		instance.Quantity -=instance.Issue_qty
		instance.Issue_by = str(request.user)
		instance.save()
		issue_history = StockHistory(
			Item_id = instance.id,
			Item_name = instance.Item_name,
			Quantity  = instance.Quantity,
			Price     = instance.Price,
			Issue_qty = instance.Issue_qty,
			Issue_by  = instance.Issue_by,
			Issue_to  = instance.Issue_to,	
			Receive_qty = -1,
			Timestamp = instance.Timestamp,
			Last_update = instance.Last_update,
		)
		issue_history.save()
		messages.success(request, 'Successfully Issue '+ str(instance.Item_name) +" The Quantity in store now is "+ str(instance.Quantity))
		return redirect('/detail/'+str(instance.id))
	context = {
		'title' : 'Issue '+ str(obj.Item_name),
		'obj' : obj,
		'form' : form,
		'username' : 'Issue by '+ str(request.user)
	}		 	
	return render(request, 'add_item.html',context)	

@login_required
def receive_item(request, pk):
	obj = get_object_or_404(Stock,id = pk)
	form = ReceiveForm(request.POST or None, instance = obj)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.Quantity += instance.Receive_qty
		instance.Receive_by = str(request.user) 
		instance.save()
		receive_history = StockHistory(
			Item_id      = instance.id,
			Item_name    = instance.Item_name,
			Quantity     = instance.Quantity,
			Price        = instance.Price,
			Receive_qty  = instance.Receive_qty,
			Receive_from = instance.Receive_from,
			Receive_by   = instance.Receive_by,
			Timestamp    = instance.Timestamp,
			Last_update  = instance.Last_update,
		)
		receive_history.save()
		messages.success(request, 'Successfully Receive : '+ str(instance.Item_name) +" The Quantity in store now is "+ str(instance.Quantity))
		return redirect('/detail/'+str(instance.id))
	context = {
		'title' : 'Receive '+ str(obj.Item_name),
		'obj' : obj,
		'form' : form,
		'username' : 'Receive by '+ str(request.user)
	}		 	
	return render(request, 'add_item.html',context)	

@login_required
def categories(request):
	title = ' CATEGORIES'
	stocks = []
	objs   = Category.objects.order_by('-Last_update')  
	for obj in objs:
		count = Stock.objects.filter(Category = obj).count()
		stocks.append(count)
	context = {
		'title'  : title,
		'objs'   : objs,
		'stocks' : stocks,
	}
	return render(request, 'category.html',context)

	
@login_required
def add_cat(request):
	title = 'ADD CATEGORY'
	form = CatCreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		instance.save()
		messages.success(request, "Successfully Added")
		return redirect('/')
	context ={
		'title'  : title,
		'form'   : form,
	}
	return render(request, 'add_cat.html',context)
