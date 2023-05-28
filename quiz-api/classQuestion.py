

class Question:
    def __init__(self,id, title, text, image, position, possible_answers):
        self.id = id
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.possible_answers = possible_answers