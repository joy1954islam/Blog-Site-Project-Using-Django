from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import ListView

from .forms import PostForm
from .models import Post


def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            messages.success(request, "Post Created Successfully")
            return redirect('viewPost')
        else:
            messages.error(request, "Post Not Created Successfully")
    else:
        form = PostForm()
    return render(request, 'Blog/form.html', {'form': form})


class viewPostList(ListView):
    model = Post
    template_name = 'Blog/Post_View.html'
    context_object_name = 'object_list'
    ordering = ['-data_posted']
    paginate_by = 5


def deletePost(request, pk, template_name='Blog/Post_Confirm_Delete.html'):
    training = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        training.delete()
        messages.success(request, "Post Deleted Successfully")
        return redirect('viewPost')
    # else:
    #     messages.error(request, "Training Not Deleted Successfully")
    return render(request, template_name, {'object': training})


def updatePost(request,pk):
    training = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=training)
    if form.is_valid():
        form.save()
        messages.success(request, "Post Updated Successfully")
        return redirect("viewPost")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'Blog/form.html', {'form': form})


def about(request):
    return render(request,'Blog/about.html')