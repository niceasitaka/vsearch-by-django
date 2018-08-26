from vsearch_test.models import *
from vsearch_test.forms import VsearchForm

from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, resolve_url, render

class SearchV(CreateView):
	model = Vsearch
	#form_class = VsearchForm
	fields = ['phrase', 'letters']
	template_name = 'vsearch_test/entry.html'
	initial = {'letters': 'aeiou'}
	#success_url = reverse_lazy('vsearch:result')	
	'''
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['key'] = Vsearch.objects.filter(id=self.kwargs['pk'])
		return context	
	'''
	def form_valid(self, form):
		#context = self.get_context_data()
		PhWord = '%s' % self.request.POST['phrase']
		LeWord = '%s' % self.request.POST['letters']
		#phrase_db = Vsearch(phrase=PhWord, letters=LeWord, results=set(PhWord).intersection(set(LeWord)))
		form.instance.results = set(PhWord).intersection(set(LeWord))
		#phrase_db = Vsearch(results=set(PhWord).intersection(set(LeWord)))
		return super(SearchV, self).form_valid(form)
		'''
		formset = context			
		self.object = phrase_db.save()
		formset = self.object
		formset.save()
		#self.object = phrase_db.save()
		#return resolve_url('vsearch:result', 10)
		#return super(SearchV, self).form_valid(form)
		return redirect(self.object.get_absolute_url())
		#return redirect(Vsearch)
		#return redirect('vsearch:result', view)
		'''
		#return render(self.request, self.template_name)
		
class Search_resultV(DetailView):
	model = Vsearch
		
class View_log(ListView):
	pass