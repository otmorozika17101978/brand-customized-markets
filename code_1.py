
def generate_random_data():
    random_string = 'Activity knowledge thing month yard run.'
    random_number = 72

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Activity knowledge thing month yard run.")
        print(f"Random Number: 72")

if __name__ == "__main__":
    main()
