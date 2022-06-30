#import numpy as np
import pandas as pd
from scrapper import scrap 

#filename = 'naiveb/poultry.txt'
#with open(filename) as f:
#    contents = f.read()
#    f.close()

#contents = " "

from nltk.tokenize import word_tokenize

def prepare(url):
        contents = scrap(url)
        data = word_tokenize(contents.lower()) #contents.lower() 
        #from nltk.corpus import stopwords
        #english_stopwords = stopwords.words('english')
        #t_data = [t for t in data if t not in english_stopwords]
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
        print(df)
        return (df)
        
#prepare('https://www.britannica.com/topic/agriculture/Early-development')