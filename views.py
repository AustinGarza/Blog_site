from django.shortcuts import render, redirect
from .models import Blog_post
from .forms import NewPostForm

# Create your views here.
def index(request):
    """ Home page for blog """
    posts = Blog_post.objects.order_by('date')
    context = {'posts': posts}
    return render(request, 'blog_app/index.html', context)

def new_post(request):
    """ Adds a new post """
    if request.method != 'POST':
         # No data submitted, create blank form.
        form = NewPostForm()
    else:
        # POST data submitted; process data. 
        form = NewPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:index')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blog_app/new_post.html', context)

def edit_post(request, post_id):
    """ Edit posts contents """
    post_id = Blog_post.objects.get(id=post_id)
    current_entry = post_id.body
    
    if request != 'POST':
        # Initial request; Pre-fill with current contents.
        form = NewPostForm(instance=current_entry)
    else: 
        # POST data submitted; process data.
        form = NewPostForm(instance=current_entry, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('blog_app:index')