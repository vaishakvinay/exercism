import random
import string


class Robot:
    used_names = set()

    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        while True:
            letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
            numbers = str(random.randint(100, 999))
            name = letters + numbers

            if name not in Robot.used_names:
                Robot.used_names.add(name)
                return name

    def reset(self):
        self.name = self.generate_name()
