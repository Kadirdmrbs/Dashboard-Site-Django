from django.shortcuts import render
from decouple import config
from . forms import MlForm



'''
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('./models/ssports_model2.pickle', 'rb') as f:
    model1 = pickle.load(f)

'''

def ml_view(request):
	global result

	if request.method == "POST":
		form = MlForm(request.POST)

		if form.is_valid():
			form.save()
			print(form.cleaned_data)
			result = form.cleaned_data
			likes = result['likes']
			comments = result['comments']
			return render(request,'prediction/ml.html',context={'form':form,
																'likes':likes,
																'comments':comments})
	
	else:
		form = MlForm()
	

	return render(request,'prediction/ml.html',context={'form':form})
