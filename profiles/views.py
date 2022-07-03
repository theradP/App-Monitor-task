from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from datetime import timedelta, datetime
from .forms import SignUpForm, UserRoleForm, AppForm
from .models import User, InstallDetails
from rest_framework.views import APIView
import pandas as pd


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {
        'form': form,
        'profile': True
    })


@csrf_exempt
def role_update(request):
    if request.method == 'POST':
        instance = get_object_or_404(User, id=request.POST.get('id'))
        form = UserRoleForm(request.POST, instance=instance)
        if form.is_valid():
            user = form.save()
            user.save()
            user.refresh_from_db()
            return redirect('profiles:profile-role')
    else:
        users = User.objects.all()
        return render(request, 'app/admin_setting_user_role.html', {
            'users': users,
        })


def rating_view(request):
    return render(request, 'app/ratings.html')


def revenue_view(request):
    return render(request, 'app/revenue.html')


class InstallView(APIView):
    carriers = [x[0] for x in InstallDetails.objects.all().values_list('carrier').distinct()]

    def get(self, request):
        return render(request, 'app/installs.html', {'carriers': self.carriers})

    def post(self, request):
        start_date = datetime.strptime(request.POST.get('date__gte'), "%Y-%m-%d")
        end_date = datetime.strptime(request.POST.get('date__lte'), "%Y-%m-%d")
        carrier = request.POST.get('carrier')
        data = InstallDetails.objects.filter(carrier=carrier, date__lte=end_date, date__gte=start_date)
        date_list = [str(x.date()) for x in pd.date_range(start_date, end_date-timedelta(days=1), freq='d').tolist()]
        context = {"installs": [], 'carriers': self.carriers}
        for date in date_list:
            context['installs'].append(
                {
                    'date': date,
                    'daily_installs': data.filter(date=date).aggregate(Sum('daily_device_installs'))['daily_device_installs__sum']
                }
            )
        print(context['installs'])
        return render(request, 'app/installs.html', context)


class AdminView(APIView):

    def get(self, request):
        users = User.objects.all()
        return render(request, 'app/admin_setting.html', {'users': users})


def add_app(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save()
            app.save()
            app.refresh_from_db()
            return redirect('profiles:profile-admin')
    else:
        form = AppForm()
    return render(request, 'app/admin_setting_appform.html', {
        'form': form,
    })



