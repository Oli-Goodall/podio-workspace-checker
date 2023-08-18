import tkinter as tk
from tkinter import ttk
import backend_processes
import popups

class LandingPage:

    def __init__(self):

        # Defines the root, i.e., the window that opens when code is run
        self.root = tk.Tk()
        self.root.title("Franchisee Workspace Tracker")
        self.root.geometry("500x250")
        self.root.resizable(False, False)

        self.selected_index = ""

        self.top_frame = tk.Frame(self.root)
        self.landing_title = tk.Label(self.top_frame, text='Select the franchise location you want to check:', font=("Arial", 20))
        self.landing_title.pack()

        # Retrieve list of franchisee space names from Podio
        self.franchise_space_data = [{'id': space['id'], 'name': space['name'].split('Accountants', 1)[-1].strip()} for space in backend_processes.get_franchisee_locations()]
        self.franchise_locations = [space['name'] for space in self.franchise_space_data]

        self.middle_frame = tk.Frame(self.root)

        self.franchisee_location_dropdown = ttk.Combobox(self.middle_frame, state="readonly", values=self.franchise_locations)
        self.franchisee_location_dropdown.set('Select franchisee location...')
        self.franchisee_location_dropdown.bind("<<ComboboxSelected>>", self.combo_click)
        self.franchisee_location_dropdown.pack()
        
        self.bottom_frame = tk.Frame(self.root)
        self.submit_button = tk.Button(self.bottom_frame, text="Submit", command=self.handle_submit)
        self.exit_button = tk.Button(self.bottom_frame, text="Exit", command=self.handle_exit)
        self.submit_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)

        self.top_frame.pack(pady=30)
        self.middle_frame.pack()
        self.bottom_frame.pack(pady=30)

        # Tells the root window to render
        self.root.mainloop()

    def combo_click(self, e):
        self.selected_index = self.franchisee_location_dropdown.get()

    def handle_submit(self):
        if self.selected_index:
            selected_item = self.franchisee_location_dropdown.get()
            selected_id = None
            for space in self.franchise_space_data:
                if space['name'] == selected_item:
                    selected_id = space['id']
                    break

            # Create the AddAppWindow instance with the fetched data
            add_app_window = popups.AddAppWindow(self.root, selected_id, selected_item)

            # Display the window
            add_app_window.grab_set()
     
    def handle_exit(self):
        popups.ConfirmExitWindow(self.root).grab_set()
