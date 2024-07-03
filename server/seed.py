# #!/usr/bin/env python3

# from app import app, db
# from models import  Plant


# with app.app_context():

#     Plant.query.delete()

#     aloe = Plant(
#         id=1,
#         name="Aloe",
#         image="./images/aloe.jpg",
#         price=11.50,
#         is_in_stock=True,
#     )

#     zz_plant = Plant(
#         id=2,
#         name="ZZ Plant",
#         image="./images/zz-plant.jpg",
#         price=25.98,
#         is_in_stock=False,
#     )

#     db.session.add_all([aloe, zz_plant])
#     db.session.commit()


from app import app, db
from models import Plant

def seed_data():
    plant1 = Plant(name='Aloe', image='./images/aloe.jpg', price=11.50, is_in_stock=True)
    db.session.add(plant1)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
