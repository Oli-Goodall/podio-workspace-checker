import sys
sys.path.append('./src/pypodio2/')
from pypodio2 import api

#Credentials for Podio API authentication
client_id = "olis-podio-app"
client_secret = "BPuU6ZWR8uQP3HFMrU9HjfO1eEaChtJnDxoYosDEi8htMxakvzeVahCDnxzoXdm3"
username = "oliver@theaccountancyfranchise.co.uk"
password = "Oliver1234."

#Authenticaiton with above credentials
c = api.OAuthClient(
    client_id,
    client_secret,
    username,
    password,    
)

#Retrieve the template workspace's app list data from Podio
templateAppData = c.Application.list_in_space(8295229)

#Extract the useful bits of data from templateAppData
templateAppList = []
for app in templateAppData:
    templateAppList.append({'name': app['config']['name'], 'id': app['app_id']})


print(templateAppList)