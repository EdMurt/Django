# Create your views here
from models import Post, comment
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from forms import PostForm, commentForm

#def post_list (request):
#	posts = Post.objects.all() #recoge todos los valores del Post
#	context = {'posts': posts} #lso q va entre " " es lo q se envia al bucle for del html
#	return render_to_response("blog/list.html", context) #"blog/list.html" esta dentro de carpeta templates

#def post_detail (request,pk):
#	post = get_object_or_404 (Post,pk=pk)
#	context = {'post': post}
#	return render_to_response("blog/detail.html", context)

class PostList (ListView):
	model = Post

class PostDetail (DetailView):
	model = Post
	
	def get_context_data (self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
#		context['comments'] = comment.objects.all() # Para el if de la plantilla
		context['comments'] = comment.objects.filter(vinculo = self.get_object())
		return context

#class AddCommentView (request):
#	form_class = commentForm()
#	template_name = 'blog/post_comment.html'	
#	def form_valid(self, form):
#		Comm = comment(post=Post.objects.get(pk=int(self.kwargs['post_id'])))
#		frm = comment.objects.get(vinculo = self.get_object())
#		frm = commentForm(self.request.POST, instance=Comm)
#		frm.save()
#		return super(AddComment, self).form_valid(frm)

class PostCreate (CreateView):
	model = Post
	form_class = PostForm
	success_url = reverse_lazy('post_list')

class PostUpdate (UpdateView):
        model = Post

class PostDelete (DeleteView):
        model = Post
	success_url = reverse_lazy('post_list')

