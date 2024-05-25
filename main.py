# Task 1: Finding the longest word, total characters,
# writing the shortest two words to separate files,
# and printing the length of each word.
def targil1 () :
    with open("C:\\Users\\Zoey\\python2.txt", 'r') as file: print(max(file.read().split(), key=len))

    print(sum(len(word) for word in open("C:\\Users\\Zoey\\python2.txt").read().split()))

    with open("C:\\Users\\Zoey\\python2.txt", 'r') as shortest_two, open("shortest1.txt", 'w') as f1, open("shortest2.txt",
                                                                                                     'w') as f2:
        words = sorted(shortest_two.read().split(), key=len)[:2]
        f1.write(words[0]);
        f2.write(words[1])

    print(open("shortest1.txt").read(), open("shortest2.txt").read(), sep='\n')


    with open("C:\\Users\\Zoey\\python2.txt", 'r') as infile, open("name_length.txt", 'w') as outfile:
        outfile.writelines(f"{len(word)}\n" for word in infile.read().split())
    print(open("name_length.txt").read())


    name_length = int(input("Enter the name length: "))
    print(*[name for name in open("C:\\Users\\Zoey\\python2.txt", 'r').read().split() if len(name) == name_length], sep='\n')


# Task 2: Animal classes and main function
class Animal:
    # Base class for animals
    zoo_name = "Hayaton"

    def __init__(self, name_, hunger_=0):
        # Initializing an animal with a name and hunger level
        self.name_ = name_
        self.hunger_ = hunger_


    def get_name(self):
        return self.name_

    def is_hungry(self):
        return self.hunger_ > 0

    def feed(self):
        if self.hunger_ > 0:
            self.hunger_ -= 1

    def talk(self):
        pass

    def perform_special_action(self):
        pass

class Dog(Animal):
    # Dog subclass inheriting from Animal
    def talk(self):
        print("woof woof")
    def fetch_stick(self):
        print("There you go, sir!")
    def perform_special_action(self):
        self.fetch_stick()

class Cat(Animal):
    # Cat subclass inheriting from Animal
    def talk(self):
        print("meow")
    def chase_laser(self):
        print("Meeeeow")
    def perform_special_action(self):
        self.chase_laser()

class Skunk(Animal):
    # Skunk subclass inheriting from Animal
    def __init__(self, name_, hunger_=0, stink_count=6):
        super().__init__(name_, hunger_)
        self._stink_count = stink_count
    def talk(self):
        print("tsssss")
    def stink(self):
        print("Dear lord!")
    def perform_special_action(self):
        self.stink()

class Unicorn(Animal):
    # Unicorn subclass inheriting from Animal
    def talk(self):
        print("Good day, darling")
    def sing(self):
        print("I'm not your toy...")
    def perform_special_action(self):
        self.sing()

class Dragon(Animal):
    # Dragon subclass inheriting from Animal
    def __init__(self, name_, hunger_=0, color="Green"):
        super().__init__(name_, hunger_)
        self._color = color
    def talk(self):
        print("Raaaawr")
    def breath_fire(self):
        print(f"{self._color} dragon says: $@#$#@$$")
    def perform_special_action(self):
        self.breath_fire()

def main_2():
    # Main function for interacting with animal instances and demonstrating their behavior
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450, "Red"),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80, "Green")
    ]

    for animal in zoo_lst:
        print(f"{type(animal).__name__} {animal.get_name()}")
        if animal.is_hungry():
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        animal.perform_special_action()

    print(f"The zoo is named: {Animal.zoo_name}")


# Task 3: Username and password validation classes and functions
import re
import string

# Exception classes
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, index):
        self.char = char
        self.index = index
        super().__init__(f"The username contains an illegal character '{char}' at position {index + 1}")

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, index):
        message = f"The username contains an illegal character '{char}' at position {index + 1}"
        super().__init__(message)

class UsernameTooShort(Exception):
    def __init__(self):
        message = "Username is too short; it must be at least 3 characters."
        super().__init__(message)

class UsernameTooLong(Exception):
    def __init__(self):
        message = "Username is too long; it must not exceed 16 characters."
        super().__init__(message)

class PasswordMissingCharacter(Exception):
    def __init__(self, message="The password is missing a character"):
        super().__init__(message)

class MissingUppercase(PasswordMissingCharacter):
    def __init__(self):
        super().__init__("The password is missing a character (Uppercase)")

class MissingLowercase(PasswordMissingCharacter):
    def __init__(self):
        super().__init__("The password is missing a character (Lowercase)")

class MissingDigit(PasswordMissingCharacter):
    def __init__(self):
        super().__init__("The password is missing a character (Digit)")

class MissingSpecial(PasswordMissingCharacter):
    def __init__(self):
        super().__init__("The password is missing a character (Special)")

class PasswordTooShort(Exception):
    def __init__(self):
        message = "Password is too short; it must be at least 8 characters."
        super().__init__(message)

class PasswordTooLong(Exception):
    def __init__(self):
        message = "Password is too long; it must not exceed 40 characters."
        super().__init__(message)


