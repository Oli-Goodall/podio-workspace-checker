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
    franchisee_apps = [app['config']['name'] for app in c.Application.list_in_space(id)]
    
    template_app_full_data_list = c.Application.list_in_space(8295229)
    template_app_names = [app['config']['name'] for app in template_app_full_data_list]
    
    missing_apps = []
    for template_app in template_app_names:
        template_app_clean = template_app.replace(" ", "")
        match_found = False
        for franchisee_app in franchisee_apps:
            franchisee_app_clean = franchisee_app.replace(" ", "")
            if template_app_clean == franchisee_app_clean:
                match_found = True
                break
            elif template_app_clean.endswith("XX") and template_app_clean[:-2] == franchisee_app_clean[:-2]:
                match_found = True
                break
        if not match_found:
            for template_app_full_data in template_app_full_data_list:
                if template_app == template_app_full_data['config']['name']:
                    missing_apps.append(template_app_full_data)
    return missing_apps

def add_app(app_id, space_id):
    c.Application.install(app_id, {"space_id":space_id, "features":["items"]})
    pass

