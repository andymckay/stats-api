An example script to pull the Marketplace API.

To run::

 git clone https://github.com/andymckay/stats-api
 pip install -r requirements.txt
 export CONSUMER_KEY=[replace with your consumer key]
 export CONSUMER_SECRET=[replace with your consumer secret]
 python api.py

You should get::

 200
 {u'display_name': u'Andy McKay'}
