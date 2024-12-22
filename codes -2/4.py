class Bird:
    def fly(self):
        return "Flying!"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly!")

def let_bird_fly(bird: Bird):
    try:
        print(bird.fly())
    except NotImplementedError as e:
        print(e)

let_bird_fly(Bird())       # Flying!
let_bird_fly(Penguin())    # Penguins can't fly!