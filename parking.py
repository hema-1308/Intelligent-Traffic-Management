Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time

def delay(milliseconds):
    time.sleep(milliseconds / 1000.0)

... def upload(x, y, z, p):
...     # Simulate data uploading
...     print(f"Data uploaded successfully: x={x}, y={y}, z={z}, p={p}")
... 
... def main():
...     print("Starting simulation...")
... 
...     cnt = 0
...     while True:
...         try:
...             sen1 = int(input("Enter simulated sensor 1 value (0 or 1): "))
...             sen2 = int(input("Enter simulated sensor 2 value (0 or 1): "))
...             sen3 = int(input("Enter simulated sensor 3 value (0 or 1): "))
...             sen4 = int(input("Enter simulated sensor 4 value (0 or 1): "))
...             sen5 = int(input("Enter simulated sensor 5 value (0 or 1): "))
... 
...             # Simulate LCD output
...             print(f"S1: {sen1} | S2: {sen2} | S3: {sen3} | S4: {sen4}")
... 
...             delay(500)
...             cnt += 1
...             if cnt > 10:
...                 cnt = 0
...                 print("Uploading data to ThingSpeak...")
...                 upload(sen1, sen2, sen3, sen4)
...                 print("Data uploaded.")
... 
...             # Simulate servo control
...             if sen5 == 0:
...                 print("Servo control activated.")
...                 # Control servo logic can go here
... 
...             continue_simulation = input("Do you want to continue simulation? (yes/no): ").strip().lower()
...             if continue_simulation != "yes":
...                 print("Simulation ended.")
...                 break
...         except ValueError:
...             print("Invalid input. Please enter 0 or 1 for sensor values.")
... 
... if __name__ == "__main__":
...     main()