def check_input(username, password):
    # Function to check the validity of a username and password based on specified criteria.
    if not re.match(r'^[a-zA-Z0-9_]*$', username):
        for idx, char in enumerate(username):
            if not re.match(r'[a-zA-Z0-9_]', char):
                raise UsernameContainsIllegalCharacter(char, idx)
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()

    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

    uppercase = any(c in string.ascii_uppercase for c in password)
    lowercase = any(c in string.ascii_lowercase for c in password)
    number = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    if not uppercase:
        raise MissingUppercase()
    if not lowercase:
        raise MissingLowercase()
    if not number:
        raise MissingDigit()
    if not special:
        raise MissingSpecial()

    print("OK")

def main_3():
    # Main function for checking username and password validity based on specified criteria
    try:
        check_input("A_a1.", "12345678")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "abcdefghijklmnop")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "ABCDEFGHIJLKMNOP")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "ABCDEFGhijklmnop")
    except Exception as e:
        print(e)

    try:
        check_input("A_1", "4BCD3F6h1jk1mn0p")
    except Exception as e:
        print(e)

    while True:
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            check_input(username, password)
            print("OK - Your username and password meet the requirements.")
            break
        except Exception as e:
            print(e)
            print("Please try again.")



#targil mesakem 4

def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for minute in range(60):
        yield minute

def gen_hours():
    for hour in range(24):
        yield hour

def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"


def gen_years(start=2019):
    while True:
        yield start
        start += 1

def gen_months():
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year):
    days_in_month = 31 if month in (1, 3, 5, 7, 8, 10, 12) else 30 if month in (4, 6, 9, 11) else 29 if leap_year else 28
    for day in range(1, days_in_month + 1):
        yield day

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def gen_date(start_year=2019):
    for year in gen_years(start_year):
        for month in gen_months():
            for day in gen_days(month, is_leap_year(year)):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"

def main_4():
    # Example usage of the gen_date function
    date_generator = gen_date(2019)
    for _ in range(20):
        print(next(date_generator))

    date_generator = gen_date(2019)


    for i, date in enumerate(date_generator, 1):
        if i % 1000000 == 0:
            print(date)
            if i >= 5000000:
                break


# Task 5: ID number validation and generation
def check_id_valid(id_number):
    # Function to check the validity of an ID number
    return sum(int(digit) if i % 2 != 0 else (int(digit) * 2 if int(digit) * 2 < 10 else sum(map(int, str(int(digit) * 2)))) for i, digit in enumerate(str(id_number), 1)) % 10 == 0

class IDIterator:
    # Iterator class for generating valid ID numbers
    def __init__(self, id_):
        self.id_ = id_

    def __iter__(self):
        return self

    def __next__(self):
        if self.id_ > 999999999:
            raise StopIteration
        else:
            current_id = self.id_ + 1
            while not check_id_valid(current_id):
                current_id += 1
            self.id_ = current_id
            return current_id


def id_generator(id_):
    # Generator function for generating valid ID numbers
    while id_ <= 999999999:
        current_id = id_ + 1
        while not check_id_valid(current_id):
            current_id += 1
        id_ = current_id
        yield current_id


def main_5():
    # Main function for user interaction and demonstrating ID generation using iterator or generator
    user_id = int(input("Enter an ID number (9 digits): "))
    while True:
        user_choice = input("Enter 'it' for iterator or 'gen' for generator: ")

        if user_choice == "it":
            iterator = IDIterator(user_id)
            print("Using iterator to generate 10 new ID numbers:")
            for _ in range(10):
                print(next(iterator))
            break

        elif user_choice == "gen":
            generator = id_generator(user_id)
            print("Using generator to generate 10 new ID numbers:")
            for _ in range(10):
                print(next(generator))
            break

        else:
            print("Invalid choice. Please enter 'it' or 'gen'.")



# Task 6: Drawing an image of an animal
from PIL import Image, ImageDraw

def call_draw():
    # Function to call draw_animal function to draw an image of an animal
    first = (
        146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
        355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
        178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
        307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
        199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
        389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
        216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
        365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
        215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
        290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
        279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
        291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
        306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
        393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
        336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
        259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
        349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
        234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
        339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
        122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
        214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
        134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
        171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
        115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
        89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108, 132,
        110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149, 77, 155,
        81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111, 156, 113, 170,
        115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259, 136, 266, 139,
        276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153, 366, 149, 379,
        147, 394, 146, 399
    )

    second = (
        146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
        355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
        178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
        307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
        199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
        389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
        216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
        365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
        215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
        290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
        279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
        291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
        306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
        393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
        336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
        259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
        349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
        234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
        339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
        122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
        214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
        134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
        171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
        115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
        89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108,
        132, 110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149,
        77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111,
        156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259,
        136, 266, 139, 276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153,
        366, 149, 379, 147, 394, 146, 399
    )

    draw_animal(first, second)


def draw_animal(first, second):
    # Function to draw an image of an animal using given points
    img = Image.new('RGB', (800, 600), 'white')  # Adjust size as necessary
    draw = ImageDraw.Draw(img)

    def draw_lines(points, color):
        if len(points) % 2 != 0:
            raise ValueError("Points list must contain an even number of elements.")
        point_pairs = [(points[i], points[i+1]) for i in range(0, len(points), 2)]
        for j in range(len(point_pairs) - 1):
            draw.line([point_pairs[j], point_pairs[j+1]], fill=color, width=2)

    draw_lines(first, 'pink')
    draw_lines(second, 'pink')


    img.save('animal.png')
    img.show()


if __name__ == "__main__":
    print(targil1())
    print(main_2())
    print(main_3())
    print(main_4())
    print(main_5())
    call_draw()




