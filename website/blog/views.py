from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.shortcuts import redirect
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    print(posts)
    return render(request,'blog/post_list.html',{"post":posts})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def contents(request):
    return HttpResponse("Hey it's loading")

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)

    else:
        form = PostForm()
        return render(request,'blog/post_edit.html',{"form":form})

def upload_pic(request):
    if request.method == "POST":
        form  = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')




