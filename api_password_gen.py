import requests
import random

# Function to fetch a random word from an API
def get_random_word():
    url = "https://random-word-api.vercel.app/api?words=2&length=" + str(random.randint(4, 6))
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns the first random word
    else:
        raise RuntimeError(f"Failed to fetch word: {response.status_code}")

# Function to generate special characters
def generate_special_char():
    special_chars = ['!', '@', '#', '$', '%', '^', '*', '-', '_', '=', '+']
    return random.choice(special_chars)

# Function to generate a password
def generate_password():
    # Generate 3-5 lowercase words
    lowercase_words = get_random_word()[0].lower()
    
    # Generate 1 special character word
    special_char = generate_special_char()

    # Generate 3-5 uppercase words
    uppercase_words = get_random_word()[1].upper()

    # Construct the password
    password = lowercase_words + special_char + uppercase_words + special_char

    return password

# Example usage
# password = generate_password()
# print(f"Generated password: {password}")
