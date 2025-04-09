from extensions import db


class Dessert(db.Model):
    __tablename__ = 'desserts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, calories):
        self.name = name
        self.price = float(price)
        self.calories = int(calories)

    def calories_per_dollar(self):
        if self.price:
            return self.calories / self.price
        return 0


class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name


def create_dessert(new_name, new_price, new_calories):
    dessert = Dessert(new_name, new_price, new_calories)
    db.session.add(dessert)
    db.session.commit()
    return dessert
