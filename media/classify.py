from joblib import load
#from naiveb.prepare_input import prepare
from vocab import vect
from prepare_input import prepare


my_nb = load('naiveb/newnbmodel.joblib')
df = prepare('https://www.britannica.com/topic/agriculture/Early-development')
A = df.text

A_pred_vect = vect.transform(A)

my_pred = my_nb.predict(A_pred_vect)

print('Prediction: ',my_pred)

if my_pred[0] == 1:
    print('Agriculture')
else:
    print('Not agriculture')

print(A) 
