import random
import string

def generate_otp(length=6):
    # Define the characters that can be used in the OTP
    characters = string.digits + string.ascii_letters
    
    # Generate a random OTP using the characters
    otp = ''.join(random.choice(characters) for _ in range(length))
    
    return otp

# Example usage: Generate a 6-digit OTP
otp = generate_otp(6)
print(f"Your OTP is: {otp}")