import json
import gensim as gs
from gensim import corpora
import numpy as np

#Pull the data
wosdata = json.load(open('../data/wos_topic_doc.json'))
journals = [k for k in wosdata if k != 'SCIENCE']
full_docs = []
for k in journals:
    full_docs += wosdata[k]
#Train/test split
#setting a seed so we all get the same train/test
np.random.seed(6)
#testing will be 20%
train_num = int(0.8 * len(full_docs))
#We can shuffle the dataset and just take up to train_num and then the test is the leftover
np.random.shuffle(full_docs)
train_docs = full_docs[:train_num]
test_docs = full_docs[train_num:]
#Conversion
#Create the dictionary - note that we use all documents *not* the train or test 
dictionary = corpora.Dictionary(full_docs)
#And the the corpuses
##training
corpus_train = []
for tmp_doc in train_docs:
    corpus_train += [dictionary.doc2bow(tmp_doc)]
##testing
corpus_test = []
for tmp_doc in test_docs:
    corpus_test += [dictionary.doc2bow(tmp_doc)]
#Run it out
assumed_K_list = [x+1 for x in range(10)] + [20, 30, 40, 50]
train_perplex, test_perplex, model_bound = [], [], []
topic_descriptions = {}
for tmp_k in assumed_K_list:
    lda = gs.models.ldamodel.LdaModel(corpus=corpus_train, id2word=dictionary, num_topics=tmp_k, update_every=1, chunksize=10000, passes=1)
    train_perplex.append( 2**-lda.log_perplexity(corpus_train) )
    test_perplex.append( 2**-lda.log_perplexity(corpus_test) )
    model_bound.append( lda.bound(corpus_test) )
    topic_descriptions[tmp_k] = lda.print_topics(num_words = 5)
    print(tmp_k)
#Save it down
json.dump({'train' : train_perplex, 'test': test_perplex, 'k': assumed_K_list, 'bound' : model_bound}, \
          open('../data/wos_lda/wos_perplexity.json', 'w'))
for k,v in topic_descriptions.items():
    print( v )

