import tkinter as tk
from tkinter import ttk, scrolledtext

class ScrollableNotebookTab(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Create a Canvas and add a Scrollbar to it
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas['yscrollcommand'] = self.scrollbar.set

        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='right', fill='both', expand=True)

        # Create a frame to hold the content inside the canvas
        self.container = ttk.Frame(self.canvas)
        self.container.grid(row=0, column=0, padx=250, pady=20)
        self.canvas.create_window((0, 0), window=self.container)

        # Configure canvas to update scroll region when the frame size changes
        self.container.bind('<Configure>', self.on_frame_configure)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        header_label = ttk.Label(self.container, text="Fill out Campaign details", font=("Helvetica", 14, 'bold'))
        header_label.grid(row=0, column=1, sticky="w")

        # Campaign Name
        name_label = ttk.Label(self.container, text="Campaign Name: ", font=("Helvetica", 12))
        name_label.grid(row=1, column=0, sticky="e")
        self.name_entry = ttk.Entry(self.container)
        self.name_entry.grid(row=1, column=1, sticky="w", pady=25)

        # Email From
        email_from_label = ttk.Label(self.container, text="Send From(Email): ", font=("Helvetica", 12))
        email_from_label.grid(row=2, column=0, sticky="e")
        self.email_from_entry = ttk.Entry(self.container)
        self.email_from_entry.grid(row=2, column=1, sticky="w", pady=25)

        # To Sent
        to_sent_label = ttk.Label(self.container, text="To Send(Emails): ", font=("Helvetica", 12))
        to_sent_label.grid(row=3, column=0, sticky="e")
        self.bcc_email_entry = ttk.Entry(self.container)
        self.bcc_email_entry.grid(row=3, column=1, sticky="w", pady=25)

        # Bcc Email
        bcc_email_label = ttk.Label(self.container, text="Bcc(Email): ", font=("Helvetica", 12))
        bcc_email_label.grid(row=4, column=0, sticky="e")
        self.to_sent_entry = ttk.Entry(self.container)
        self.to_sent_entry.grid(row=4, column=1, sticky="w", pady=25)

        # Email Body
        email_body_label = ttk.Label(self.container, text="Email Body: ", font=("Helvetica", 12))
        email_body_label.grid(row=5, column=0, sticky="e")
        self.email_body_text = scrolledtext.ScrolledText(self.container, wrap=tk.WORD, width=60, height=8)
        self.email_body_text.grid(row=5, column=1, sticky="w", pady=25)

        # Schedule Time
        schedule_time_label = ttk.Label(self.container, text="Campaign Schedule: ", font=("Helvetica", 12))
        schedule_time_label.grid(row=6, column=0, sticky="e")
        self.schedule_time_entry = ttk.Entry(self.container)
        self.schedule_time_entry.grid(row=6, column=1, sticky="w", pady=25)

        # Number of Emails per Campaign
        num_emails_label = ttk.Label(self.container, text="No. of sents/Campaign: ", font=("Helvetica", 12))
        num_emails_label.grid(row=7, column=0, sticky="e")
        self.num_emails_entry = ttk.Entry(self.container)
        self.num_emails_entry.grid(row=7, column=1, sticky="w", pady=25)
        
        # Configure the style for the button
        style = ttk.Style()
        style.configure("SubmitButton.TButton", foreground="white", background="gray", padding=(15,15))

        # Button to submit the campaign
        submit_button = ttk.Button(self.container, text="Save Campaign", command=self.submit_campaign, style="SubmitButton.TButton")
        submit_button.grid(row=8, column=1, sticky="w", pady=25)

    def on_frame_configure(self, event):
        # Update the canvas scroll region to match the size of the frame
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def on_canvas_configure(self, event):
        # Adjust canvas window width to avoid unnecessary horizontal scrollbar
        canvas_width = event.width
        self.canvas.itemconfig(self.container, width=canvas_width)
        
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
