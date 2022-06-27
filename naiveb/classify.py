from joblib import load

from prepare_input import df
from vocab import vect


my_nb = load('naiveb/newnbmodel.joblib')

A = df.text

A_pred_vect = vect.transform(A)


my_pred = my_nb.predict(A_pred_vect)

print('Prediction: ',my_pred)

if my_pred[0] == 1:
    print('Agriculture')
else:
    print('Not agriculture')

print(A)
