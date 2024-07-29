import sys
import platform
import os
import requests

def main():
    print("Python version:")
    print(sys.version)
    print("\nPlatform information:")
    print(platform.platform())
    
    print("\nCurrent working directory:")
    print(os.getcwd())
    
    print("\nContents of current directory:")
    print(os.listdir())
    
    print("\nTesting internet connectivity:")
    try:
        response = requests.get("https://www.wikipedia.org")
        print(f"HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting AWS EC2 metadata:")
    try:
        response = requests.get("http://169.254.169.254/latest/meta-data/instance-id")
        print(f"EC2 Instance ID: {response.text}")
    except Exception as e:
        print(f"Error accessing EC2 metadata: {e}")

if __name__ == "__main__":
    main()