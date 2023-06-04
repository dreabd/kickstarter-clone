from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        first_name="Demo",
        last_name="User",
        bio="Demo is an innovative startup revolutionizing the world of product trials. Founded in 2022, Demo connects consumers with a diverse range of companies offering exclusive trial experiences for their latest products. By seamlessly bridging the gap between businesses and potential customers, Demo is reshaping the way people discover, experience, and provide feedback on cutting-edge innovations.",
        username='Demo',
        email='demo@aa.io',
        password='password',
        city="Tacoma",
        state="WA"
    )
    marnie = User(
        first_name="Mary",
        last_name="Nguyen",
        bio="Marnie, a visionary illustrator with an unmatched flair for storytelling, is on a mission to bring her imaginative creations to life through Kickstarter. With a portfolio brimming with whimsy and wonder, Marnie captivates audiences with her unique blend of vibrant colors and intricate details. Back Marnie's Kickstarter campaign to embark on a visual journey filled with enchanting characters, captivating narratives, and the magic of art.",
        username='marnie',
        email='marnie@aa.io',
        password='password',
        city="Albany",
        state="NY"
    )
    bobbie = User(
        first_name="Robert",
        last_name="Smith",
        bio="Bobbie, a visionary creator at the intersection of technology and design, is launching an exciting Kickstarter campaign to bring his innovative products to the world. With an unwavering commitment to both functionality and aesthetics, Bobbie's designs seamlessly integrate cutting-edge technology into sleek and intuitive devices. Join Bobbie's Kickstarter journey to support the birth of groundbreaking tech products that elevate the user experience and redefine what's possible in the realm of design and technology.",
        username='bobbie',
        email='bobbie@aa.io',
        password='password',
        city="Chicago",
        state="IL"
    )
    user4 = User(
        first_name="Penelope",
        last_name="Frankel",
        bio="Penelope Frankel is a passionate and talented artist based in the vibrant city of Seattle. With a deep love for creativity and an unwavering dedication to her craft, Penelope has embarked on a mission to bring her unique artistic visions to life through several exciting Kickstarter campaigns.Drawing inspiration from the beautiful landscapes of the Pacific Northwest, Penelope's art captures the essence of nature and the human experience. Her captivating works blend elements of realism and abstract expressionism, resulting in thought-provoking pieces that evoke a wide range of emotions. Driven by a desire to connect with her audience on a profound level, Penelope utilizes various mediums, including painting, sculpture, and mixed media, to push the boundaries of artistic expression.",
        username='penelope',
        email='penelope@aa.io',
        password='password',
        city="Seattle",
        state="WA"
    )
    user5 = User(
        first_name="Sylvester",
        last_name="McKinney",
        bio="By launching multiple Kickstarter campaigns, Sylvester is likely seeking funding for various artistic endeavors or projects. Kickstarter allows artists to showcase their work, set funding goals, and offer rewards to backers who pledge money towards the campaigns. It's an excellent way for artists to gain financial support, generate buzz for their projects, and engage with their audience.",
        username='sylvester',
        email='sylvester@aa.io',
        password='password',
        city="Atlanta",
        state="GA"
    )

    user6 = User(
        first_name="Mikhail",
        last_name="Bulgakov",
        bio="I am here to find support for a number of different projects ranging from tech and design to film. I have successfully had several projects funded in the past and hope to find more success. Thank you in advance for all your support!",
        username='MikBoi666',
        email='Mikhail@cbp.com',
        password='password',
        city="New York City",
        state="NY"
    )

    user7 = User(
        first_name="Nikolai",
        last_name="Gogol",
        bio="Hello! My name is Nikolai and I am from Chicago, IL. I have recently launched several campaigns on Kickstarter looking for support for my tech, dsign, and film projects. I thank you in advance for your support!",
        username='GoGoGogol',
        email='Gogol@cbp.com',
        password='password',
        city="Chicago",
        state="IL"
    )

    user8 = User(
        first_name = "Frankly",
        last_name = "Delicious",
        bio = "Frankly Delicious is an exceptional company merging the worlds of gastronomy and gaming with their mouthwatering creations. With a passion for crafting delectable treats and immersive gaming experiences, they are launching an exciting Kickstarter campaign to introduce their unique line of food and game products. Back Frankly Delicious on Kickstarter to savor the blend of tantalizing flavors and thrilling adventures, as they redefine the way we indulge in both gastronomy and gaming.",
        username='frankly',
        email='frankly@email.io',
        password='password',
        city = "Seattle",
        state = "WA"
        )

    user9 = User(
        first_name = "Innovators",
        last_name = "LLC",
        bio = "Innovators, a trailblazing company at the forefront of culinary and gaming innovation, is set to revolutionize the way we experience food and entertainment through their captivating creations. With a relentless drive to push boundaries, Innovators is launching an exhilarating Kickstarter campaign to introduce their groundbreaking line of food and game products. Embrace the fusion of tantalizing flavors and immersive gameplay by supporting Innovators on Kickstarter, and join them on their mission to redefine the boundaries of culinary and gaming experiences.",
        username='innovators',
        email='innovators@email.io',
        password='password',
        city = "Boston",
        state = "MA"
        )
    user10 = User(
        first_name="Ethan",
        last_name="Reynolds",
        bio="I am a visionary music producer hailing from the vibrant city of Los Angeles. With an innate ear for sonic artistry, I crafted a distinct sound that seamlessly blends genres and pushes the boundaries of contemporary music. My electrifying productions have garnered critical acclaim, propelling him to the forefront of the LA music scene, where he continues to inspire and captivate audiences with his unparalleled creativity.",
        username='ER_Records',
        email='ethan@gmail.com',
        password='password',
        city="Los Angeles",
        state="CA"
    )

    user11 = User(
        first_name="Olivia",
        last_name="Thompson",
        bio="I am esteemed publisher making waves in the literary world from her base in Seattle. With a passion for storytelling and an unwavering commitment to nurturing emerging voices, I built a reputable publishing house known for its diverse and thought-provoking titles. My keen editorial eye and strategic approach have led to numerous bestsellers, cementing my status as a prominent figure in the thriving literary community of Seattle.",
        username='OT_Publishing',
        email='olivia@gmail.com',
        password='password',
        city="Seattle",
        state="Washington"
    )

    jen = User(
        first_name = "Jen",
        last_name = "Samuel",
        bio = "Interested in tech products",
        username='jen',
        email='jen@email.io',
        password='password',
        city = "Tuscon",
        state = "AZ"
)

    alan = User(
        first_name = "Alan",
        last_name = "Branden",
        bio = "Interested in gaming projects",
        username='alan',
        email='alan@email.io',
        password='password',
        city = "Milwaukee",
        state = "WI"
)

    charlie = User(
        first_name = "Charlie",
        last_name = "Kayson",
        bio = "Interested in design projects",
        username='charlie',
        email='charlie@email.io',
        password='password',
        city = "Las Vegas",
        state = "NV"
)

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user10)
    db.session.add(user11)
    db.session.add(jen)
    db.session.add(charlie)
    db.session.add(alan)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
