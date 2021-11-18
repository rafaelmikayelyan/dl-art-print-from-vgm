def user_prompt_url():
    print("\nTo download an image, enter [Vangogh Museum's Poster URL: https://www.vangoghmuseum.nl/en/prints]")
    url = input("\nEnter [url] or press [return] to choose from defaults: ")

    while (url == "" and url != "1" and url != "2"):
        url = input("Enter [1-2] to download either 'Chat Noir' v1 or v2: ")
    return url


def user_prompt_resolution(data):
    print("\nAvailable resolutions:")
    if len(data["levels"]) == 1:
        return "0"
    for i in data["levels"]:
        print("({}) {}x{}".format(data["levels"].index(i), i['width'], i['height']))
    return input("\nPress [return] for the highest resolution or type [0-{}]: ".format(len(data["levels"])-1))


def user_prompt_name(exists=False, filename=""):
    if exists:
        return input(f'"{filename}" already exists, please enter different name: ')
    return input("\nPress [return] or enter custom name for the image: ")


def notify_user(message):
    print(message)