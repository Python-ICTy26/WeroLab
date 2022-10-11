def get_greeting(name: str) -> str:
    a = "Hello, " + name + "!"
    return a


if __name__ == "__main__":
    message = get_greeting("World")
    print(message)
