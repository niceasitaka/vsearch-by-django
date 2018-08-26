from vsearch_test.models import *
from mysite.views import LoginRequiredMixin
#from vsearch_test.forms import VsearchForm

from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
#from django.urls import reverse_lazy, reverse
#from django.shortcuts import redirect, resolve_url, render

from ipware.ip import get_ip
from django_user_agents.utils import get_user_agent

class SearchV(CreateView):
	model = Vsearch
	fields = ['phrase', 'letters']
	template_name = 'vsearch_test/entry.html'
	initial = {'letters': 'aeiou'}	

	def form_valid(self, form):
		PhWord = '%s' % self.request.POST['phrase']
		LeWord = '%s' % self.request.POST['letters']
		form.instance.results = set(PhWord).intersection(set(LeWord))
				
		ip = get_ip(self.request)
		form.instance.ip = ip
		
		browser = get_user_agent(self.request)
		#browser = self.request.META['HTTP_USER_AGENT']
		form.instance.browser_string = browser
		
		return super(SearchV, self).form_valid(form)
		
class Search_resultV(LoginRequiredMixin, DetailView):
	model = Vsearch

class View_log(LoginRequiredMixin, ListView):
	model = Vsearch