import tkinter as tk
import backend_processes
import entry_with_placeholder
import popups

class LandingPage:

    def __init__(self):

        # Defines the root, i.e., the window that opens when code is run
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        self.top_frame = tk.Frame(self.root)
        self.landing_title = tk.Label(self.top_frame, text='Select the franchise location you want to check:', font=("Arial", 20))
        self.landing_title.pack()

        self.middle_frame = tk.Frame(self.root)
        # Create the EntryWithPlaceholder widget without focus
        self.franchisee_selection_input = entry_with_placeholder.EntryWithPlaceholder(self.middle_frame, "Start typing location...")
        self.franchisee_selection_input.pack()

        self.listbox_frame = tk.Frame(self.middle_frame)
        self.listbox_scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.franchisee_list_box = tk.Listbox(self.listbox_frame, width=19, height=10, yscrollcommand=self.listbox_scrollbar.set)
        self.error_text = tk.Label(self.middle_frame, text='Error: Please enter valid location', font=("Arial", 18))

        self.listbox_scrollbar.config(command=self.franchisee_list_box.yview)

        # Hide listbox initially
        self.franchisee_list_box.pack_forget()
        self.listbox_scrollbar.pack_forget()

        # Retrieve list of franchisee space names from Podio
        self.franchise_space_names = [{'id': space['id'], 'name': space['name'].split('Accountants', 1)[-1].strip()} for space in backend_processes.get_franchisee_locations()]

        # Add franchisee space names to listbox
        self.update(self.franchise_space_names)

        self.franchisee_list_box.bind("<<ListboxSelect>>", self.fillout)
        self.franchisee_selection_input.bind("<KeyRelease>", self.check)
        self.franchisee_selection_input.bind("<FocusIn>", self.on_entry_focus_in)

        # Set focus on the root when the window is clicked
        self.root.bind("<Button-1>", self.on_root_click)
        
        self.bottom_frame = tk.Frame(self.root)
        self.submit_button = tk.Button(self.bottom_frame, text="Submit", command=self.handle_submit)
        self.exit_button = tk.Button(self.bottom_frame, text="Exit", command=self.handle_exit)
        self.submit_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)

        self.top_frame.pack(pady=10)
        self.bottom_frame.pack(pady=10)
        self.middle_frame.pack()

        # Tells the root window to render
        self.root.mainloop()

    def update(self, data):
        self.franchisee_list_box.delete(0, tk.END)
        for item in data:
            self.franchisee_list_box.insert(tk.END, item)

    def fillout(self, e):
        self.franchisee_selection_input.delete(0, tk.END)
        self.franchisee_selection_input.insert(0, self.franchisee_list_box.get(tk.ANCHOR))

    def check(self, e):
        typed = self.franchisee_selection_input.get()

        if typed == '':
            data = [space['name'] for space in self.franchise_space_names]  # Extract 'name' from each dictionary
        else:
            data = []
            for space in self.franchise_space_names:
                if typed.lower() in space['name'].lower():
                    data.append(space['name'])

        self.update(data)
        # Show the listbox only when there are matching results and the input field has focus
        if data and self.franchisee_selection_input.focus_get() == self.franchisee_selection_input:
            if len(data) < 10:
                self.franchisee_list_box.config(height=0)
            else:
                self.franchisee_list_box.config(height=10)
            self.listbox_frame.pack()
            self.franchisee_list_box.pack(side=tk.LEFT)
            self.listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        else:
            self.franchisee_list_box.pack_forget()
            self.listbox_scrollbar.pack_forget()

    def on_root_click(self, event):
        # Set focus on the root window explicitly
        self.root.focus_set()

        # Hide the listbox and scrollbar when clicking outside the input field
        self.franchisee_list_box.pack_forget()
        self.listbox_scrollbar.pack_forget()

    def on_entry_focus_in(self, event):
        # Set focus to the Entry widget when it gains focus
        self.franchisee_selection_input.focus_set()
        self.franchisee_selection_input.foc_in()

    def handle_submit(self):
        selected_name = self.franchisee_selection_input.get()

        # Check if an item is selected from the listbox
        if selected_name:
            # Find the corresponding ID from self.franchiseSpaceNames
            selected_id = None
            for space in self.franchise_space_names:
                if space['name'] == selected_name:
                    selected_id = space['id']
                    break

            if selected_id is not None:
                # Create the AddAppWindow instance with the fetched data
                add_app_window = popups.AddAppWindow(self.root, selected_id, selected_name)

                # Display the window
                add_app_window.grab_set()
            else:
                # Handle the case when the selected name does not have a corresponding ID
                self.error_text.pack()
     
    def handle_exit(self):
        popups.ConfirmExitWindow(self.root).grab_set()
