import tkinter as tk
import backend_processes


class AddAppWindow(tk.Toplevel):
    def __init__(self, parent, selected_workspace_id):
        super().__init__(parent)

        self.geometry("400x300")  # Adjust the window size as needed
        self.title("Workspace App Manager")

        self.selected_workspace_id = selected_workspace_id
        self.missing_apps = backend_processes.compare_app_lists(selected_workspace_id)
        self.missing_app_names = []
        for app in self.missing_apps:
            self.missing_app_names.append(app['config']['name'])

        self.selected_missing_apps = []  # To store the selected app names

        self.app_selection_frame = tk.Frame(self)
        self.app_selection_frame.pack()

       # Create the missing apps listbox and populate it with app names
        self.missing_apps_listbox_frame = tk.Frame(self.app_selection_frame)
        self.missing_apps_listbox_frame.pack(side=tk.LEFT)

        self.missing_apps_listbox_scrollbar = tk.Scrollbar(self.missing_apps_listbox_frame, orient=tk.VERTICAL)
        self.missing_apps_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.missing_apps_listbox = tk.Listbox(self.missing_apps_listbox_frame, selectmode="extended", font=("Arial", 14), width=10, yscrollcommand=self.missing_apps_listbox_scrollbar.set)
        self.missing_apps_listbox.pack(side=tk.LEFT)

        self.populate_missing_apps_listbox(self.missing_app_names)

        self.missing_apps_listbox.bind('<<ListboxSelect>>', self.on_missing_apps_listbox_select)

        # Create the 'apps to add' listbox and populate it with app names
        self.apps_to_add_listbox_frame = tk.Frame(self.app_selection_frame)
        self.apps_to_add_listbox_frame.pack(side=tk.RIGHT)

        self.apps_to_add_listbox_scrollbar = tk.Scrollbar(self.apps_to_add_listbox_frame, orient=tk.VERTICAL)
        self.apps_to_add_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.apps_to_add_listbox = tk.Listbox(self.apps_to_add_listbox_frame, selectmode="extended", font=("Arial", 14), width=10, yscrollcommand=self.missing_apps_listbox_scrollbar.set)
        self.apps_to_add_listbox.pack(side=tk.LEFT)

        self.apps_to_add_listbox.bind('<<ListboxSelect>>', self.on_missing_apps_listbox_select)

        # Create buttons that move items between listboxes
        self.choose_app_button = tk.Button(self.app_selection_frame, text="+", command=self.move_to_add_list)
        self.unchoose_app_button = tk.Button(self.app_selection_frame, text="-", command=self.move_to_add_list)

        self.choose_app_button.pack()
        self.unchoose_app_button.pack()

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_selected_apps)
        self.add_button.pack(side=tk.LEFT)

        self.close_button = tk.Button(self.button_frame, text="Close", command=self.destroy)
        self.close_button.pack(side=tk.RIGHT)

    def add_selected_apps(self):
        # Add the selected app names when the "Add" button is clicked
        print("Selected apps:")
        for app in self.missing_apps:
            if app['config']['name'] in self.selected_missing_apps:
                backend_processes.add_app(app['app_id'], self.selected_workspace_id)
                self.missing_app_names.remove(app['config']['name'])
        self.populate_missing_apps_listbox(self.missing_app_names)

    def populate_missing_apps_listbox(self, data):
        self.missing_apps_listbox.delete(0, tk.END)
        for item in data:
            self.missing_apps_listbox.insert(tk.END, item)

    def on_missing_apps_listbox_select(self, event):
        # Get the selected items from the listbox
        selected_items = self.missing_apps_listbox.curselection()

        # Update the selected_apps list based on the selected items
        self.selected_missing_apps = [self.missing_apps_listbox.get(index) for index in selected_items]

    def move_to_add_list(self):
        for app_name in self.selected_missing_apps:
            self.apps_to_add_listbox.insert(tk.END, app_name)
            #This part of the function needs looking at - delete from source list and repopulate?
            self.missing_apps_listbox.delete(app_name)
    

class ConfirmExitWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("300x100")
        self.title("Quit?")
        self.label = tk.Label(self, text="Are you sure you want to quit?", font=("Arial", 16))
        self.label.pack()

        self.button_frame = tk.Frame(self, pady=10)
        tk.Button(self.button_frame, text="Cancel", command=self.destroy).pack(expand=True, side=tk.LEFT)
        tk.Button(self.button_frame, text="Quit", command=self.quit).pack(expand=True, side=tk.RIGHT)
        self.button_frame.pack()
