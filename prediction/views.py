from django.shortcuts import render
from decouple import config
from . forms import MlForm
from joblib import load
import numpy as np
import os


'''
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('./models/ssports_model2.pickle', 'rb') as f:
    model1 = pickle.load(f)

'''
os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = 'models/model_07-11-2022.pkl'
model = load(filename)

def ml_view(request):
	global result

	if request.method == "POST":
		form = MlForm(request.POST)

		if form.is_valid():
			form.save()
			result = form.cleaned_data

			likes = result['likes']
			comments = result['comments']
			duration = result['duration']
			category = result['category']
			year = result['year']

			def predict_view(likes,comments,duration,category,year):

				z = []

				if category == 'Basketball':
					a = [1,0,0,0,0,0]
				elif category == 'Betting':
					a = [0,1,0,0,0,0]
				elif category == 'Fighting':
					a = [0,0,1,0,0,0]
				elif category == 'Racing':
					a = [0,0,0,1,0,0]
				elif category == 'Soccer':
					a = [0,0,0,0,1,0]
				elif category == 'Tennis':
					a = [0,0,0,0,0,1]
					
				if year == '2018':
					b = [1,0,0,0,0]
				elif year == '2019':
					b = [0,1,0,0,0]
				elif year == '2020':
					b = [0,0,1,0,0]
				elif year == '2021':
					b = [0,0,0,1,0]
				elif year == '2022':
					b = [0,0,0,0,1]

				z = [likes,comments,duration,50] + a + b
				z = np.expand_dims(z, axis=0)
				pred = model.predict(z)
				
				return pred

			pred = predict_view(likes,comments,duration,category,year)
			pred=round(pred[0])


			return render(request,'prediction/ml.html',context={'form':form,
																'likes':likes,
																'comments':comments,
																'duration':duration,
																'category':category,
																'year':year,
																'pred':pred})
	
	else:
		form = MlForm()
	

	return render(request,'prediction/ml.html',context={'form':form})
