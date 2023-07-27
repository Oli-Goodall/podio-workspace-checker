import tkinter as tk
import sys
sys.path.append('./src/pypodio2/')
from pypodio2 import api

class WorkspaceCheckerGUI:

    def __init__(self):

        #Credentials for Podio API authentication
        self.client_id = "olis-podio-app"
        self.client_secret = "BPuU6ZWR8uQP3HFMrU9HjfO1eEaChtJnDxoYosDEi8htMxakvzeVahCDnxzoXdm3"
        self.username = "oliver@theaccountancyfranchise.co.uk"
        self.password = "Oliver1234."

        #Authenticaiton with above credentials
        self.c = api.OAuthClient(
            self.client_id,
            self.client_secret,
            self.username,
            self.password,    
        )

        #Defines the root, i.e. the window that opens when code is run
        self.root = tk.Tk()

        #Adds button to the window
        self.btn = tk.Button(self.root, text="Click me", font=('Arial', 16), command=self.fetch_info)
        self.btn.pack(padx=10, pady=10)

        #Tells the root window to render
        self.root.mainloop()
    
    #Adds functionality to the button to retrieve and display the title of a hard-coded Podio item
    def fetch_info(self):
        self.itemInfo = self.c.Item.find(2542371339)
        self.displyItemInfo = tk.Label(self.root, text=f'Item name: {self.itemInfo["fields"][0]["values"][0]["value"]}', font=('Arial', 16))
        self.displyItemInfo.pack(padx=10, pady=10)