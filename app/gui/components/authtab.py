from tkinter import ttk, messagebox, Tk
from .maintab import MainTab
from src.db_operations import Session, get_login_user


class AuthenticationTab:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("JJ Email Campaign - Login")

        # Set the size of the login window
        self.root.geometry("600x300")

        # Create a frame to hold the contents
        content_frame = ttk.Frame(root)
        content_frame.grid(row=0, column=0, padx=10, pady=10)

        # Center the frame within the root window
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Center the contents within the frame
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

        self.username_label = ttk.Label(content_frame, text="Username:", font=("Helvetica", 12))
        self.username_entry = ttk.Entry(content_frame)

        self.password_label = ttk.Label(content_frame, text="Password:", font=("Helvetica", 12))
        self.password_entry = ttk.Entry(content_frame, show="*")

        self.login_button = ttk.Button(content_frame, text="Login", command=self.login)

        self.username_label.grid(row=0, column=0, pady=10, padx=10)
        self.username_entry.grid(row=0, column=1, pady=10, padx=10)

        self.password_label.grid(row=1, column=0, pady=10, padx=10)
        self.password_entry.grid(row=1, column=1, pady=10, padx=10)

        self.login_button.grid(row=2, column=1, pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        session = Session()

        # Check if the entered credentials exist in the database
        user = get_login_user(session=session, username=username, password=password)

        if user:
            messagebox.showinfo("Login Successful", "Welcome, {} {}".format(user.firstname, user.lastname))
            self.detach()  # Detach the authentication tab
            MainTab(self.root, 
                    #user
                    )  # Attach the main tab to the root
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def detach(self):
        # Destroy all widgets in the authentication tab
        for widget in self.root.winfo_children():
            widget.destroy()