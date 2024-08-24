import requests
from datetime import datetime

USERNAME = "dongminkim"
TOKEN = "dave885588"
GRAPH_ID = "graph1"
TODAY = datetime.date(datetime.today()).strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


class Pixela:
    def __init__(self):
        num = int(input("Which move do you want to make?\n"
                    "1. Post\n2. Update\n3. Delete\n4. None\nType here => "))

        if num == 1:
            self.post()
        if num == 2:
            self.update()
        if num == 3:
            self.delete()
        if num == 4:
            print("Program closing..")
            exit()

    def post(self):
        post_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

        post_config = {
            "date": TODAY,
            "quantity": input("How many minutes did you code today? "),
        }

        response = requests.post(url=post_endpoint, json=post_config, headers=headers)
        print(response.text)

    def update(self):
        update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

        update_config = {
            "quantity": input("How many minutes did you code today? "),
        }

        response = requests.put(url=update_endpoint, json=update_config, headers=headers)
        print(response.text)

    def delete(self):
        delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

        response = requests.delete(url=delete_endpoint, headers=headers)
        print(response.text)


start = Pixela()