from typing import Dict, List, Union
from util import runall
from importlib import import_module


def exercise6():
    def city_country(city: str, country: str) -> str:
        return f"{city.capitalize()}, {country.capitalize()}"

    print(city_country("regina", "canada"))
    print(city_country("paris", "france"))
    print(city_country("washington", "united states"))


def exercise7():
    def make_album(
            artist: str,
            album: str,
            n_songs: Union[int, None] = None) -> Dict[str, Union[str, int]]:
        dict: Dict[str, Union[str, int]] = {"artist": artist, "album": album}
        if n_songs:
            dict["n_songs"] = n_songs
        return dict

    print(make_album("21 Savage", "SAVAGE MODE II"))
    print(make_album("Lil Tecca", "Virgo World"))
    print(make_album("DaBaby", "BLAME IT ON BABY (DELUXE)"))
    print(make_album("Juice WRLD", "Legends Never Die", 22))


def exercise8():
    def make_album(
            artist: str,
            album: str,
            n_songs: Union[int, None] = None) -> Dict[str, Union[str, int]]:
        dict: Dict[str, Union[str, int]] = {"artist": artist, "album": album}
        if n_songs:
            dict["n_songs"] = n_songs
        return dict

    print("Enter quit at any time to exit")
    while True:
        album = input("Enter the album name: ")
        if album.lower() == "quit":
            break
        artist = input("Enter the artist name: ")
        if artist.lower() == "quit":
            break
        print(make_album(album, artist))


def exercise9():
    list = ["Hello there!", "How are you doing?", "I am good."]

    def send_messages():
        for text in list:
            print(text)

    send_messages()


def exercise10():
    list = ["Hello there!", "How are you doing?", "I am good."]
    sent_messages = []

    def send_messages(messages: List[str]):
        while messages:
            text = messages.pop()
            print(text)
            sent_messages.append(text)

    send_messages(list)
    print(list)
    print(sent_messages)


def exercise11():
    list = ["Hello there!", "How are you doing?", "I am good."]
    sent_messages = []

    def send_messages(messages: List[str]):
        while messages:
            text = messages.pop()
            print(text)
            sent_messages.append(text)

    send_messages(list[:])
    print(list)
    print(sent_messages)


def exercise12():
    def sandwich(*ingredients: str):
        print("Sandwich ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")

    sandwich("ham")
    sandwich("ham", "cheese")
    sandwich("ham", "cheese", "lettuce")


def exercise13():
    def build_profile(first: str, last: str,
                      **user_info: str) -> Dict[str, str]:
        return {
            "first_name": first,
            "last_name": last,
            **user_info,
        }

    user_profile = build_profile('arden',
                                 'arden',
                                 age="17",
                                 favorite_color="blue",
                                 instrument="guitar")
    print(user_profile)


def exercise14():
    def make_car(manufacturer: str, model: str,
                 **other: str) -> Dict[str, str]:
        return {
            "manufacturer": manufacturer,
            "model": model,
            **other,
        }

    car = make_car("subaru", "outback", color="blue")
    print(car)


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
