from tkinter import *
from pypodio2 import api

client_id = "olis-podio-app"
client_secret = "BPuU6ZWR8uQP3HFMrU9HjfO1eEaChtJnDxoYosDEi8htMxakvzeVahCDnxzoXdm3"
username = "oliver@theaccountancyfranchise.co.uk"
password = "Oliver1234."

c = api.OAuthClient(
    client_id,
    client_secret,
    username,
    password,    
)

main = Tk()

main.mainloop()
