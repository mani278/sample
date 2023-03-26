from django.shortcuts import render
import joblib
import numpy as np

# Create your views here.

model = joblib.load(r'E:\company work\N\New folder\PHD SISTER\CODE\Deploy\project\app\Dt1.pkl')


def home(request):
    return render(request, 'app/home.html')


def about(request):
    return render(request, 'app/about.html')


def predict(request):
    if request.method == 'POST':
        print('IF')
        features = [x for x in request.POST.values()]
        print(features)
        features = features[1:]
        print(features)
        final_features = [np.array(features)]
        #print(final_features)
        prediction = model.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(features)
        print(output)
        if output == 'Ischemic stroke':
            output = 'The person is affected by Ischemic stroke'
        elif output == 'hemorrhagic stroke':
            output = 'The person is affected by Hemorrhagic stroke'
        
        
        return render(request, 'app/index.html', {'prediction_text':output})
    else:
        print('ELSE')
    return render(request, 'app/index.html')