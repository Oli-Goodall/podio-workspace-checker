import tkinter as tk
import sys
sys.path.append('./src/pypodio2/')
from pypodio2 import api

class MyGUI:

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

        self.label = tk.Label(self.root, text="Your Message", font=('Arial, 18'))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16))

        self.root.mainloop()

MyGUI()



