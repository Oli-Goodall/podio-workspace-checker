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

#Retrieve full app data for template workspace from Podio
templateAppData = c.Application.list_in_space(8295229)

#Extract the useful bits of data from templateAppData
templateAppList = []
for app in templateAppData:
    templateAppList.append({'name': app['config']['name'], 'id': app['app_id']})

#Retrieve full workspace data for org from Podio
workspacesData = c.Space.find_all_for_org(301620)

#Extract the useful bits of data from workspacesData
franchiseeWorkspacesList = []
for app in workspacesData:
    if (app['name'][:3] == 'TAF' and app['name'][3].isalpha()):
        franchiseeWorkspacesList.append({'name': app['name'], 'id': app['space_id']})



