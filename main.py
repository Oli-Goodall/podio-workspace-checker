import tkinter as tk
import sys
sys.path.append('./src/pypodio2/')
from pypodio2 import api

class WorkspaceCheckerGUI:

    def __init__(self):

        self.client_id = "olis-podio-app"
        self.client_secret = "BPuU6ZWR8uQP3HFMrU9HjfO1eEaChtJnDxoYosDEi8htMxakvzeVahCDnxzoXdm3"
        self.username = "oliver@theaccountancyfranchise.co.uk"
        self.password = "Oliver1234."

        self.c = api.OAuthClient(
            self.client_id,
            self.client_secret,
            self.username,
            self.password,    
        )

        self.root = tk.Tk()

        self.btn = tk.Button(self.root, text="Click me", font=('Arial', 16), command=self.fetch_info)
        self.btn.pack(padx=10, pady=10)

        self.root.mainloop()
    
    def fetch_info(self):
        self.itemInfo = self.c.Item.find(2542371339)
        self.displyItemInfo = tk.Label(self.root, text=f'Item name: {self.itemInfo["fields"][0]["values"][0]["value"]}', font=('Arial', 16))
        self.displyItemInfo.pack(padx=10, pady=10)

WorkspaceCheckerGUI()



