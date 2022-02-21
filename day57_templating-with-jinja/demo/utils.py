import requests


def guess_func(name: str):
    request_parameters = {
        "name": name
    }
    gender_request = requests.get(url="https://api.genderize.io", params=request_parameters)
    gender_request.raise_for_status()
    gender_data = gender_request.json()
    print(gender_data)

    age_request = requests.get(url="https://api.agify.io", params=request_parameters)
    age_request.raise_for_status()
    age_data = age_request.json()
    print(age_data)

    name = name.title()

    return {"name": name, "gender": gender_data["gender"], "age": age_data["age"]}
