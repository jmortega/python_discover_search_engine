Pycones2017 Talks
===============

Installation
------------

* Elasticsearch is running locally (localhost:9200)
* Tested on Python 3.4
* Use virtualenv to install Python dependencies

Clone repo, install virtualenv, install Python dependencies::

    git clone https://github.com/jmortega/pycones2017-elasticSearch
    cd pycones2017-elasticSearch
    virtualenv venv
    source ./venv/bin/activate
    pip install -r requirements.txt

Create basic database (use data from `data/pycones2017.data`)::

    make index

Run backend service::

    make backend

Run frontend service::

    make frontend

Point your browser to::

    http://localhost:8000

and search for a talk.


