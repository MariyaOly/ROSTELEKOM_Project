import os
from dotenv import load_dotenv

load_dotenv()
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
confirm_password= os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
invalid_phone = os.getenv('invalid_phone')
first_name = os.getenv('valid_first')
last_name = os.getenv('valid_last')
invalid_first = os.getenv('invalid_first')
invalid_last = os.getenv('invalid_last')
