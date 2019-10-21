from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,NewProfileForm,CommentForm
from .models import Image,Profile,Comment


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user=request.user
    images=Image.get_images()
    comment=Comment.objects.filter(id=current_user.id).first()
    profile= Profile.objects.filter(user=current_user).first()

    
    print(images)
    return render(request, 'index.html',{"images":images,"comment":comment,"current_user":current_user,"profile":profile})

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
     image=Image.objects.filter(user=current_user).all()
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

def comment(request,image_id):
    try:
        comment = Comment.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"index.html", {"comment":comment})        


@login_required(login_url='/accounts/login/')
def new_comment(request,image_id):
   
    current_user = request.user
    image= Image.objects.filter(id=image_id).first()
    profile=Profile.objects.filter(user=current_user.id).first()
    if request.method == 'POST':
        form =CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image=image
            comment.save()
            return redirect('welcome') 

    else:
        form = CommentForm()
    return render(request, 'all-apps/new_comment.html', {"form": form,"image":image,"image_id":image_id})                

@login_required(login_url='/accounts/login/')
def likes(request,id):
    
    likes=1
    image = Image.objects.get(id=id)
    image.likes = image.likes+1
    image.save()    
    return redirect("/")
  