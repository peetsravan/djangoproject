from django.shortcuts import render,redirect
from .models import CustomUser,Apps,task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # 1. Validate fields are not empty
        if not username or not email or not password:
            return render(request, 'register.html', {
                'error': 'All fields are required.'
            })

        # 2. Check for duplicate username
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already taken.'
            })

        # 3. Check for duplicate email
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'error': 'Email already registered.'
            })

        # 4. Create user securely
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect('login_page')

    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'login.html', {'error': 'invalid credentials'})

        login(request, user)

        if user.is_admin:
            return redirect('admin_home')
        else:
            return redirect('user_home')

    return render(request, 'login.html')



@login_required
def logout_page(request):
    logout(request)
    messages.success(request, "You’ve been logged out.")
    return redirect('login_page')

@login_required
def admin_home(request):
    if not request.user.is_admin:
        return redirect('login_page')
    apps=Apps.objects.all()
    return render(request,'admin.html',{'apps':apps})

@login_required
def user_home(request):
    apps=Apps.objects.all()
    return render(request,'user.html',{'apps':apps})

@login_required
def add_app(request):
    if not request.user.is_admin:
        return redirect('login_page')
    if request.method=='POST':
        app_name = request.POST.get('app_name')
        app_link = request.POST.get('app_link')
        app_category = request.POST.get('app_category')
        sub_category = request.POST.get('sub_category')
        description = request.POST.get('description')
        points = request.POST.get('points')
        picture = request.FILES.get('picture')

        Apps.objects.create(
            app_name=app_name,
            app_link=app_link,
            app_category=app_category,
            sub_category=sub_category,
            description=description,
            points=points,
            picture=picture
        )
        return redirect('admin_home')

    return render(request, 'add_app.html')

@login_required
def review_screenshots(request):
    if not request.user.is_admin:
        return redirect('user_home') 

    pending_tasks = task.objects.filter(approved=False)

    return render(request, 'review_screenshots.html', {'tasks': pending_tasks})
@login_required
def approve_screenshot(request, task_id):
    if not request.user.is_admin:
        return redirect('user_home')

    task_obj = task.objects.get(id=task_id)

    if not task_obj.approved:
        task_obj.approved = True
        task_obj.save()

        task_obj.user.points_earned += task_obj.apps.points
        task_obj.user.save()

    return redirect('review_screenshots')


@login_required
def submit_task(request):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        app_id = request.POST.get("app_id")
        screenshot = request.FILES.get("screenshot")

        if not app_id or not screenshot:
            return JsonResponse({"error": "Both app and screenshot are required."}, status=400)

        app = get_object_or_404(Apps, id=app_id)

        task.objects.create(
            user=request.user,
            apps=app,
            screenshot=screenshot,
            approved=False
        )

        return JsonResponse({"status": "ok"})

    apps = Apps.objects.all()
    return render(request, "submit_task.html", {"apps": apps})






@login_required
def profile_page(request):
    return render(request, 'profile.html', {'user': request.user})
