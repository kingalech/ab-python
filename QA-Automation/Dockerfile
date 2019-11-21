FROM python:2.7
RUN pip install nose
RUN pip install selenium
RUN pip install nose-enhanced-descriptions

COPY qa_automation.py .

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/local/lib/python2.7/site-packages/selenium/webdriver/chrome/

# run the actual selenium test
CMD ["nosetests", "qa_automation.py", "--verbose", "--with-enhanced-descriptions"]
