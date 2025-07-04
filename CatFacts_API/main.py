import requests as req

print("Cat Facts Generator using an API")
print()
def gene():
    url = "https://catfact.ninja/fact"

    try:
        response = req.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"🐱 Cat Fact: {data['fact']}")
        else :
            print(f"Error: Received status code {response.status_code}")

    except req.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        gene()
        choose = input("Do you want another cat fact? (y/n): ").lower()

        if choose == 'y':
            print()
        else :
            print()
            print("Thanks for using Cat Facts Generator!")
            break

if __name__ == "__main__":
    main()

