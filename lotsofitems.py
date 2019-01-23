from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
user1 = User(name="Ahmed Zaki", email="ahmedmohamedzaki217@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for Soccer
category1 = Category(name="soccer", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="ball", user_id=1, description="simple description", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="kit", user_id=1,  description="simple description", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="goal keeper gloves", user_id=1, description="simple description", category=category1)

session.add(item3)
session.commit()

# Items for PingPong
category2 = Category(name="Ping Pong", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Rackets", user_id=1, description="simple description", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="table", user_id=1,  description="simple description", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="net", user_id=1, description="simple description", category=category2)

session.add(item3)
session.commit()

# Items for Basket Ball
category3 = Category(name="Basket Ball", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="basket ball", user_id=1, description="simple description", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="basket", user_id=1, description="simple description", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="kit", user_id=1, description="simple description", category=category3)

session.add(item3)
session.commit()



print("Item added successfully!")
    
    	