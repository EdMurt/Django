from django.contrib import admin
from models import Post, comment
#from models import Playground


class commentInline (admin.StackedInline):
	model = comment
	extra = 1 # Muestra una casilla mas de comentario en vez de las 3 por defecto(en este caso) 
	can_delete = False # No permite borrar

class PostAdmin(admin.ModelAdmin):
	fields = ("titulo", "intro", "mas")#campos q se vean en runserver
	list_display = ("titulo", "intro", "visto")
	inlines = [
		commentInline,
	]


#class PlaygroundAdmin(admin.ModelAdmin):
#    change_form_template = 'blog/change_form.html'


admin.site.register(Post, PostAdmin)
admin.site.register(comment)
#admin.site.register(Playground, PlaygroundAdmin)
