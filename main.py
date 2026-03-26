# main.py
import os
import datetime

# Manual Trigger removed

def main():
    # Access secret from environment variable
    secret_value = os.environ.get('MY_SECRET', 'No secret found')

    # Get current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print hello world with secret and timestamp
    print("Hello World!")
    print(f"Current Time: {current_time}")
    print(f"Secret Value: {secret_value}")

    # Mask the secret in logs (optional but good practice)
    if secret_value != 'No secret found':
        print(f"Secret length: {len(secret_value)} characters")


if __name__ == "__main__":
    main()