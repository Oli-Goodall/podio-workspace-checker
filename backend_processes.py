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
template_app_data = c.Application.list_in_space(8295229)

#Extract the useful bits of data from templateAppData
template_app_list = []
for app in template_app_data:
    template_app_list.append({'name': app['config']['name'], 'id': app['app_id']})

#Retrieve full app data for template workspace from Podio
comparison_app_data = []

def get_franchisee_app_list(id):
    comparison_app_data = c.Application.list_in_space(id)
    return comparison_app_data


#Extract the useful bits of data from templateAppData


#Retrieve full workspace data for org from Podio
workspaces_data = c.Space.find_all_for_org(301620)

#Extract the useful bits of data from workspacesData
franchisee_workspaces_list = []
for app in workspaces_data:
    if (app['name'][:3] == 'TAF' and app['name'][3].isalpha()):
        franchisee_workspaces_list.append({'name': app['name'], 'id': app['space_id']})




