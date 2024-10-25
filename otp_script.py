import random
import time

# Function to generate a random Indian phone number
def generate_indian_number():
    prefix = "+91"  # India country code
    number = "".join([str(random.randint(0, 9)) for _ in range(10)])
    return prefix + number

# Function to simulate OTP retrieval with a message
def get_otp(phone_number):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])  # 6-digit OTP
    messages = [
        f"Your OTP is {otp}. Please do not share it with anyone.",
        f"Use the OTP {otp} to verify your account.",
        f"Welcome! Your OTP for registration is {otp}.",
        f"OTP: {otp}. Complete your transaction securely."
    ]
    message = random.choice(messages)
    return otp, message

# Function to log OTPs and display them in real-time
def log_otp():
    with open("otp_log.txt", "w") as log_file:  # Create the file at the start
        while True:
            phone_number = generate_indian_number()
            otp, message = get_otp(phone_number)
            log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Phone Number: {phone_number}, OTP: {otp}, Message: {message}"
            print(log_entry)
            log_file.write(log_entry + "\n")
            log_file.flush()  # Ensure it's written to the file immediately
            time.sleep(5)  # Adjust time interval as needed

# Start logging OTPs
log_otp()
