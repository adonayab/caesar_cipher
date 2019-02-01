from helpers import alphabet_position, rotate_character

def encrypt(text, rot):

    encrypted = ''

    for char in text:
        encrypted = encrypted + rotate_character(char, rot)

    return encrypted


def main():

    message = input('Type a message:\n')
    rot = int(input('Rotate by:\n'))

    print(encrypt(message, rot))


if __name__ == "__main__":
    main()
