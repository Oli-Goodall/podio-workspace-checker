import tkinter as tk


class AddAppWindow(tk.Toplevel):
    def __init__(self, parent, comparison_data):
        super().__init__(parent)

        self.geometry("400x300")  # Adjust the window size as needed
        self.title("Workspace App Manager")

        self.comparison_data = comparison_data
        self.selected_apps = []  # To store the selected app names

        self.create_app_listbox()

        self.add_button = tk.Button(self, text="Add", command=self.print_selected_apps)
        self.add_button.grid(row=len(self.comparison_data), column=0, columnspan=2, padx=5, pady=5)

        self.close_button = tk.Button(self, text="Close", command=self.destroy)
        self.close_button.grid(row=len(self.comparison_data) + 1, column=0, columnspan=2, padx=5, pady=5)

    def add_app(self, app_name):
        # Define what happens when an app is selected in the listbox
        if app_name not in self.selected_apps:
            self.selected_apps.append(app_name)
        else:
            self.selected_apps.remove(app_name)

    def print_selected_apps(self):
        # Print the selected app names when the "Add" button is clicked
        print("Selected apps:")
        for app_name in self.selected_apps:
            print(f" - {app_name}")

    def create_app_listbox(self):
        # Create the listbox and populate it with app names
        self.app_listbox = tk.Listbox(self, selectmode="extended", font=("Arial", 14))
        self.app_listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        for app in self.comparison_data:
            app_name = app['config']['name']
            self.app_listbox.insert(tk.END, app_name)

        # Bind the add_app method to the listbox selection event
        self.app_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

    def on_listbox_select(self, event):
        # Get the selected items from the listbox
        selected_items = self.app_listbox.curselection()

        # Update the selected_apps list based on the selected items
        self.selected_apps = [self.app_listbox.get(index) for index in selected_items]

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
