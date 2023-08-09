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

#Retrieve full workspace data for org from Podio
def get_franchisee_locations():
    workspaces_data = c.Space.find_all_for_org(301620)
    franchisee_locations_list = []
    for app in workspaces_data:
        if (app['name'][:3] == 'TAF' and app['name'][3].isalpha()):
            franchisee_locations_list.append({'name': app['name'], 'id': app['space_id']})
    return franchisee_locations_list

def compare_app_lists(id):
    franchisee_apps = []
    for app in c.Application.list_in_space(id):
        franchisee_apps.append(app['config']['name'])
    template_app_list = []
    for app in c.Application.list_in_space(8295229):
        template_app_list.append(app['config']['name'])
    missing_apps = []
    for template_app in template_app_list:
        if template_app not in franchisee_apps:
            missing_apps.append(template_app)
    return missing_apps
