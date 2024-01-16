x = 1000


def mitt_namn():
    print("Modulens namn är:", __name__)


def main():
    print("Jag är huvudprogrammet!")
    mitt_namn()


if __name__ == "__main__":
    main()
