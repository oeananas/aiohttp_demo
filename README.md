# aiohttp_demo
simple aiohttp web app

# run

### params
configure config.yaml file (database and site name)
or use local file

'-H', '--host': 'listening host', default='127.0.0.1'

'-P', '--port': 'connection port', default=8080

'-R', '--reload': 'Autoreload on code change', default=True

'-C', '--config': 'Path to config file', default=demo/config.py

### start
create and activate virtualenv
```
pip install -r requirements.txt
python entry.py
```