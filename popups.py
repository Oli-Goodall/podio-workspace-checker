import tkinter as tk
import backend_processes


class AddAppWindow(tk.Toplevel):
    def __init__(self, parent, selected_workspace_id, location_name):
        super().__init__(parent)

        self.geometry("750x400")
        self.resizable(False, False)
        self.title("Workspace App Manager")

        self.selected_workspace_id = selected_workspace_id
        self.location_name = location_name
        self.no_apps_message = None
        self.missing_apps = backend_processes.compare_app_lists(selected_workspace_id)
        self.missing_app_names = []
        for app in self.missing_apps:
            self.missing_app_names.append(app['config']['name'])

        self.apps_to_add = []

        self.selected_missing_apps = []  # To store the selected app names
        self.selected_apps_to_add = []

        self.app_selection_frame = tk.Frame(self)
        self.app_selection_frame.pack(fill="both")

       # Create the missing apps listbox and populate it with app names
        self.missing_apps_listbox_frame = tk.Frame(self.app_selection_frame)
        self.missing_apps_listbox_frame.pack(side=tk.LEFT, padx=50, pady=10)

        self.close_button = tk.Button(self.missing_apps_listbox_frame, text="< Back", command=self.destroy)
        self.close_button.pack(anchor=tk.NW)

        self.left_listbox_label = tk.Label(self.missing_apps_listbox_frame, text="Missing apps", font=("Arial", 20))
        self.left_listbox_label.pack(pady=10)

        self.missing_apps_listbox_scrollbar = tk.Scrollbar(self.missing_apps_listbox_frame, orient=tk.VERTICAL)
        self.missing_apps_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.missing_apps_listbox = tk.Listbox(self.missing_apps_listbox_frame, selectmode="extended", font=("Arial", 20), width=20, yscrollcommand=self.missing_apps_listbox_scrollbar.set)
        self.missing_apps_listbox.pack(side=tk.LEFT)

        self.missing_apps_listbox.bind('<<ListboxSelect>>', self.on_missing_apps_listbox_select)

        # Create the 'apps to add' listbox and populate it with app names
        self.apps_to_add_listbox_frame = tk.Frame(self.app_selection_frame)
        self.apps_to_add_listbox_frame.pack(side=tk.RIGHT, padx=50, pady=10)

        self.add_button = tk.Button(self.apps_to_add_listbox_frame, text="Add chosen apps >", command=self.handle_submit)
        self.add_button.pack(anchor=tk.NE)

        self.right_listbox_label = tk.Label(self.apps_to_add_listbox_frame, text="Apps to add", font=("Arial", 20))
        self.right_listbox_label.pack(pady=10)

        self.apps_to_add_listbox_scrollbar = tk.Scrollbar(self.apps_to_add_listbox_frame, orient=tk.VERTICAL)
        self.apps_to_add_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.apps_to_add_listbox = tk.Listbox(self.apps_to_add_listbox_frame, selectmode="extended", font=("Arial", 20), width=20, yscrollcommand=self.apps_to_add_listbox_scrollbar.set)
        self.apps_to_add_listbox.pack(side=tk.LEFT)

        self.apps_to_add_listbox.bind('<<ListboxSelect>>', self.on_apps_to_add_listbox_select)

        self.populate_listboxes()

        self.selection_button_frame = tk.Frame(self.app_selection_frame)
        self.selection_button_frame.pack(pady=150)

        # Create buttons that move items between listboxes
        self.choose_app_button = tk.Button(self.selection_button_frame, text="+", command=self.move_to_apps_to_add_list)
        self.unchoose_app_button = tk.Button(self.selection_button_frame, text="-", command=self.remove_from_apps_to_add_list)

        self.choose_app_button.pack()
        self.unchoose_app_button.pack()

    def handle_submit(self):
        if self.apps_to_add != []:
            ConfirmAddWindow(self, self.apps_to_add, self.location_name).grab_set()
        elif not self.no_apps_message:
            self.no_apps_message = tk.Label(self, text="No apps selected", font=("Arial", 20), anchor=tk.NE)
            self.no_apps_message.pack()

    def populate_listboxes(self):
        self.missing_apps_listbox.delete(0, tk.END)
        self.apps_to_add_listbox.delete(0, tk.END)
        for item in self.missing_app_names:
            self.missing_apps_listbox.insert(tk.END, item)
        for item in self.apps_to_add:
            self.apps_to_add_listbox.insert(tk.END, item)

    def on_missing_apps_listbox_select(self, event):
        # Get the selected items from the listbox
        selected_items = self.missing_apps_listbox.curselection()

        # Update the selected_apps list based on the selected items
        self.selected_missing_apps = [self.missing_apps_listbox.get(index) for index in selected_items]

    def on_apps_to_add_listbox_select(self, event):
        # Get the selected items from the listbox
        selected_items = self.apps_to_add_listbox.curselection()

        # Update the selected_apps list based on the selected items
        self.selected_apps_to_add = [self.apps_to_add_listbox.get(index) for index in selected_items]

    def move_to_apps_to_add_list(self):
        for app_name in self.selected_missing_apps:
            if app_name not in self.apps_to_add:
                self.apps_to_add.append(app_name)
                self.missing_app_names.remove(app_name)
        self.populate_listboxes()
        if self.no_apps_message:
            self.no_apps_message.pack_forget()
            self.no_apps_message = None


    def remove_from_apps_to_add_list(self):
        for app_name in self.selected_apps_to_add:
            if app_name not in self.missing_app_names:
                self.missing_app_names.append(app_name)
                self.apps_to_add.remove(app_name)
        self.populate_listboxes()

class ConfirmExitWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("300x100")
        self.resizable(False, False)
        self.title("Quit?")
        self.label = tk.Label(self, text="Are you sure you want to quit?", font=("Arial", 16), pady=5)
        self.label.pack()

        self.button_frame = tk.Frame(self, pady=10)
        tk.Button(self.button_frame, text="Cancel", command=self.destroy).pack(side=tk.LEFT)
        tk.Button(self.button_frame, text="Quit", command=self.quit).pack(side=tk.RIGHT)
        self.button_frame.pack()

class ConfirmAddWindow(tk.Toplevel):
    def __init__(self, parent, selected_app_names, target_workspace):
        super().__init__(parent)

        self.geometry("400x300")
        self.title("Confirm apps to add")
        self.resizable(False, False)
        self.message_width = self.winfo_screenwidth() - 30
        app_names_formatted = '\n'.join(selected_app_names)
        self.label = tk.Message(self, text=f"Are you sure you want to add the following apps to the {target_workspace} workspace? \n{(app_names_formatted)}", font=("Arial", 16), pady=5, padx=10, width=350)
        self.label.pack()

        self.button_frame = tk.Frame(self, pady=10)
        tk.Button(self.button_frame, text="Cancel", command=self.destroy).pack(side=tk.LEFT)
        tk.Button(self.button_frame, text="Confirm", command=self.add_chosen_apps).pack(side=tk.RIGHT)
        self.button_frame.pack()

        # Update the window's size to fit the label's height
        self.update_idletasks()  # Update widget sizes
        label_height = self.label.winfo_reqheight()  # Get the required height of the label
        new_height = label_height + self.button_frame.winfo_reqheight() + 30  # Adjust with padding
        self.geometry(f"400x{new_height}")  # Set new window height

    def add_chosen_apps(self):
    # Add the selected app names when the "Add" button is clicked
        for app in AddAppWindow.missing_apps:
            if app['config']['name'] in AddAppWindow.apps_to_add:
                backend_processes.add_app(app['app_id'], AddAppWindow.selected_workspace_id)
                AddAppWindow.apps_to_add.remove(app['config']['name'])
        AddAppWindow.populate_listboxes()
