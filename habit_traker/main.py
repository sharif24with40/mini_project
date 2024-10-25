import os
import requests
from datetime import datetime
import logging

# Load sensitive data from environment variables
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

# Check for missing environment variables
if not USERNAME or not TOKEN or not GRAPH_ID:
    raise ValueError("Environment variables PIXELA_USERNAME, PIXELA_TOKEN, and PIXELA_GRAPH_ID must be set.")

# Endpoints
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
headers = {
    "X-USER-TOKEN": TOKEN
}

# Set up logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    handle_response(response, "User creation")

def create_graph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    handle_response(response, "Graph creation")

def get_valid_quantity():
    while True:
        try:
            quantity = float(input("How many kilometers did you cycle today? "))
            if quantity >= 0:
                return str(quantity)
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def add_pixel(quantity):
    today = datetime.now().strftime("%Y%m%d")
    pixel_data = {
        "date": today,
        "quantity": quantity,
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    handle_response(response, "Pixel creation")

def update_pixel(date, quantity):
    update_endpoint = f"{pixel_creation_endpoint}/{date}"
    new_pixel_data = {
        "quantity": quantity
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    handle_response(response, "Pixel update")

def delete_pixel(date):
    delete_endpoint = f"{pixel_creation_endpoint}/{date}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    handle_response(response, "Pixel deletion")

def view_graph_data():
    response = requests.get(url=pixel_creation_endpoint, headers=headers)
    handle_response(response, "View graph data")
    data = response.json()
    if response.status_code == 200:
        print("Current Graph Data:")
        for pixel in data['pixels']:
            print(f"Date: {pixel['date']} - Quantity: {pixel['quantity']} Km")
    else:
        print("Failed to retrieve graph data.")

def view_graph_url():
    graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"
    print(f"View your graph online at: {graph_url}")

def handle_response(response, action_name):
    if response.status_code == 200:
        print(f"\n{action_name} was successful!\n")
    else:
        print(f"\nError during {action_name}: {response.text}\n")
        logging.error(f"Error during {action_name}: {response.text}")

def main_menu():
    while True:
        print("===== Pixela Habit Tracker =====")
        print("1. Add today's cycling data")
        print("2. Update a past entry")
        print("3. Delete a past entry")
        print("4. View current graph data")
        print("5. View graph URL")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            quantity = get_valid_quantity()
            add_pixel(quantity)
        elif choice == '2':
            date = input("Enter the date to update (YYYYMMDD): ")
            quantity = get_valid_quantity()
            update_pixel(date, quantity)
        elif choice == '3':
            date = input("Enter the date to delete (YYYYMMDD): ")
            delete_pixel(date)
        elif choice == '4':
            view_graph_data()
        elif choice == '5':
            view_graph_url()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Please check the error log.")
