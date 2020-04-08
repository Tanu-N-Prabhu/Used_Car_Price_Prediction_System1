
# Importing all the necessary libraries
from django.shortcuts import render
# Importing the class named nameofTheCarForm from the forms.py file
from ucpps_app.forms import nameOfTheCarForm
# Django's built-in messages 
from django.contrib import messages
# Python date time library
from datetime import date
# Numpy library is used to operating storing the dataframe in a array
import numpy as np
# Importing Pickle library which is used to save and load the model
import pandas as pd
import time

import pandas as pd    
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score     
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error           # Loading the dataset into a dataframe and performing the desired operations
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
import time






def name(request):    
    if request.method == "POST":
        form = nameOfTheCarForm(request.POST)
    
        if form.is_valid():
            year = form.cleaned_data['carYearOfRegistration']
            power = form.cleaned_data['carPower']
            model = form.cleaned_data['carModel']
            kilometer = form.cleaned_data['carKilometer']
            month = form.cleaned_data['carMonth']
            fuel = form.cleaned_data['carFuelType']
            brand = form.cleaned_data['carBrand']
            postal = form.cleaned_data['carPostalCode']
            vehicle = form.cleaned_data['carVehicleType']
            vehicle = int(vehicle)
            vehicleList = []
            if vehicle == 1:
                vehicleList = [1, 0, 0, 0, 0, 0, 0, 0]
            elif vehicle == 2:
                vehicleList = [0, 1, 0, 0, 0, 0, 0, 0]
            elif vehicle == 3:
                vehicleList = [0, 0, 1, 0, 0, 0, 0, 0]
            elif vehicle == 4:
                vehicleList = [0, 0, 0, 1, 0, 0, 0, 0]        
            elif vehicle == 5:
                vehicleList = [0, 0, 0, 0, 1, 0, 0, 0]
            elif vehicle == 6:
                vehicleList = [0, 0, 0, 0, 0, 1, 0, 0]
            elif vehicle == 7:
                vehicleList = [0, 0, 0, 0, 0, 0, 1, 0]
            else:
                vehicleList = [0, 0, 0, 0, 0, 0, 0, 1]

            gearbox = form.cleaned_data['carGearBox']

            gearbox = int(gearbox)

            gearboxList = []
            if gearbox == 1:
                gearboxList = [1, 0]
            else:
                gearboxList = [0, 1]

            a = [year, power, model, kilometer, month, fuel, brand, postal]
            for i in vehicleList:
                a.append(i)

            for i in gearboxList:
                a.append(i)


            print(a)
            a = np.array([a]).tolist()

            
            loaded_model = pickle.load(open("model.sav", 'rb'))
            result = loaded_model.predict(a)
            predictedValue = pd.DataFrame(result)
            predictedValue = predictedValue.to_numpy()
            finalPrice  = str(predictedValue).lstrip('[').rstrip(']')
            finalPrice = int(float(finalPrice))
            print(finalPrice)
            messages.success(request,'The predicted price is: {}'.format(finalPrice)+ ' euros')

       
           








           
    form = nameOfTheCarForm()
    

    return render(request, "home.html", {'form':form, 'date': time.asctime( time.localtime(time.time()) )})

