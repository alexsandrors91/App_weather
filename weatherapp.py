import requests
import json
import pprintpp
r= requests.get('http://www.geoplugin.net/json.gp')

if(r.status_code != 200):
    print('Não foi possivel obter a localização')
else:
   localizacao = json.loads(r.text)
   print(pprintpp.pprint(localizacao))
