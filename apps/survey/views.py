from django.shortcuts import render, HttpResponse, redirect

#render the main form page
def index(request):
	if 'counter' not in request.session:
		request.session['counter'] = 0
	else: 
		request.session['counter'] += 1
	return render(request, 'survey/index.html') #may need to change

#process form submission
def process(request):
	if request.method == 'POST':
		
		request.session['data'] = {
			'First name' : request.POST['firstname'],
			'Last name' : request.POST['lastname'],
			'Dojo Location' : request.POST['location'],
			'Favorite Language' : request.POST['language']
		}
		print 'form processed'

	return redirect('/results')

def results(request):
	print "Show results"
	# print request.session['data']
	return render(request, 'survey/results.html')

def reset(request):
	request.session['counter'] = 0

	return redirect('/')



# Create your views here.
