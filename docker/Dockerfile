FROM tiagopeixoto/graph-tool
USER root
RUN pacman -S wget firefox python-pip --noconfirm
#Gecko driver install
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz
RUN tar -xvf geckodriver-v0.33.0-linux64.tar.gz -C /usr/local/bin/
#Python package and data installs
RUN pip install jupyter networkx gensim soupsieve beautifulsoup4 nltk seaborn statsmodels spacy booknlp selenium --break-system-packages	
RUN wget https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0.tar.gz
RUN tar -xf en_core_web_sm-3.6.0.tar.gz
RUN rm en_core_web_sm-3.6.0.tar.gz
USER user
RUN python -c 'import nltk; nltk.download("all")'
