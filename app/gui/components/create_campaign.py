import tkinter as tk
from tkinter import ttk, scrolledtext
from .scrolltab import ScrollableNotebookTab
from tkcalendar import DateEntry

class CreateCampaign:
    def __init__(self, notebook):
        self.notebook = notebook
        
        # Create Campaign Frame
        self.create_campaign_tab = ttk.Frame(self.notebook)
        self.create_campaign_tab.pack(expand=True, fill="both")
        
        # Create Campaign Frame
        # self.create_campaign_frame = ScrollableFrame(self.notebook)
        # self.create_campaign_frame.pack(expand=True, fill="both")
        
        # self.create_campaign_frame = ScrollableNotebookTab(notebook)
        # label = tk.Label(self.create_campaign_frame.content_frame, text="This is the content of the scrollable tab")
        # label.pack()
        # self.create_campaign_frame.pack(fill='both', expand=True)  # Use pack for the scrollable tab
        # self.notebook.add(self.create_campaign_frame, text="Scrollable Tab")

        
        # Container for centering
        container = ttk.Frame(self.create_campaign_frame)
        container.grid(row=0, column=0, padx=250, pady=20)
        
        header_label = ttk.Label(container, text="Fill out Campaign details", font=("Helvetica", 14, 'bold'))
        header_label.grid(row=0, column=1, sticky="w")
        
        # Campaign Name
        name_label = ttk.Label(container, text="Campaign Name: ", font=("Helvetica", 12))
        name_label.grid(row=1, column=0, sticky="e")
        self.name_entry = ttk.Entry(container)
        self.name_entry.grid(row=1, column=1, sticky="w", pady=25)

        # Email From
        email_from_label = ttk.Label(container, text="Send From(Email): ", font=("Helvetica", 12))
        email_from_label.grid(row=2, column=0, sticky="e")
        self.email_from_entry = ttk.Entry(container)
        self.email_from_entry.grid(row=2, column=1, sticky="w", pady=25)
        
        # Define the options for the dropdown
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]

        # Variable to store the selected option
        selected_option = tk.StringVar(container)
        selected_option.set(options[0])  # Set the default option

        # Create the OptionMenu widget
        dropdown = tk.OptionMenu(container, selected_option, *options)
        dropdown.pack(pady=10)

        # To Sent
        to_sent_label = ttk.Label(container, text="To Send(Emails): ", font=("Helvetica", 12))
        to_sent_label.grid(row=3, column=0, sticky="e")
        self.bcc_email_entry = ttk.Entry(container)
        self.bcc_email_entry.grid(row=3, column=1, sticky="w", pady=25)

        # Bcc Email
        bcc_email_label = ttk.Label(container, text="Bcc(Email): ", font=("Helvetica", 12))
        bcc_email_label.grid(row=4, column=0, sticky="e")
        self.to_sent_entry = ttk.Entry(container)
        self.to_sent_entry.grid(row=4, column=1, sticky="w", pady=25)

        # Email Body
        email_body_label = ttk.Label(container, text="Email Body: ", font=("Helvetica", 12))
        email_body_label.grid(row=5, column=0, sticky="e")
        self.email_body_text = scrolledtext.ScrolledText(container, wrap=tk.WORD, width=60, height=8)
        self.email_body_text.grid(row=5, column=1, sticky="w", pady=25)

        # Schedule Time
        schedule_time_label = ttk.Label(container, text="Campaign Schedule: ", font=("Helvetica", 12))
        schedule_time_label.grid(row=6, column=0, sticky="e")
        self.schedule_time_entry = ttk.Entry(container)
        self.schedule_time_entry.grid(row=6, column=1, sticky="w", pady=25)

        # Number of Emails per Campaign
        num_emails_label = ttk.Label(container, text="No. of sents/Campaign: ", font=("Helvetica", 12))
        num_emails_label.grid(row=7, column=0, sticky="e")
        self.num_emails_entry = ttk.Entry(container)
        self.num_emails_entry.grid(row=7, column=1, sticky="w", pady=25)
        
        # Configure the style for the button
        style = ttk.Style()
        style.configure("SubmitButton.TButton", foreground="white", background="gray", padding=(15,15))

        # Button to submit the campaign
        submit_button = ttk.Button(container, text="Save Campaign", command=self.submit_campaign, style="SubmitButton.TButton")
        submit_button.grid(row=8, column=1, sticky="w", pady=25)

    def submit_campaign(self):
        # Implement your logic to handle the submitted campaign data
        name = self.name_entry.get()
        email_from = self.email_from_entry.get()
        to_sent = self.to_sent_entry.get()
        bcc_email = self.bcc_email_entry.get()
        email_body = self.email_body_text.get("1.0", "end-1c")  # Get text from the Text widget
        schedule_time = self.schedule_time_entry.get()
        num_emails = self.num_emails_entry.get()

        # Add your logic to handle the data (e.g., send emails, schedule, etc.)
        # For now, just print the values for demonstration
        print("Name:", name)
        print("Email From:", email_from)
        print("To Sent:", to_sent)
        print("Bcc Email:", bcc_email)
        print("Email Body:", email_body)
        print("Schedule Time:", schedule_time)
        print("Number of Emails per Campaign:", num_emails)



