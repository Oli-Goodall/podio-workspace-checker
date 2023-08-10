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

# empty_app_request = {
#     "space_id": 0, #The id of the space on which the app is placed
#     "config": #The current configuration of the app,
#         {
#         "type": "standard", #The type of the app, either "standard", "meeting" or "contact",
#         "name": "", #The name of the app,
#         "item_name": "", #The name of each item in an app,
#         "description": "", #The description of the app,
#         "usage": "", #Description of how the app should be used,
#         "external_id": 0, #The external id of the app. This can be used to store an id from an external system on the app,
#         "icon": "", #The name of the icon used to represent the app,
#         "allow_edit": True, #True if other members are allowed to edit items from the app, false otherwise,
#         "default_view": "", #The default view of the app items on the app main page (see area for more information),
#         "allow_attachments": True, #True if attachment of files to an item is allowed, false otherwise,
#         "allow_comments": True, #True if members can make comments on an item, false otherwise,
#         "silent_creates": False, #True if item creates should not be posted to the stream, false otherwise,
#         "silent_edits": #True if item edits should not be posted to the stream, false otherwise,
#         "fivestar": #True if fivestar rating is enabled on an item, false otherwise,
#         "fivestar_label": #If fivestar rating is enabled, this is the label that will be presented to the users,
#         "approved": #True if an item can be approved, false otherwise,
#         "thumbs": #True if an item can have a thumbs up or thumbs down, false otherwise,
#         "thumbs_label": #If thumbs ratings are enabled, this is the label that will be presented to the users,
#         "rsvp": #True if RSVP is enabled, false otherwise,
#         "rsvp_label": #If RSVP is enabled, this is the label that will be presented to the users,
#         "yesno": #True if yes/no rating is enabled, false otherwise,
#         "yesno_label": #If yes/no is enabled, this is the label that will be presented to the users,
#         "tasks": #The list of tasks to be automatically created when an item is created
#         [
#         {
#             "text": #The text for the task,
#             "responsible": #The users who should be responsible for the task
#             [
#             "{user_id}",
#             #... (more user ids)
#             ]
#         }
#         ]
#     },
#     "fields":
#     [
#         {
#         "type": #The type of the field (see area for more information),
#         "config": #The configuration of the field,
#         {
#             "label": #The label of the field, which is what the users will see, 
#             "description": #The description of the field, shown to the user when inserting and editing,
#             "delta": #An integer indicating the order of the field compared to other fields,
#             "settings": #The settings of the field which depends on the type of the field (see area for more information),
#             "mapping": #The mapping of the field, see available mappings above,
#             "required": #True if the field is required when creating and editing items, false otherwise
#         }
#         },
#         ......
#     ]
#     }

app_to_add = {
      "app_id":28802203,
      "config":{
         "allow_create":True,
         "allow_edit":True,
         "description":"None",
         "external_id":"None",
         "icon":"411.png",
         "icon_id":411,
         "item_name":"Potential Clients",
         "name":"Leads",
         "type":"standard",
         "usage":"None"
      },
      "current_revision":2,
      "default_view_id":"None",
      "is_default":False,
      "item_accounting_info":"None",
      "link":"https://podio.com/businessandlegalcouk/template-franchisee-workspace/apps/leads",
      "link_add":"https://podio.com/businessandlegalcouk/template-franchisee-workspace/apps/leads/items/new",
      "original":28751074,
      "sharefile_vault_url":"None",
      "space_id":8295229,
      "status":"active",
      "url_add":"https://podio.com/businessandlegalcouk/template-franchisee-workspace/apps/leads/items/new",
      "url":"https://podio.com/businessandlegalcouk/template-franchisee-workspace/apps/leads",
      "url_label":"leads"
   },

data = c.Application.list_in_space(8295229)

print(data)