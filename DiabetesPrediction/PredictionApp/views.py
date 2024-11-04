import joblib
from django.shortcuts import render

model = joblib.load('.\Saved models\Diabetes prediction model.jolib')

def Home(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        blood_pressure = int(request.POST.get('blood_pressure'))
        glucose = int(request.POST.get('glucose'))
        bmi = float(request.POST.get('bmi'))        

        data = [age, blood_pressure, glucose, bmi, ]
        
        prediction = model.predict([data])
        
        prediction_text = "Diabetic" if prediction == 1 else "Not Diabetic"
        
        return render(request, 'Home.html', {'prediction': prediction_text})
    return render(request, 'Home.html')