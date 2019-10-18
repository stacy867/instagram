from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,NewProfileForm
from .models import Image,Profile


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images=Image.objects.all()
    print(images)
    return render(request, 'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('welcome')
        # return render(request, 'all-apps/post.html')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
     current_user= request.user
     image=Image.objects.filter(user=current_user)
     profile= Profile.objects.filter(user=current_user).first()   
     return render(request,'profile.html',{"image":image,"profile":profile})     

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('profile')
        # return render(request, 'all-apps/post.html')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form}) 




def post(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-apps/post.html", {"image":image})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        # searched_profiles = User.objects.filter(username__icontains=search_term)

        searched_users = Profile.search_by_profile(search_term)
        print(searched_users)
        message = f"{search_term}"

        return render(request, "all-apps/search.html",{"message":message,"users": searched_users})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-apps/search.html',{"message":message})

