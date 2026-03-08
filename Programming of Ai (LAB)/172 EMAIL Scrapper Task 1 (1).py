import requests
import re
from bs4 import BeautifulSoup

# Website URL
url = "https://www.w3.org/People/"   

# Request bhejna
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Pure page ka text lena
    text = soup.get_text()
    
    # Email regex pattern
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    
    emails = re.findall(email_pattern, text)
    
    unique_emails = set(emails)  
    
    print("Found Emails:")
    for email in unique_emails:
        print(email)
else:
    print("Website access failed!")