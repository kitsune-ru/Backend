import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora

def preproc_data(data, otdelnie_slova):
    tokenizer = RegexpTokenizer(r'\w+')
    nltk.download("stopwords")
    en_stop = set(stopwords.words('russian'))
    en_stop.add('т')
    en_stop.add('д')


    p_stemmer = PorterStemmer()
    text = []
    for i in data['data']:
        if (isinstance(i, float)==False):
            raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        stopped_tokens = [i for i in tokens if not i in en_stop]

        if (otdelnie_slova==True):
            'версия с отдельными словами'
            stemmed_tokens = []
            for i in stopped_tokens:
                stemd=p_stemmer.stem(i)
                if (stemd.isnumeric() == False):
                    stemmed_tokens.append(stemd)
        else:
            'версия с полными словосочетаниями'
            stemmed_tokens=""
            for i in stopped_tokens:
                stemd=p_stemmer.stem(i)
                if (stemd.isnumeric() == False):
                    stemmed_tokens+=stemd+" "

            stemmed_tokens=[stemmed_tokens]

        if (len(stemmed_tokens)>0):
            text.append(stemmed_tokens)
    return text

def prepare_corp(text):
    dictionary = corpora.Dictionary(text)
    text_term_matrix = [dictionary.doc2bow(doc) for doc in text]
    return dictionary, text_term_matrix