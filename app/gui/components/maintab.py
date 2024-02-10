
import tkinter as tk
from tkinter import ttk, Tk
from src.models import User
from .create_campaign import CreateCampaign
from .scrolltab import ScrollableNotebookTab


class MainTab:
    def __init__(self, root: Tk,
                 #user: User
                 ):
        self.root = root
        self.root.geometry("1200x800")
        self.root.title("JJ Email Campaign")
        
        # Create Notebook Style
        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Helvetica', 12, 'bold'), padding=(15, 7))
        self.style.configure("Header.TFrame", background="#F0F0F0")

        # Header
        self.header_frame = ttk.Frame(self.root, padding=(50,50), style="Header.TFrame")
        self.header_frame.pack(fill="x")

        self.header_label = ttk.Label(self.header_frame, text="JJ Email Campaign", font=("Helvetica", 16, 'bold'))
        self.header_label.pack(side="left", padx=10)

        self.username_label = ttk.Label(self.header_frame, text=f"Hello, ", font=("Helvetica", 14, 'bold'))
        self.username_label.pack(side="right", padx=10)
        

        # Notebook with two tabs
        notebook = ttk.Notebook(self.root)

        # Existing Campaigns tab
        existing_campaigns_frame = ttk.Frame(notebook)
        existing_campaigns_label = ttk.Label(existing_campaigns_frame, text="Content for Existing Campaigns")
        existing_campaigns_label.pack(pady=10)
        notebook.add(existing_campaigns_frame, text="Existing Campaigns")

        # Create Campaign tab
        create_campaign_tab = CreateCampaign(notebook)
        notebook.add(create_campaign_tab, text="Create Campaign")
        # scrollable_tab = ScrollableNotebookTab(notebook)
        # # label = tk.Label(scrollable_tab.container, text="This is the content of the scrollable tab")
        # # label.pack()
        # scrollable_tab.pack(fill='both', expand=True)  # Use pack for the scrollable tab
        # notebook.add(scrollable_tab, text="Scrollable Tab")

        notebook.pack(expand=True, fill="both")