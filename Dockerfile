 FROM python:3
 ENV PYTHONUNBUFFERED 1
 ENV DIRPATH /code/HouseholdLedger
 RUN mkdir -p /code/HouseholdLedger
 RUN mkdir -p /var/log/django
 # RUN git clone https://github.com/jgj1018/HouseholdLedger.git
 ADD . $DIRPATH/
 WORKDIR $DIRPATH
 RUN pip install -r requirements.txt

