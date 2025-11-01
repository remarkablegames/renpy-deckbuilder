init python:
    class Emojis:
        emojis = {
            "0": "0️⃣",
            "1": "1️⃣",
            "2": "2️⃣",
            "3": "3️⃣",
        }

        def get(self, key) -> str:
            return self.emojis.get(str(key))


    emojis = Emojis()
