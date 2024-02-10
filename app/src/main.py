from exchangelib import Credentials, Account, HTMLBody, DELEGATE, Message
import schedule
import time

def send_email(account, to_email, subject, body):
    # Create an HTML email
    email = Message(account=account,
                    subject=subject,
                    body=HTMLBody(body),
                    to_recipients=[to_email])
    
    # Send the email
    email.send()

def read_replies(account):
    # Access the inbox folder
    inbox = account.inbox
    
    # Iterate through unread emails
    for item in inbox.filter(is_read=False):
        print("Subject:", item.subject)
        print("Body:", item.body)
        
        # Here, you can extract the information you need from the email and store it in your database.
        # For example, you might want to extract data using regular expressions or other parsing methods.
        
        # Mark the email as read
        item.is_read = True
        item.save()

def main():
    # Configure your Office 365 accounts
    account_credentials = [
        {'email': 'account1@example.com', 'password': 'password1'},
        {'email': 'account2@example.com', 'password': 'password2'},
        # Add more accounts as needed
    ]

    # Set up accounts
    accounts = []
    for creds in account_credentials:
        credentials = Credentials(creds['email'], creds['password'])
        account = Account(creds['email'], credentials=credentials, autodiscover=True, access_type=DELEGATE)
        accounts.append(account)

    # Schedule sending emails
    schedule.every().day.at("08:00").do(send_email, accounts[0], 'recipient@example.com', 'Scheduled Email', 'Hello, this is a scheduled email.')

    # Schedule reading replies
    schedule.every(5).minutes.do(read_replies, accounts[0])  # Check for replies every 5 minutes

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
