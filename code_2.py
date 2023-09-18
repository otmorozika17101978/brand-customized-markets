
def generate_random_data():
    random_string = 'His law range thing see energy least.'
    random_number = 67

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: His law range thing see energy least.")
        print(f"Random Number: 67")

if __name__ == "__main__":
    main()
