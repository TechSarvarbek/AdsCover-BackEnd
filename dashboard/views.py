from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from datetime import datetime

from .forms import AdminUpdateForm, UserUpdateForm, CompanyForm, AdForm
from users.models import Users
from company.models import Company, Ad


@login_required
def home(request):
	""" home """
	user_count = Users.objects.filter(created_at=datetime.today().date()).count()
	company_count = Company.objects.filter(created_at=datetime.today().date()).count()
	return render(request, 'dashboard/home.html', {'user_count':user_count, 'company_count':company_count})

@login_required
def users_view(request):
	""" all users """
	search = request.GET.get("search")
	if search:
		users = Users.objects.filter(Q(email__contains=search) | Q(telegram_name__contains=search))
	else:
		users = Users.objects.all().order_by('-id')
	paginator = Paginator(users, 100)
	page_number = request.GET.get('page')
	page = paginator.get_page(page_number)
	return render(request, 'dashboard/users/view.html', {
		'page':page, 
		'search':search if search else '',
		'result':users.count()
	})

@login_required
def user_update(request, id):
	""" user update """
	try:
		user = Users.objects.get(id=id)
		url = request.GET.get('url')
		if request.method == "POST":
			form = UserUpdateForm(request.POST, instance=user)
			if form.is_valid():
				form.save()
				messages.success(request, f"{user.email} has been changed.")
				return redirect(url if url else "dashboard:users")
			messages.error(request, form.errors)
			return render(request, 'dashboard/users/update.html', {'form':form})
		return render(request, 'dashboard/users/update.html', {'form':UserUpdateForm(instance=user)})
	except Users.DoesNotExist:
		raise Http404

@login_required
def companies_view(request):
	""" all companies """
	search = request.GET.get("search")
	if search:
		company = Company.objects.filter(Q(name=search) | Q(user__email__contains=search), active=True)
	else:
		company = Company.objects.filter(active=True).order_by('-id')
	paginator = Paginator(company, 100)
	page_number = request.GET.get('page')
	page = paginator.get_page(page_number)
	return render(request, 'dashboard/company/view.html', {
		'page':page, 
		'search':search if search else '',
		'result':company.count()
	})

@login_required
def company_update(request, id):
	""" company update """
	try:
		company = Company.objects.get(id=id)
		if request.method == "POST":
			form = CompanyForm(request.POST, instance=company)
			if form.is_valid():
				form.save()
				messages.success(request, f"{company.name} has been changed.")
				return redirect("dashboard:companies")
			messages.error(request, form.errors)
			return render(request, 'dashboard/company/update.html', {'form':form})
		return render(request, 'dashboard/company/update.html', {'form':CompanyForm(instance=company)})
	except Company.DoesNotExist:
		raise Http404

@login_required
def ad_update(request, id):
	""" ad update """
	try:
		ad = Ad.objects.get(id=id)
		url = request.GET.get('url')
		if request.method == 'POST':
			form = AdForm(request.POST, instance=ad)
			if form.is_valid():
				form.save()
				messages.success(request, "ad has been changed.")
				return redirect(url if url else 'dashboard:home')
			messages.error(request, form.errors)
			return render(request, 'dashboard/company/ad-update.html', {'form':form})
		return render(request, 'dashboard/company/ad-update.html', {'form':AdForm(instance=ad)})
	except Ad.DoesNotExist:
		raise Http404

@login_required
def admin_update(request):
	""" admin user update """
	if request.method == 'POST':
		form = AdminUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'The administrator profile has been changed.')
			return redirect('dashboard:home')
		messages.error(request, form.errors)
		return render(request, 'dashboard/admin/profile-update.html', {'form':form})
	return render(request, 'dashboard/admin/profile-update.html', {'form':AdminUpdateForm(instance=request.user)})

def admin_login(request):
	""" login """
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, email=email, password=password)
		if user is not None and user.is_superuser:
			login(request, user)
			messages.success(request, 'Login successfully.')
			return redirect("dashboard:home")
		else:
			messages.error(request, 'Invalid username or password.')
	return render(request, 'dashboard/login.html')

@login_required
def admin_logout(request):
	""" logout """
	logout(request)
	return redirect('dashboard:login')