from typing import Dict, List, Any
import requests
import os

def parse_data(user)-> Dict[str, Any]:
    if not user:
        raise ValueError("Error: User is Empty!!")
    KEY_API = os.getenv("KEY");
    URL = f"https://api.github.com/users/{user}"
    if not KEY_API:
        raise ValueError("The IPA Key is Empty !!")
    response = requests.get(URL);
    if response.ok:
        data: Dict[str, Any] = response.json()
    else: raise ValueError(f"Error: status {response.status_code}msg {response.reason} ") 

    return {
            "name" : data["login"],
            "Url" : data["url"],
            "realName" : data["name"],
            "Followers" : data["followers"],
            "create_time" :  data["created_at"],
            "Folowing" : data['following'],
            "bio" : data["bio"],
            "repos" : data['public_repos']
            };
def desplay_data(data: Dict[str, Any])-> None:
    print("=== github data ==")
    print(f"Name : {data['name']}");
    print(f"Url: {data['Url']}")
    print(f"Real Name: {data['realName']}")
    print(f"Followers: {data['Followers']}")
    print(f"Folowing: {data['Folowing']}")
    print(f"This account start in {data['create_time']}")
    print(f"Local repos: {data['repos']}")
    print(f"bio : {data['bio']}")
def main()-> None:
    user_name = input("Please Enter The User Name: ");
    try:
        data = parse_data(user_name.strip())
        desplay_data(data);
    except ValueError as e:
        print(e);
if __name__ == "__main__":
    main()
