from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from joblib import load
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import nltk
from nltk.tokenize import word_tokenize
from naiveb.forms import UrlForm 
from.models import Posts

global post_url

def get_link(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UrlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post_url = form.cleaned_data['url_link']
            new_post = Posts(url= post_url)
            new_post.save()
            post_id = new_post.id
            redirect_string = '/get-text/{}/'.format(post_id)
            return redirect(redirect_string)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UrlForm()
    template = loader.get_template('naiveb/classify.html')
    context = {'form':form,}
    return HttpResponse(template.render(context,request))

def get_text (request,id):
    template = loader.get_template('naiveb/classify.html')
    post = Posts.objects.get(id=id)
    post_url = post.url
    req = Request(post_url, headers={'User-Agent': 'Mozilla/5.0'})
    decoded_string = urlopen(req).read().decode() # convert bytes to str
    my_text = BeautifulSoup(decoded_string,features="lxml").get_text() # get the text from html and javascript
    my_text.encode(encoding = 'UTF-8', errors = 'replace') # use UTF-8 encoding.
    sent_list = nltk.tokenize.sent_tokenize(my_text) # split text into sentences
    content = sent_list[3:-10] # get the sentences that are commonly unique for each post
    content = ''.join(s for s in content) # combine the sentences
    # separate and join lines to form paragraphs
    lines = content.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    clean_content = ""
    for line in non_empty_lines:
        clean_content += line + "\n"
    context = {'text':clean_content}
    post.text = clean_content
    post.save()
    redirect_string = '/classify/{}/'.format(id)
    return redirect(redirect_string)


def classify(request,id):
    template = loader.get_template('naiveb/classify.html')
    post = Posts.objects.get(id=id)
    contents = post.text
    data = word_tokenize(contents.lower())
    t_data = [t for t in data if len(t)>3]
    from nltk import PorterStemmer
    ps = PorterStemmer()
    token_data = [ps.stem(i) for i in t_data]

    # Join tokenized words
    token_text = ' '.join([str(item) for item in token_data])

    data = {'text': token_text,
            'title': None}
    # Create DataFrame
    df = pd.DataFrame(data, index= [0])
    train = pd.read_csv('naiveb/clean.csv')
    from sklearn.model_selection import train_test_split
    X = train.text
    y = train.title
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

    from sklearn.feature_extraction.text import CountVectorizer
    vect = CountVectorizer(binary=False,max_features=3500,min_df=2,max_df=0.5) 

    X_train_vect = vect.fit_transform(X)
    ###
    my_nb = load('naiveb/newnbmodel.joblib')
    A = df.text

    A_pred_vect = vect.transform(A)

    my_pred = my_nb.predict(A_pred_vect)

    if my_pred[0] == 1:
        pred = 'Agriculture'
    else:
        pred = 'Not agriculture'

    post.prediction = my_pred
    post.save()
    context = {'pred': pred,
                'text':contents}
    redirect_string = '/results/{}/'.format(id)
    return redirect(redirect_string)

def results(request, id):
    post = Posts.objects.get(id=id)
    context = {'post':post}
    template = loader.get_template('naiveb/results.html')
    return HttpResponse(template.render(context,request))
