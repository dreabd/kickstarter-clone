from app.models import db, Project, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date
from random import randint,choice


def seed_projects():
    food1 = Project(
        project_name="Estate 98 Ultra-Concentrated Coffee: Make Coffee Your Way",
        description="Use a few drops to create hot or iced coffee, lattes & more in seconds | Experience the richness of El Salvadors finest coffee beans.",
        category_id=5,
        money_goal=10000,
        user_id=8,
        city="Miami",
        state="FL",
        story="Estate 98 coffee beans have been cultivated on volcanic soil and picked by hand for six generations in the lush mountains of El Salvador. We are proud to introduce our 10x ultra-concentrated coffee, which offers the most exquisite flavor and quality. Now you can experience the full potential of your creativity by adding just a few drops of our premium liquid ultra-concentrated coffee to your favorite drink! At Estate 98, our 100 percent strictly high-grown Arabica coffee (Bourbon varietal) is picked individually by hand and dried on patios; honoring the age-old processing method for the most exquisite coffee flavor and quality.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_1_coffeeconcentrate.png",
        end_date=date(2024, 6, 23),
        reward_name="Super Early Bird | Estate 98 4-pack",
        reward_amount=72,
        reward_description="Back this reward for four (4) bottles of Estate 98. Perfect for those who travel, a family of coffee drinkers and those who feel like gifting something great."
    )

    food2 = Project(
        project_name="Curbside to Dine-In: Help Buddy's Chicken & Waffles Expand!",
        description="After almost two years of operating in ghost kitchens, we are ready to open our flagship location right here in Tacoma!",
        category_id=5,
        money_goal=40000,
        user_id=9,
        city="Tacoma",
        state="WA",
        story="When I made the move from Baltimore to Tacoma in January 2020, I had no clue where life would take me. Little did I know that a pandemic would spark the idea for Buddy's—a small coffee shop serving fried chicken and variety of waffles. As someone who always had a passion for cooking but lacked confidence, I honestly thought the waffles would be the star of the show. Shockingly, the fried chicken recipe that I developed after years of watching Mommie & Grandma in the kitchen is what got Buddys featured on the evening news. Now, we need your help to make this dream a reality. With this Kickstarter campaign, we aim to establish Buddys Chicken & Waffles as the go-to destination for incredible chicken and waffles in the entire state of Washington. Your support will enable us to secure the new space, equip the kitchen, and create an unforgettable dining experience that honors Uncle Thurms' 16-year legacy.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_2_chicken_waffles.png",
        end_date=date(2023, 11, 10),
        reward_name="Chicken & Waffles and a Sticker!",
        reward_amount=25,
        reward_description="Try any one of our 9 different waffles with our famous fried chicken AND get a shiny new sticker!"
    )

    food3 = Project(
        project_name="Frankly Delicious - Mini Chocolate Bars",
        description="Chocolate made from ethically and sustainably sourced cocoa and other ingredients, but small.",
        category_id=5,
        money_goal=2500,
        user_id=8,
        city="Leeds",
        state="WA",
        story="Frankly Delicious is a group of artisan chocolate makers who make chocolate from scratch using ethically sourced cocoa. Unfortunately, most chocolate is made from cocoa that has been grown by farmers who earn less than $2 a day and often rely on illegal child labour. All of the cocoa we use to make our chocolate is grown by cocoa farmers who earn a fair price for their crop and because of this can hire qualified workers when needed. Right now we sell 10 different chocolate bars, with new, limited edition flavoured being added each month, and they are 60g bars. As well as using ethically sourced cocoa, all of our ingredients and flavourings are fully natural. From locally roasted coffee in our coffee white chocolate bar to freeze dried fruits in bars like our raspberry white chocolate alternative and blackcurrant dark chocolate bars.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_3_frankly_chocolate_bars.png",
        end_date=date(2024, 3, 12),
        reward_name="4 Bars - Vegan - Most Popular",
        reward_amount=19,
        reward_description="1x Madagascar 70 percent dark chocolate bar, 1x Oat m!lk chocolate bar, 1x Coconut m!lk chocolate bar, 1x Raspberry white chocolate alternative bar"
    )

    food4 = Project(
        project_name="The Sourdough Framework",
        description="Master the art of sourdough baking at home with this comprehensive guide, covering science, basics, and advanced techniques.",
        category_id=5,
        money_goal=14500,
        user_id=9,
        city="Hamburg",
        state="NY",
        story="Gluten Tag. I'm a German software engineer and passionate bread nerd.  My mission is to democratise baking by enabling everyone around the world to bake delicious bread at home. Right now when you follow online recipes to bake bread (and even more so sourdough) you will likely fail. The flour is different, you use different yeast strains and you work with different temperatures. For this reason I have started The Bread Code - a YouTube channel that dives deeper into bread making at looks at the science and why behind the process. By understanding what's happening in the background I enable you to bake delicious bread at home in your environment.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_4_sourdough.jpeg",
        end_date=date(2023, 10, 2),
        reward_name="Physical book and sourdough infographic",
        reward_amount=70,
        reward_description="You'll receive the physical version of the book and a handy poster of a sourdough info graphic that assists you with daily tasks in the kitchen."
    )

    food5 = Project(
        project_name="Grazed Snax: A pastured based snack line.",
        description="We are regenerative farmers launching a snack line. Starting with an original pork stick made from 100% pasture-raised pork, sugar free.",
        category_id=5,
        money_goal=29000,
        user_id=8,
        city="Durham",
        state="NC",
        story="In 2019 the farm started in our front yard with chickens. Withing 18 months we raised over 6,000 broilers and 100 hogs and finished 40 head of cattle. All our livestock rotates from pasture to pasture daily. Rotation spreads livestock fertility, minimizing fertilization needs and allowing for vegetation recovery. Each paddock is occupied less than half of the time. Keeping nutrients on-farm helps reduce the need for outside inputs. We want to expand Grass Grazed to make nutrient dense products accessible to consumers nationwide.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_5_grazed_snax.jpeg",
        end_date=date(2023, 11, 10),
        reward_name="Sticks + MERCH",
        reward_amount=50,
        reward_description="8 Original Pork Sticks + Farm T-shirt"
    )

    food6 = Project(
        project_name="Homefire Tea & Botanicals - Pour A Cup Of Comfort",
        description="Tea blends and medicinals that will bless you down to your bones.",
        category_id=5,
        money_goal=1500,
        user_id=9,
        city="Janesville",
        state="WI",
        story="Homefire Tea & Botanicals is a dream shared by two people who really love tea, plants, and taking care of folks. Combined we have over 30 years of experience studying, interacting with, and recommending plants for the benefit of the human experience. When they were asked for recommendations to help people deal with their problems or find a moment of quiet enjoyment, two things came up over and over: Tea and tinctures. Our initial blends have been perfected in small batches and are ready to debut.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_6_tea_botanicals.png",
        end_date=date(2023, 12, 5),
        reward_name="Simple Sample",
        reward_amount=10,
        reward_description="4 samples of your choice of blends (each makes about 3 cups)."
    )

    food7 = Project(
        project_name="Help Us Publish The Flavor Seed Organic Seasonal Cookbook",
        description="Follow our chef inspired, mother approved cookbook to create simple organic meals within 30 minutes.",
        category_id=5,
        money_goal=5000,
        user_id=8,
        city="Charlotte",
        state="NC",
        story="Our goal is to help families and individuals eat a non-processed food diet; quickly, easily deliciously, and organically. Our Organic blended seasonings do just that and while our flavors work great by just getting them on whatever you are cooking our fans kept asking for recipes. Not being a huge recipe guy, I sought out professional help. That's when fate and fortune aligned and Johnson & Wales University agreed to partner with Flavor Seed to not only help create this cookbook, but to help teach an entrepreneurship class and expose their students to real world small business challenges. Our team won the President's Award for most professional and rewarding experience.  While we did not complete the entire Flavor Seed Organic cookbook, we did produce the Summer edition of Flavor Seed recipes. Our Summer Cookbook (magazine) is also available as a digital download ebook.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_7_seed_cookbook.png",
        end_date=date(2023, 11, 15),
        reward_name="Printed Summer Cookbook (magazine)",
        reward_amount=15,
        reward_description="Get a printed version of the smaller organic summer recipe cookbook. This printed magazine-like copy will contain recipes for the summer and is a shorter version of the overall cookbook. This is a composition of the work produced this spring semester by the Johnson and Wales students. The full version of the cookbook will contain additional summer recipes as well as the remainder seasons. This is just a starter version."
    )

    food8 = Project(
        project_name="Ghost Bagel Food Truck",
        description="Ghost Bagel of Napa, California is buying a food truck!",
        category_id=5,
        money_goal=60000,
        user_id=9,
        city="Napa",
        state="CA",
        story="I grew up in New York state, eating bagels nearly every weekend from my town's multiple bagel shops.  After moving to Napa, I realized that a fresh bagel was one of the few things that we couldn't find here, so I started making them myself and got pretty good.  I decided to start a little bagel business and see where it went.  After a few years of delivering a few dozen bagels per day, last year, my friend joined me and we were able to multiply the number of bagels we make.  We started doing markets and popups and Ghost started growing. To keep the momentum, we are hoping to take steps to expand our production and our distribution.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_8_ghost_bagel.png",
        end_date=date(2023, 11, 20),
        reward_name="A dozen bagels!",
        reward_amount=50,
        reward_description="Get one dozen bagels whenever you'd like! (This reward is claimed at our food truck once it is open.)"
    )

    food9 = Project(
        project_name="Reyna Filipina Kitchen TACOMA",
        description="Where Brunch Flavors of the Philippines Reign Supreme",
        category_id=5,
        money_goal=71000,
        user_id=8,
        city="Tacoma",
        state="WA",
        story="Over the past five years, I have been sharing my love for Filipino food with the Tacoma community, and the response has been overwhelming. We have successfully operated a farmers market stand, offering fresh and distinct Filipino cuisine. Now, we am ready to take it to the next level and reach a wider audience by launching a new restaurant here in Tacoma. This restaurant, Reyna Filipina Kitchen TACOMA, which means queen in Filipino, is a tribute to my mother, Lucy, and other women who have inspired and supported me throughout my journey. We will be offering all-day brunch.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_9_filipino_restaurant.jpeg",
        end_date=date(2024, 1, 2),
        reward_name="Thank You Note From Chef Jan",
        reward_amount=20,
        reward_description="A heartfelt, handwritten Salamat: Thank you note from Chef Jan"
    )

    food10 = Project(
        project_name="milk & mochi — an Asian American bakery in Seattle, WA",
        description="Sister-owned pop up is opening a brick-and-mortar bakery in Fremont!",
        category_id=5,
        money_goal=50000,
        user_id=8,
        city="Seattle",
        state="WA",
        story="We started as a pop up in June 2022 with a little idea but a big love of food. We're Vietnamese American: born in Vietnam, raised in Southern California, and settled in Seattle. Our bakery is an expression of the in-between experience of being both Asian and American. We create desserts that are a bit Asian and a bit Western, with a unique mix of the two that represents who we are, and our name reflects that: milk (Western) & mochi (Asian)! We make desserts that hit the sweet spot in the middle: punchy flavors, not too sweet (the ultimate Asian compliment), and airy enough to feel light, but rich enough to feel a bit decadent.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_10_milk_mochi_bakery.png",
        end_date=date(2023, 12, 10),
        reward_name="Cream puff reservation",
        reward_amount=20,
        reward_description="Two cream puffs just for you! Backers will get access to make a reservation on the day of your choice (up to six months after opening). There will be a limited number of reservations per day."
    )

    food11 = Project(
        project_name="Herders to Home 2023: Luxury Mongolian Yarn and Fiber",
        description="Herders to Home, ULA+LIA procures fibers from free-range Mongolian animals to create world-class knitting yarn",
        category_id=5,
        money_goal=27500,
        user_id=9,
        city="Honolulu",
        state="HI",
        story="We've made it though winter in Mongolia and after a trip to see the herders providing our fiber for this season, I'm once again coming to the Kickstarter community to raise funds to reach our batch requirements and bring our beautiful Mongolian yarn and fiber to the rest of the world! Now as official partners of of the yak wool and two cashmere cooperatives we source our fibers from, I can't wait to visit them during the campaign to share our progres",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_11_mongolian_yarn.jpeg",
        end_date=date(2023, 11, 28),
        reward_name="Mongolian Wool/Cashmere Blend Yarn 200g",
        reward_amount=30,
        reward_description="With select sourcing through our cooperative partners for the soft, Sartuul sheep wool and expert processing, we are able to provide an incredibly soft and durable fiber that offers great value next to its more rare fiber relatives. Adding a 15 percent blend of our cashmere, the final products pick up some of the beautiful hand and loft that our cashmere is known for."
    )

    food12 = Project(
        project_name="ALIVE - The World's First Shower Bomb For Your Morning",
        description="ALIVE is the strongest shower bomb taken to market. An intense blend of essential oils and menthol to energize, decongest and focus.",
        category_id=5,
        money_goal=5600,
        user_id=8,
        city="Columbus",
        state="OH",
        story="The new ALIVE formula lasts longer and hits harder than ever before! Our new prototype bombs last around 15 minutes in the shower. Kick brain fog to the curb. Power through your day with clarity and focus. Peppermint has been shown to improve cognitive performance and alertness, strong menthol allows you to breather, and eucalyptus and pepperming are commonly known to increase dopamine.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_12_shower_bomb.jpeg",
        end_date=date(2023, 11, 30),
        reward_name="Kickstarter Special - 1 Pack of ALIVE",
        reward_amount=27,
        reward_description="Our new ALIVE Shower Bomb - Hits harder and last longer. The only way to wake up and hit the ground running, without having to change your daily routine."
    )

    game1 = Project(
        project_name="The Medusa Report",
        description="A thrilling tabletop puzzle adventure about a missing spy, a nuclear physicist and Cold War family secrets.",
        category_id=6,
        money_goal=12000,
        user_id=8,
        city="Juneau",
        state="AK",
        story="The Medusa Report is a tabletop puzzle game. A treasure trove of touch-real, confidential items from a Cold War infiltration mission. By yourself, or as a team of up to 4 players, you'll investigate a mysterious agency, uncover what really happened near Nikitagrad in 1974 and above all: find out where Abigail Vandermist is hiding! The game is entirely analog. Solve puzzles, study a tactical map, decode classified letters, unravel the secrets of an old floppy disk... (don’t worry, you won’t need a floppy drive). With each deciphered message, you'll uncover more of the story and find new clues for the next puzzle. No rule sheet. No time limit. No envelopes saying 'Don't open me until you've solved X.' Every puzzle has a narrative justification and everything you need is right there, if you figure out how to look.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_1_medusa_report.png",
        end_date=date(2023, 11, 3),
        reward_name="THE DOUBLY SPECIAL AGENT",
        reward_amount=100,
        reward_description="One personalized PREMIUM copy of THE MEDUSA REPORT, plus one copy of THE VANDERMIST DOSSIER. Includes Vandermist enamel pin. Kickstarter exclusive."
    )

    game2 = Project(
        project_name="Soulmist : Unspoken Tales",
        description="A book of dark and unforgiving adventures inside the heart of Erebos, for 5e.",
        category_id=6,
        money_goal=15000,
        user_id=9,
        city="Albany",
        state="NY",
        story="Journey inside the Darklands, where the Light never shines, and fight hordes of darkspawns, demons, and unfathomable abominations. This is a set of two adventures, taking place in the world of the Soulmist campaign setting, but that can be played in any regular 5e campaign without any issue. Our biggest priority is to deliver you the best quality products we can achieve. In order to accomplish that we have set up a network of talented individuals and companies to troubleshoot any obstacle in the road to delivering on our project.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_2_soulmist.png",
        end_date=date(2024, 1, 10),
        reward_name="Prince of Dusk",
        reward_amount=80,
        reward_description="Get the full collection of Soulmist titles, in both their Hardcover and Digital versions. Included are both GM's screens featuring artwork from Soulmist and Darklands, the map of Fyera and a set of maps of all its major cities, the collector's slip case, the dice set and the spell cards. *Shipping charged after the campaign"
    )

    game3 = Project(
        project_name="Pathfinder: Abomination Vaults - Hack & Slash ARPG",
        description="The first-ever co-op Hack and Slash ARPG, based on the renowned Pathfinder Roleplaying Game! Set to release on PC (Steam).",
        category_id=6,
        money_goal=410000,
        user_id=8,
        city="Milwaukee",
        state="WI",
        story="The first-ever Co-op Hack and Slash ARPG based on the renowned Pathfinder Roleplaying Game! Pathfinder: Abomination Vaults is a classic Co-op Hack and Slash game, based on the epic Adventure Path of the same name, in which up to four players lead iconic Pathfinder heroes into the farthest depths of Gauntlight Keep, battle deadly monsters and abominations to reach the evil sorceress Belcorra Haruvex and put an end to her vile schemes once and for all. Genre: Online & Local Co-op/Offline Solo Hack and Slash, Action RPG, Dungeon Crawler game Platform: PC (Steam)",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_3_pathfinder_abomination.jpeg",
        end_date=date(2023, 11, 30),
        reward_name="Digital Download",
        reward_amount=40,
        reward_description="Unlocks the Deluxe role in our Discord server, a digital download of our game Pathfinder: Abomination Vaults, and your name in the credits! Includes digital download of Pathfinder: Abomination Vaults game and exclusive wallpaper backgrounds for desktop and mobile."
    )

    game4 = Project(
        project_name="Asteroid Dice: The giant throw & collide squishy dice game!",
        description="Throw, bounce and collide giant foam dice in this chaotic, cosmic game! These squishy dice are also great for RPGs, DnD & Giant Gaming.",
        category_id=6,
        money_goal=7800,
        user_id=9,
        city="Boston",
        state="MA",
        story="The giant roll, throw and collide dice game! Grab your asteroid die from the middle, but be prepared to face-off against your opponent snowball-fight style! Once the moon dust has settled, roll and crash the dice together to get your score up, and hopefully get your opponents score down. With giant squishy foam dice this game is as tactile as it is fun. You will need strategy, speed and skill to come out on top. The Kickstarter Edition, Fireball Expansion Edition and all of the Kickstarter artwork is limited and exclusive to this campaign only. They will not be available outside of Kickstarter. We are also offering an exclusive Shape Invaders Bundle (a sneak preview into our next game) including an Alpha of an App!",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_4_asteroid_dice.png",
        end_date=date(2023, 12, 12),
        reward_name="Astronaut",
        reward_amount=5,
        reward_description="Help support our Kickstarter, get access to the pledge manager, and get 7 awesome pieces of space-art as phone backgrounds from our talented collaborating artist: Khairul Anam!"
    )

    game5 = Project(
        project_name="French Quarter: A let the good times roll and write game!",
        description="Welcome to the heart of New Orleans! Explore the French Quarter in this new loaded roll and write game.",
        category_id=6,
        money_goal=18000,
        user_id=8,
        city="Detroit",
        state="MI",
        story="In French Quarter,  you are in town for a weekend trip with plans to spend your Saturday evening taking in as many of the citys unique sights and sounds as you possibly can in a mere eight hours. Whether it’s the distinct food, local culture, shopping hotspots, mystic customs, or vibrant nightlife, there’s something to experience on practically every corner. There is live jazz everywhere you go, and NOLA is world-famous for its street performers. Make sure you do not miss the spontaneous wedding parades, known locally as second lines, that roll through the streets!",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_5_french_quarter.png",
        end_date=date(2023, 11, 22),
        reward_name="French Quarter - Kickstarter Edition",
        reward_amount=29,
        reward_description="INCLUDES: French Quarter - Kickstarter Edition, All Achieved Stretch Goals, Kickstarter Bonus Content, A hearty thank you!"
    )

    game6 = Project(
        project_name="Penumbra City",
        description="A ttrpg set in the mysterious world of Harrow.",
        category_id=6,
        money_goal=13000,
        user_id=9,
        city="Tucson",
        state="AZ",
        story="Penumbra City is a rules-medium, campaign-world-rich tabletop roleplaying game designed for 3-6 players. It is already 80% written and is playable, we just need your help to finish the last round of playtesting and get it printed and into your hands. Penumbra City is a class-based game with simplified core mechanics but a broad range of character class abilities. Healing is hard to come by, so the decision to fight must never be taken lightly. While one player takes the role of the Game Master, players roll all dice. Most rolls are made with d20s. Penumbra City uses a reputation economy; it is a world where money has lost its luster, and it is a characters reputation with the various gangs, factions, and coalitions that determine their access to resources.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_6_penumbra.png",
        end_date=date(2024, 1, 18),
        reward_name="Digital Edition",
        reward_amount=15,
        reward_description="This tier includes downloadable digital editions (PDF) of Penumbra City, our Zine Bundle, and our Class Character Sheets"
    )

    game7 = Project(
        project_name="The Wagadu Chronicles - Afrofantasy MMO for role-play",
        description="An Afrofantasy world to explore both as an isometric MMO built for in-character roleplay and as a 5E-compatible tabletop setting!",
        category_id=6,
        money_goal=100000,
        user_id=8,
        city="Madison",
        state="WI",
        story="We believe that role-playing isn't always just about about grinding and growing stats. It's the embodying of a role; the presence of a backstory and all of the quirks and details that define your unique character. Many of us have experienced old-school role-play around a table with pencils and a bunch of dice. We know how immersive it is to speak like our characters and to be surrounded by other players who are making decisions based on their characters profiles. Role-play truly submerses you in another world, more powerfully than any NPC  quest could. Imagine a videogame where everyone around you is role-playing. The noble Emere with whom you are travelling does not want to desecrate any tombs and ignores the loot; the Swala hunter you just met chants a ritual prayer before every hunt and the Asiman merchant never attacks or kills anyone because she believes her goddess wants peace to rule in Wagadu.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_7_wagadu.jpg",
        end_date=date(2023, 11, 1),
        reward_name="Afrofantasy Lore Bundle",
        reward_amount=55,
        reward_description="INCLUDES: 🎮 Digital Edition of The Wagadu Chronicles MMO 📂 The 7th Era Setting 5E Rulebook (PDF) 📂 Guide to Afrofantasy Roleplay (PDF) 📂 The Art of Wagadu (PDF) 🗝 Access to MMO closed Beta - Sixth Era 💎 Golden Sun Spear (In-Game Item) 🔶 Name in Credits 🔷 Discord Role"
    )

    game8 = Project(
        project_name="Command of Nature",
        description="An immersive, deck-building tabletop game from the creators of Here to Slay and Casting Shadows",
        category_id=6,
        money_goal=50000,
        user_id=9,
        city="St. Louis",
        state="MO",
        story="Harness the magic of the forest and go head-to-head with your rivals in this strategic deck-building game for 2 or 4 players. You will play as a powerful Sage, summoning warriors from the Twig, Leaf, Droplet, and Pebble factions and fighting to prove your prowess. As the battle continues, you will level up and gain access to extraordinary abilities and fierce new recruits. Protect your Sage at all costs and vanquish your opponents to earn the title of Master of the Elements! As part of this project, we created exclusive and collectible items that you won't get anywhere else as a thank you for supporting us on Kickstarter. These items will not be available online or in retail stores at a later date.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_8_command_of_nature.jpg",
        end_date=date(2023, 12, 24),
        reward_name="Kickstarter Exclusive Edition Game",
        reward_amount=39,
        reward_description="INCLUDES: Command of Nature: Kickstarter Exclusive Edition Game"
    )

    game9 = Project(
        project_name="Flickade",
        description="Experience an exciting and engaging game for those who enjoy flicking objects with precision and strategy.",
        category_id=6,
        money_goal=1200,
        user_id=8,
        city="Kimberly",
        state="ID",
        story="Introducing Flickade, my second-ever game creation and first venture on Kickstarter. This thrilling flicking game challenges your precision and strategic skills. I've meticulously designed every ship piece in Blender and brought them to life with 3D printing. Even the extensively refined case design is 3D printed. It not only screws on perfectly but also boasts an aesthetically pleasing appearance. Each set comes with a sticker on the bottom, featuring a condensed version of the rules, and an additional sticker with answers to common questions that you can place wherever you like. Master the game within just 5 minutes and immerse yourself in hours of fun. Flickade includes 20 ships (10 per player) with 4 small speedboats, 10 medium destroyers, and 6 large aircraft carriers, all 3D printed out of PLA. PLA is a type of plastic that doesn't rely on petroleum and is mainly corn starch or sugar cane. This environmentally conscious choice ensures that our game is both fun and eco-friendly. Each round lasts approximately 15 to 30 minutes, making it perfect for quick matches or extended gaming sessions. The game is designed primarily for two players, but Flickade can be easily adapted for multiple participants with additional sets. Flickade is recommended for ages 4 and up, making it an ideal choice for family game nights. We offer a vibrant selection of eight distinct colors, paired to create four dynamic color combinations for your Flickade sets: Red/Blue, Gray/Orange, White/Magenta, and Brown/Green. Each set's container comes in a sleek black finish by default but can be customized upon request.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_9_flickade.jpg",
        end_date=date(2023, 11, 10),
        reward_name="Flickade: 2-Player Set",
        reward_amount=30,
        reward_description="Flickade full set and a big thank you!"
    )

    game10 = Project(
        project_name="Slothtopia - A reimagined life simulator game for PC/Switch",
        description="A charming life simulator game where you can fish, farm, build relationships, and even catch and train monsters",
        category_id=6,
        money_goal=5000,
        user_id=9,
        city="Huntington Beach",
        state="CA",
        story="Slothtopia: A family-friendly charming life simulator game where you can fish, farm, build relationships, and even catch monsters as an adorable, hard working sloth. Catch fish at sea, come home and pick fresh herbs from the garden, and make a meal for your friends. Build friendships and romance with other villagers. Catch local monsters and train them to help you with tasks around the island. These are just a few of the things to do on the magical island of Slothtopia! Catching island monsters can be difficult. Hone your skills by picking magical fruits and hiding in the tall grass until you spot one. Once caught you will be required to provide for your monster. You can pet, feed, and train your monster to level up your relationship and it's abilities. Unlike some other popular monster catching games, we do not battle our monsters. We use them much more like service animals. They are excellent companions, but also serve a distinct purpose. You must train them to utilize their special skills. Once trained, you can send your monster on tasks like catching fish, farming, and even romancing that special someone.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_10_slothtopia.jpg",
        end_date=date(2023, 12, 1),
        reward_name="Alpha Access Bundle: Slothtopia",
        reward_amount=40,
        reward_description="Get access to Slothtopia in it's earliest stages for testing. In addition get your name in credits and an exclusive hang-glider skin."
    )

    game11 = Project(
        project_name="Pelican Playing Cards",
        description="Elegant playing cards printed by USPCC, tuck box printed by Gambler's Warehouse",
        category_id=6,
        money_goal=10000,
        user_id=8,
        city="Las Vegas",
        state="NV",
        story="Hey, I'm a magician and Guinness World Record card thrower from Lithuania. Over the past decade, I've traveled the world performing magic in theaters, on cruise ships, and at corporate events. I'm extremely excited for this debute in the world of PLAYING CARDS! Ive had a passion for playing cards since I started practicing magic at 12 years old. Everywhere I went I would always look for new or interesting decks. I would even have my friends and family bring them back from their trips. Ever since, the dream of creating MY OWN DECK OF PLAYING CARDS has always been in the back of my mind. I never felt ready or confident enough to create something unique, but eventually I realized that I would never be ready. I needed to trust the process and start. Now, after spending two years on this project, I am thrilled to be one step away from releasing my very first deck, which I have named... drum roll... PELICAN! Now I am excited to invite you to be a part of bringing these cards to life! But why Pelican? First of all, it sounds really cool! Just say it out loud with me: 'Pelican Playing Cards'! I bet you want to say it again, don't you? BUT there's also a deeper meaning behind the name! Pelicans can hunt in groups, yet they also spend time alone. I believe that life is all about balance - being alone, being in a group - and you can help others when youre at peace with yourself.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_11_pelican_cards.jpg",
        end_date=date(2023, 11, 20),
        reward_name="1 Pelican Deck",
        reward_amount=19,
        reward_description="100 percent custom playing cards."
    )

    game12 = Project(
        project_name="SLAV BORG - A Post-Soviet Semi-Fantasy RPG",
        description="Rev the engines with your goblin crew, steal some sweet new orc wheels and put the brakes on the Eastern Bloc’s slimiest necromancer.",
        category_id=6,
        money_goal=8035,
        user_id=8,
        city="Philadelphia",
        state="PA",
        story="In SLAV BORG, cunning, speed, and covertness reign supreme. You will traverse the borderland with your goblin crew, outmaneuver orcs in illegal (and fixed) street races, and try to put the brakes on the sleaziest necromancer this side of the Eastern Bloc. SLAV BORG is a stand-alone game that’s also compatible with MORK BORK and other OSRs. And you know what this means: tons of new tables, monsters, NPCs, and various additional components you can use to craft a playstyle and narrative that best suit your greedy spirit. The game can be played in three different modes. SLAV BORG’s main RPG campaign will throw you right in the middle of the Realm of Zgol, where you will try to carve out your own skid by leveling your crew, upgrading your vehicles, and burning rubber across multiple story chapters. The stakes, along with the players' death count, escalate even further in SLAV BORG's second play mode: one-shot adventures. Finally, theres the roguelike mode, where each run is randomized with new locations, events, and scenarios. Using the classic framework of sword and sorcery, we are telling our SLAV BORG tales against the real-world backdrop of the social and economic struggles of the Polish-German-Czech borderland. This way, we want to craft a fantasy world that mirrors the reality that shaped us, with one of Europes biggest coal mines on one side, and rampant crime and lawlessness on the other. Welcome to the Realm of Zgol.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_12_slav_borg.jpg",
        end_date=date(2023, 9, 25),
        reward_name="NECROMANCER [PRINTED DELUXE + DIGITAL]",
        reward_amount=70,
        reward_description="INCLUDES: Hardcover book. Character sheet notebook. Paper miniatures (if unlocked). Modular cardboard Gurlitz racetrack/dungeon (if unlocked). Printed poster with map and dungeon. Digital book [PDF]. Digital poster with a dungeon. Digital character sheet. Digital map. Digital coloring book"
    )

    design1 = Project(
        project_name="Keychron Q5 Pro - QMK Custom Wireless Mechanical Keyboard",
        description="Wireless | Full Aluminum | Hot-Swappable | Connects Up to 3 Devices | For Mac, Windows, Linux | Remap with QMK/VIA ",
        category_id=3,
        money_goal=50000,
        user_id=6,
        city="Beverly Hills",
        state="CA",
        story="Introducing Keychron Q5 Pro, a unique QMK/VIA wireless mechanical keyboard with a full aluminum body. The Q5 Pro is designed to deliver a premium typing experience for users who need a compact board with a number pad and home cluster. We designed the Q5 Pro to allow people to intuitively reassemble the keyboard from the inside out, so they can customize any key or create macro commands through the VIA software, and easily assemble each component. Together with our signature Bluetooth wireless connection, in-house KSA PBT keycaps, double-gasket design, and hot-swappable features, the Q5 Pro is quite a versatile premium custom mechanical keyboard. Designed to enhance your creative workflow, the aluminum rotary encoder allows you easily customize the knob to your desired key or macro commands, such as zooming in/out, selecting video clips, photos, or backlight hue, and adjusting screen brightness, brush size, and volume.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/keychron.jpeg",
        end_date=date(2024, 5, 4),
        reward_name="Fully Assembled - Q5 Pro",
        reward_amount=205,
        reward_description="1 x Q5 Pro Fully Assembled US Layout Keyboard, included Mac and Windows keycaps and stretch goal gift/s once unlocked. Available in Carbon Black, Silver Gray, Shell White frame options with corresponding PBT keycap colorways (We'll ask about your preferences and address after the Kickstarter ends). Available in Keychron K Pro Mechanical Red, Brown, Banana switch options (We'll ask about your preferences and address after the Kickstarter ends)."
    )

    design2 = Project(
        project_name="Jollylook Pinhole SQUARE - The Instant Film Camera DIY Kit!",
        description="It’s a functional camera. It’s a project. It’s a puzzle. It’s a model. All in one.",
        category_id=3,
        money_goal=15000,
        user_id=7,
        city="New York City",
        state="NY",
        story="The Jollylook Pinhole SQUARE is an innovative, eco-friendly DIY kit that lets photography enthusiasts create their own instant film camera from scratch. Designed with the vintage aesthetics and the charm of classic photography, this kit aims to make the process of camera-building and picture-taking a hands-on, educational, and enriching experience. This project is not just a DIY kit but an educational journey, a nod to the rich history of photography, and an exploration of the joy of creating something with your own hands. It's a perfect gift for photographers, hobbyists, students, educators, and anyone who appreciates the intersection of art and science. Building on the success of our previous Kickstarter campaign for the Jollylook Pinhole Mini DIY kit, we've designed an even more exciting SQUARE format camera for instant film enthusiasts and DIY lovers.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/JollyLook.jpeg",
        end_date=date(2023, 10, 14),
        reward_name="1 x Jollylook Pinhole SQUARE KS special",
        reward_amount=89,
        reward_description="1 x Jollylook Pinhole SQUARE DIY - Kickstarter special Get creative and own this unique Vintage Style Instant Film Camera Kit. Craft a camera that captures nostalgic memories, SQUARE format, pinhole-style! Get now with an Early Bird Price of $89 (MSRP $119) only on Kickstarter. Don't miss out on your special discount!Choose from our eco-friendly materials and colors in the post-campaign survey.The shipping fee will be charged in the post-campaign survey."
    )

    design3 = Project(
        project_name="The Popsmith Popper: Reimagining Popcorn",
        description="A modern stovetop popcorn popper that elevates snacking at home to a fun and memorable experience.",
        category_id=3,
        money_goal=30000,
        user_id=6,
        city="Seattle",
        state="WA",
        story="At Popsmith, we think that popcorn is more than just a snack—it’s a way to celebrate and connect. The best way to enjoy this classic snack has always been popping up a batch fresh on the stove. But the current stovetop popping experience leaves a lot to be desired. It can be intimidating– even professional chefs worry about burning their popcorn or getting the ratio of butter to oil just right. We wanted to design a popper that made the perfect bowl of popcorn every time, no matter your level of experience. The Popsmith Popper uses an old-fashioned popping technique (just like movie-theater machines use) to achieve the perfect pop. It begins with our patented spinner that tumbles the kernels in oil for consistent results.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/popsmith.jpeg",
        end_date=date(2023, 11, 9),
        reward_name="1x Popsmith Popper",
        reward_amount=149,
        reward_description="Get our BEST price and the earliest shipping with our Kickstarter Early Bird exclusive offer; limited quantities, first-come, first served. Be the first to buy! KICKSTARTER SPECIAL | 1x Popsmith Popper 25% OFF (Save $50, $199 MSRP) 1x Popsmith Popper: Constructed of sturdy stainless steel and works on all stove types."
    )

    design4 = Project(
        project_name="Time Machine a Multi-tap Delay for Eurorack Modular",
        description="A tactile, intuitive interface for the exploration of the recent past.",
        category_id=3,
        money_goal=6500,
        user_id=7,
        city="Northhampton",
        state="MA",
        story="Time Machine is a tactile interface for mixing together 8 delay lines with the original input signal. It has its own character and color. It has an expansive range that makes it possible to space the taps several seconds from each other while also letting you make the delays short enough to enable flange, comb filters, and Karplus–Strong. Our little company, Olivia Artz Modular, is a collective of trans and gender non-conformant artists and builders who are working together to bring our dreams into the world. We’re neurodivergent people who lean on each other. We’re queer people going full voltron/megazord. When you support this woman-owned, queer-owned business you are supporting a network of queer people around the world. To say hi, get involved, or get updates you can join our public Discord server. Last year we released Teletouch, an expressive touch instrument invented by Non-Verbal Poetry, a witch living on a boat in Scotland. Earlier this year we released Uncertainty, a tiny platform for working with gates. It features artwork on the PCB by my daughter, Marcy Artz-Skylark, who designed a fuzz pedal we’re working on. We build and we keep building, but we need a boost. Time Machine only uses high quality components (Bourns faders, Alpha pots, Qingpu sockets) and we want it to cost around half as much as anything comparable. At the same time, all markings on the faceplate will be actual silver. We can do all these things if we’re making 20+ and we have the funding up front. Funds from Kickstarter will also go into transitioning from our functional prototype to our final design. ",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/TimeMachine.jpeg",
        end_date=date(2024, 2, 5),
        reward_name="1x Time Machine",
        reward_amount=335,
        reward_description="You get a Time Machine. I mean, what else? That’s what this Kickstarter is all about!"
    )

    design5 = Project(
        project_name="UNIT 1 AURA: next-gen smart helmet for urban & road riding",
        description="Elevate your safety with integrated lights, turn signals, brake lights, Mips & Crash detection. E-bike certified. Iconic design.",
        category_id=3,
        money_goal=20000,
        user_id=6,
        city="New York City",
        state="NY",
        story="Helmets can do so much more than just protecting your head. Heres proof. AURA fives you lights on your highest point, offers E-bike certified protection and will even call for help if you crash. It does all that in a super lightweight package with extensive ventilation and undeniable style.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/helmet.jpeg",
        end_date=date(2024, 4, 5),
        reward_name="Early Bird | Helmet Kit",
        reward_amount=169,
        reward_description="Serious protection. Will retail for $250 | 32% off retail. Helmet color and size are selected through a survey via email at the end of the campaign. Shipping, duty, and VAT are calculated and charged separately prior to shipping. Scroll down to see estimated shipping costs."
    )

    design6 = Project(
        project_name="FINEDAY 3.0 Aluminum Edition: Bluetooth Mechanical Keyboard",
        description="Classic typewriter with a modern twist! Enjoy the sophisticated design with increased productivity via 4-device multi-pairing function",
        category_id=3,
        money_goal=3000,
        user_id=7,
        city="Philadelphia",
        state="PA",
        story="A classic mechanical typewriter is a beautiful historical creation. Known for the unique clicky switches, the 'feel' of the mechanical typewriter is very popular and adored by many users to this day. Switches are what determine the sensation of typing via key registers, and they last ten times longer than membrane or laptop keyboards. The mechanical keyboard is also equipped with key caps with a long lifespan that can withstand up to 500,000 presses. However, general keycaps are expendable, made of plastic or alloy materials, and require to be replaced periodically. Introducing FINEDAY 3.0, a new high-end mechanical keyboard inspired by the classic typewriter design! From its body, keycap, knob, and lever, FINEDAY 3.0 has used full aluminum for durability as well as easy maintenance. Experience the best of both worlds—enjoy the timeless charm and make a worthwhile investment that will make your desk setup extra special.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/fineday.jpeg",
        end_date=date(2024, 6, 15),
        reward_name="Kickstarter Special",
        reward_amount=770,
        reward_description="Includes keyboard body, keyboard cover, USB-C cable, customized keycaps, user manual. When the Kickstarter campaign ends, we will send you  a survey where you can select your color"
    )

    design7 = Project(
        project_name="GoChess: The Most Powerful Chess Board Ever Invented",
        description="Experience the Magic with Self-moving pieces | Real-time coaching | Online play | AI-powered | Premium Design.",
        category_id=3,
        money_goal=20000,
        user_id=6,
        city="Bend",
        state="OR",
        story="The ultimate strategy game played for centuries. From kings and queens to grandmasters, it has captivated players of all skill levels with its timeless beauty. With its simple rules and rich complexity, chess has the power to challenge the mind like no other, while simultaneously providing hours of entertainment. With two products successfully delivered (GoCube and GoDice) already under our belt, and over 300k happy customers, and multiple global awards for our products,  our team is excited to introduce GoChess — the world’s first truly robotic chess board with AI technology that provides an unprecedented level of realistic gameplay. With GoChess, distance is no longer a barrier to playing your favorite game of chess, against your opponent of choice! Play with Anyone. Anywhere. Anytime. Whether it’s face-to-face, online, or with AI.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/chess.jpeg",
        end_date=date(2024, 1, 4),
        reward_name="Early Bird 1x GoChess Modern 1XR",
        reward_amount=269,
        reward_description="Get your GoChess Modern 1XR smart chess set, where only one piece moves at a time. Secure your reward for $269, enjoying an incredible 29% discount off the future retail price of $379! NOTE: Shipping is charged in the post campaign survey."
    )

    design8 = Project(
        project_name="55 66 88 by CW&T",
        description="A phone stand set at 3 useful angles for positioning your camera.",
        category_id=3,
        money_goal=8000,
        user_id=7,
        city="Miami",
        state="FL",
        story="A phone stand set at 3 useful angles for positioning your camera. Great for everyday chats or documenting your latest creation. Made in the USA from extruded aluminum with a black anodized finish. 55 66 88 is simple, durable and convenient to keep handy. No moving parts to fuss or fiddle with.  55 66 88 is about quickness and convenience. All 3 angles are useful for a variety of everyday uses for your phone’s camera : 55° : aim down to photograph or record video of stuff on a surface. 66° : 1-on-1 chats or to take photos of taller things on a surface. 88° : group video chats or POV documentation. We use this one a lot at the dinner table. (This one's surprisingly useful!)",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/phoneHolder.jpeg",
        end_date=date(2024, 3, 4),
        reward_name="1x 55 66 88",
        reward_amount=33,
        reward_description="Anodized black aluminum phone stand set at 3 useful angles for chatting or documenting."
    )

    design9 = Project(
        project_name="Micro Clutch: Never drop your mirrorless camera again.",
        description="A beautiful, functional hand strap specially designed for mirrorless cameras. Better grip, more comfort, total access to controls.",
        category_id=3,
        money_goal=50000,
        user_id=6,
        city="San Francisco",
        state="CA",
        story="Whoa! Peak Design is launching a new product on Kickstarter. A few things to know: Micro Clutch will ship in summer of 2023. Lock in this sweet deal by backing now! You can add other PD products onto you reward for up to 50% off MSRP! This is a shorter campaign than most of our others. We've got big things coming soon. We launch products on Kickstarter because it keeps us free of outside investment and you closer to great design. Now, meet Micro Clutch.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/clutch.jpeg",
        end_date=date(2024, 8, 23),
        reward_name="1x Micro Clutch",
        reward_amount=50,
        reward_description="Get the Micro Clutch hand strap and never drop your mirrorless camera again. Choose the L-Plate or I-Plate version when we send out fulfillment surveys in July. Local sales tax/VAT will also be calculated and collected at that time."
    )

    design10 = Project(
        project_name="Lucid ONE, Out of box & AI Planning 7DOF robotic arm",
        description="Industrial grade ultralight robot arm with open source magnetic tooling for AI control, Vlog, 3D printing, Engraving & Education labs.",
        category_id=3,
        money_goal=10000,
        user_id=7,
        city="Irvine",
        state="CA",
        story="AMBER is unlocking a new era for intuitive control, robotic technology with affordable, lightweight and Zero-Code robotic arm. By drastically reducing the costs and technical barriers to entry, AMBER L1 is the best choice to enable beginners, experienced developers or companies to embrace robot intelligence for the future. We have taken simple operation and easy-to-use as our goal, and we hope to lower the threshold for using the robotic arm, that's why we called Zero-Code. With AMBER AI intuitive control, you don't even have to think about the robot. Just squeeze the controller and place it exactly where you want.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/robotArm.jpeg",
        end_date=date(2024, 6, 2),
        reward_name="Amber Lucid-1 KS Exclusive",
        reward_amount=1399,
        reward_description="Incredible 55% off the MSRP ($3,079) Gear up with the advanced robotic tech at the BEST & ONLY price!"
    )

    design11 = Project(
        project_name="Vernte: Noise Canceling Smart Headphones.",
        description="Industrial grade ultralight robot arm with open source magnetic tooling for AI control, Vlog, 3D printing, Engraving & Education labs.",
        category_id=3,
        money_goal=10000,
        user_id=6,
        city="San Francisco",
        state="CA",
        story="We are pleased to introduce our closed-back, noise canceling headphones with sonic clarity and smart features.  We began developing the headphones in 2020 as the World shifted towards more virtual and contactless communication.  This innovative headphone combines the functionality of a smartphone with the convenience of a wireless headset, providing a truly immersive and connected audio experience.  You can also connect them to your mobile phone and use them like regular headphones. The Vernte smart headphones come equipped with 4G LTE SIM capability, 128GB or 256GB storage, and 4GB or 6GB RAM options. The 2' OLED screen allows you to configure, set up, and manage your headphones, browse the internet,  and access your favorite social media platforms providing crisp visuals and intuitive touch controls. Besides powerful functionality, the device comes in a sleek and textured design that offers three high-quality leather options with an aluminum finish on the braces and earcups. The Exquisite-Plus model stands out with an aesthetically pleasing monogram on the headband.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/headphone.jpeg",
        end_date=date(2024, 1, 2),
        reward_name="Early Bird: Exquisite",
        reward_amount=330,
        reward_description="Semi-aniline leather headband, Aluminum body, Engraved design, 4G LTE network, 4GB RAM, 128GB storage. Color options: White, Black, Red & Brown. A set of Custos headphones with free shipping within the United States for our VIP subscribers. This is an amazing offer and $270 lower than the suggested retail price of $599. INCLUDES: Custos Exquisite Headphones, Charger and USB-C Cable, Product Documentation"
    )

    design12 = Project(
        project_name="KOKONI SOTA 3D Printer : 10X Faster 3D Printing with 7-Color",
        description="600mm/s Fast Speed｜7-Color Printing｜Inverted Design ｜21m/s² Acceleration｜AI modeling ｜Accurate 0.1mm Detail ｜30dB Silent Printing",
        category_id=3,
        money_goal=50000,
        user_id=7,
        city="Boise",
        state="ID",
        story="Discover the innovative KOKONI SOTA 3D printer, featuring a unique upside-down design for rapid, stable printing.* Enjoy 10 × faster 3D printing with up to 7 colors, and effortlessly create intricate models using the AI-powered KOKONI APP. With advanced AI Radar Detection and error compensation, the KOKONI SOTA delivers flawless prints every time and exceeds expectations with its unparalleled precision, error less than 0.1mm. Immerse yourself into a universe of infinite imagination, where KOKONI SOTA effortlessly translates your creative visions into stunning works of art.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/3dPrinter.jpeg",
        end_date=date(2023, 11, 2),
        reward_name="KOKONI SOTA Lite",
        reward_amount=550,
        reward_description="By claiming this reward, you will get the SOTA Lite 3D Printer with guaranteed delivery by the KOKONI team at $200 OFF from the $749 MSRP."
    )

    film1 = Project(
        project_name="FEDORA",
        description="The marriage between Betty and José has challenged social norms regarding age and gender. But 25 years later, what keeps them together?",
        category_id=4,
        money_goal=25000,
        user_id=6,
        city="New York City",
        state="NY",
        story="After almost four years of working with Betty Grafstein and José Castelo Branco in registering their life in NYC and their testimonies as they struggle through major changes and challenges, we are ready to enter the editing room in order to put together a first cut of this stunning documentary film about this endearing couple that over 25 years has been challenging social norms regarding age and gender, and facing several controversies in Portugal and abroad. The collected sum will serve to enter the first stage of the post-production and present a first glance of the potential of the film to distributors and other financing entities in order to complete financing. Project supported by the ICA Portugal. Selected at DOC NYC, DOK Leipzig Industry, Sheffield Doc/Fest UK and Film London PFM co-production markets.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/fedora.jpeg",
        end_date=date(2024, 5, 2),
        reward_name="Your Name on the Big Screen!",
        reward_amount=10,
        reward_description="For the price of a (fancy) coffee, your personal or your company name will be in the final credits of the film as a contributor of the Kickstarter funding campaign."
    )

    film2 = Project(
        project_name="THIRSTY",
        description="A new narrative feature film about a gutsy woman who strives to become the mayor of Oakland",
        category_id=4,
        money_goal=40000,
        user_id=7,
        city="Berkeley",
        state="CA",
        story="THIRSTY follows the journey of Audrey Allen, a woman torn between her career and family as she strives to become the mayor of Oakland. Her story is acutely relevant today because 3.5 million American mothers left the workforce during the pandemic and many have not returned. So I hope THIRSTY emboldens women to strive for their professional actualization against the odds and also expands our collective notion of what a leader looks like. Despite our advances, we've never had a woman president, women still hold less than 20% of elected positions nationwide and make up only one-quarter of congress. The more we see women, mothers and people of color striving for positions of political leadership, the more we normalize it. During the development of THIRSTY, I had the honor of interviewing many women politicians who entrusted me with their personal experiences on and off the campaign trail. Among these women was my own mother who ran for office twice during my childhood. What I often found most compelling about their stories were the fumbles. I began thinking about how powerful it would be to see an imperfect, middle class mother like Audrey in campaign mode. THIRSTY is an undeniably feminist film that aims to inspire more women to run for office, against the odds and with their families in tow. I believe that getting more women into government is the single most efficient way to transform society and it is also THIRSTY's raison d'être. But THIRSTY is not just a campaign film. It is also a deeply honest portrayal of a woman who is unapologetically ambitious, maternal and sexual. Because our characters reflect the diversity of Oakland, the complexity of modern day race relations is also an important theme. And at the heart of our story is an interracial marriage under great pressure. As a female filmmaker, I share many experiences with women in politics. We are both engaged in a daily struggle for leadership positions – one in the artistic arena, one in the political. As a working mother that is striving for success in a highly competitive and male-dominated field, Audrey’s journey is very much my own.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/thirsty.jpeg",
        end_date=date(2024, 2, 2),
        reward_name="Ramses Party Package",
        reward_amount=150,
        reward_description="Join Team Thirsty on Friday, July 7th from 6-9PM for an exclusive cocktail party at Oakland's sublime store/event space Ramses Art Garden (owned by friends of the production Malik & Carson). Address: 2511 Broadway, Downtown Oakland, www.ramsesartgarden.com"
    )

    film3 = Project(
        project_name="Brigidy Bram: A Feature Documentary Film",
        description="Meet the greatest artist you've never heard of.",
        category_id=4,
        money_goal=25000,
        user_id=6,
        city="Miami",
        state="FL",
        story="In this intimate portrait circling fact and fiction, the true story of prolific painter Kendal Hanna reveals a case study of how society codifies genius—and institutionalizes difference. Artists and scientists collaborate to uncover the forces threatening to erase Hanna's memory, his work, and his name from history. Drawing from the strong literary and cinematic tradition of anachronistic narratives, we explore the mysteries of Hanna’s life as one might put together a jigsaw puzzle.  The fabric of the documentary is made up of scenes crafted by artists of various disciplines, carefully reconnecting the fragmented narrative. After experimenting with psychedelics in the Chelsea beatnik scene of the 1950s, Hanna is committed to a psychiatric institution which diagnoses him with schizophrenia.  He's prescribed two electroshock treatments per week.  When he asks for his freedom, he's told he has one chance: double his course to four treatments per week, or commit to institutionalization for life.  ",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/brigidy.jpeg",
        end_date=date(2024, 6, 6),
        reward_name="Your Name in the Credits",
        reward_amount=50,
        reward_description="Be immortialized in the credits of the film"
    )

    film4 = Project(
        project_name="Outwith",
        description="A lone assassin navigates a dangerous exclusion zone, encountering those who have lost everything in the search of hope",
        category_id=4,
        money_goal=3000,
        user_id=7,
        city="Chicago",
        state="IL",
        story="Outwith is a genre-bending Sci-Fi/Drama/Neo-Western which takes place in a wild and dangerous exclusion Zone. We follow a Liquidator, a Party-appointed assassin, on a mission to clear the province of terrorists and subversives. Along his journey he encounters several characters, including an old man living in the ruins of his old life, a teenager with a stillborn child heading to 'The Core' where she believes her child can be healed, and a former Liquidator who has rejected her training and dogma to live a quiet life deep within the exclusion zone. As the Liquidator continues his mission, he begins to question his role and the strict dogma he has been indoctrinated with. The film explores themes of grief, memory and regret, contrasting emotion and hope against the harsh reality of a broken world. The overall tone is bleak, but there are hints of hope as the characters navigate the ruins of their past lives and search for purpose in a world that has been destroyed. Outwith is a thought-provoking film that considers what it means to be human in a world that has been stripped of its humanity.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/outwith.jpeg",
        end_date=date(2023, 11, 2),
        reward_name="A Copy of the Film",
        reward_amount=25,
        reward_description="You will receive a digital copy of the finished film!"
    )

    film5 = Project(
        project_name="Music for the Requiem Mass",
        description="A fresh take on the horror-romance genre; Music for the Requiem Mass is a woman-led, queer vampire feature film shooting this June.",
        category_id=4,
        money_goal=30000,
        user_id=6,
        city="New York City",
        state="NY",
        story="First developed as a play, writer/director Maia Golden has been passionate about Requiem  for a long time.  Through theatrical iterations, short film drafts, and eventually a feature-length screenplay, Maia has lived with this story and these characters for four years.  Over the course of development, Maia brought it to her friend and creative partner Laura Lee. The two of them began to cultivate a plan to shoot in the early winter of 2022.  But as the scope of the project grew, so did the creative community around the film.  Years into development, we are excited to bring Music for the Requiem Mass to life! Music for the Requiem Mass is written and directed by Maia Golden.  Maia is also serving as an executive producer.  The film is produced by Laura Lee, Jacob Daniel Brodsky, and Portia Lundie.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/requiem.jpeg",
        end_date=date(2024, 9, 2),
        reward_name="Invite to Digital Screening",
        reward_amount=25,
        reward_description="Thank you for helping our movie come to life! You'll be one of the first people in the entire world to see this movie. When it's complete, we'll send you an exclusive invitation to an early screening, accessible from anywhere in the world (with internet access)."
    )

    film6 = Project(
        project_name="The Suit - An LGBTQ+ Short Film",
        description="A short LGBTQ+ film surrounding ex-lovers, a tailor and a dancer, learning to say goodbye. How will their crafts honour each other?",
        category_id=4,
        money_goal=10000,
        user_id=7,
        city="Los Angeles",
        state="CA",
        story="Charles, an introverted tailor in his 50s, is creating a suit for his former lover Lawrence, a eccentric performer. As they reminisce over their shared past, Charles grapples with anticipated grief, struggling to hold on to fading memories, whilst Lawrence's love for dance clashes with his illness which is quickly rendering him incapable of pursuing his passion. As they say final goodbye's how will they use each of their talents to remember and honour each other?",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/suit.jpeg",
        end_date=date(2024, 1, 2),
        reward_name="Thank You Credit and Digital Copy of the Film!",
        reward_amount=20,
        reward_description="So not only do you have the wonderfulness of being credited, but you also get the final cut of the short film that we have been putting our blood sweat and tears into! It's the perfect duo!"
    )

    film7 = Project(
        project_name="BY FIRE | A psychological drama short",
        description="A Graduation Short Film about the dark side of getting into character",
        category_id=4,
        money_goal=5000,
        user_id=6,
        city="Detroit",
        state="MI",
        story="By Fire is a psychological short drama following Anya, a wide-eyed understudy who has to replace the actress she idealises, Maria, in the role of Medea, as she navigates within a morally distorted theatre company. Thirty minutes before the play starts, Anya experiences mysterious visions of Maria, while she also has to battle against a director who doubts her competence, a tense stage manager, and the pressures of being in the spotlight for the first time. All these elements of this behind-the-scenes odyssey lead her to confront Maria, let go of her fears, and ultimately become the true version of Medea.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/byFire.jpeg",
        end_date=date(2024, 7, 2),
        reward_name="Associate Producer Credit",
        reward_amount=500,
        reward_description="By pledging $500, you become an integral part of this project. To prove it to you, we’ll credit you as an Associate Producer on By Fire, send you a late draft of the film and music to hear your thoughts and give you an official IMDB credit as well !"
    )

    film8 = Project(
        project_name="Is That All There Is?",
        description="A film about failuer.",
        category_id=4,
        money_goal=15000,
        user_id=7,
        city="New York City",
        state="NY",
        story="Is That All There Is is a film about creative failure. It examines what success means through the story of my experience as a struggling indie musician in a failing city at the turn of the 21st century. Detroit in the early aughts was a strange place. Mostly abandoned and ignored, it was a sort of industrial wasteland turned blank slate. This nothingness sparked a fire of musical output that launched some of the most promising bands in the country at the time. Seemingly overnight, the national media had gotten a whiff of what was bubbling in Detroit, and they descended, laser-focused on the emerging underground rock scene. Bands like The White Stripes, The Dirtbombs, The Von Bondies and The Go were getting international media coverage and record deals. My band, The Trembling, was not. And it wasn’t just us; there was an entire underground of the underground in Detroit that never quite made the leap to a good old-fashioned American success story.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/allThereIs.jpeg",
        end_date=date(2024, 3, 3),
        reward_name="Basement Show Level",
        reward_amount=10,
        reward_description="Wow, thank you! You get a thank you email from the esteemed director!"
    )

    film9 = Project(
        project_name="Yard Bird",
        description="Yard Bird is a short comedy about a man who attempts to break into a retirement community to get face to face with his estranged father",
        category_id=4,
        money_goal=20000,
        user_id=6,
        city="Los Angeles",
        state="CA",
        story="Yard Bird is a short comedy about a charming and desperate man who attempts to break into a retirement community to get face to face with his estranged father. Owen Murray needs his father’s help, but his dad doesn’t want to see him, and the employees don't want to help. This leads Owen to take extreme measures at the strict retirement home where his dad is cooped up.The film deals with themes of forgiveness, family and generational growth.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/yardBird.jpeg",
        end_date=date(2023, 11, 5),
        reward_name="PDF of Yard Bird Script",
        reward_amount=200,
        reward_description="Thank you! This tier gets you everything so far plus the yard Bird Script in PDF format"
    )

    film10 = Project(
        project_name="MONSTER GIRLS",
        description="The secret history and current work of Women in SFX.",
        category_id=4,
        money_goal=5000,
        user_id=7,
        city="Los Angeles",
        state="CA",
        story="Women have been contributing the world of special effects since the days of Universal Monsters but their story has largely gone undocumented … until now. MONSTER GIRLS covers the history and the current work of Women working in SFX. From Creature from the Black Lagoon, to Beetlejuice and beyond! We have officially wrapped the initial interview process of MONSTER GIRLS and now we need your help getting it to the finish line. By partnering with us you’ll be contributing directly to the post production of the film to ensure we finish with the highest quality and are able to present this to festivals and streaming platforms world wide! We have chosen to offer most of our perks digitally to ensure that we can deliver AMAZING bonus content to everyone, no matter where they live in the world! THANK YOU for checking out our project and your consideration in supporting, we're so excited to bring this story to life! ",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/monsterGirls.jpeg",
        end_date=date(2024, 8, 8),
        reward_name="Exclusive Footage Download",
        reward_amount=25,
        reward_description="The story of MONSTER GIRLS is huge and there's no way we could fit it all into a 70 minute time slot. With this tier you'll be getting a digital download of exclusive footage that won't be seen in the documentary release!"
    )

    film11 = Project(
        project_name="The discarded ones",
        description="This is a story about how wars have no winners but only losers. A man finds himself being held captive as he is fighting his own battle",
        category_id=4,
        money_goal=2000,
        user_id=6,
        city="Boston",
        state="MA",
        story="The story begins with Benjamin Mason, a Union sergeant major running through a forest with a gun and a sword. He discovers his fellow soldiers have been killed in action and orders the lone survivor, Private Dwight McCree, that the two of them must regroup with the rest of the company. However, Dwight is more or less unresponsive. As Benjamin tries to talk to him,  they are both shot by an attacker. Benjamin dies instantly, leaving Dwight at the mercy of his enemies. Dwight wakes up much later in a cell and meets Juliette Knox. A confederate scout who is fed up with this war and wants to leave these soldiers. Dwight reveals to Juliette the traumatic events that led him to the war and his motivations for fighting and Juliette shares why she is in this war. In a strange twist of fate, the two realize how alike they are. They form a strong bond with each other and together they form a plan to escape. However as they do, They find themselves being pursued by Confederate soldiers which lead to a tense and daring gunfight where the duo find themselves being very outnumbered and outgunned. And that's where Dwight comes face to face with a vengeful Confederate Liutenant who has a personal vendetta against him because much like Dwight, he has a traumatic event to led to his dark path. It's only a question of weather or not these three individuals can settle their scores in peace or if this neverending circle of hate will be the death of all of them..",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/discardedOnes.jpeg",
        end_date=date(2024, 5, 2),
        reward_name="Your name in the Credits",
        reward_amount=50,
        reward_description="Your name will appear in the credits for the film! Thank you!"
    )

    film12 = Project(
        project_name="Whole World Blind",
        description="Whole World Blind is a Coming of Age / Crime Thriller written and directed by Guatemalan film maker Pablo Gordillo. Shot in Prague.",
        category_id=4,
        money_goal=40000,
        user_id=7,
        city="New York City",
        state="NY",
        story="WHOLE WORLD BLIND is a journey of self discovery that touches on  themes such as: Toxic masculinity and family expectations. The film seeks to expose the effect that this toxicity can have on developing teenagers, especially growing up in an unsupervised household with a violent brother. It shows us the importance of how our closest role models can make or break us in our quest to understand ourselves. Throughout the film, the audience will follow a collective narrative that focuses on three characters - Lukas, Foster, and Bruce. Lukas is a 16-year-old boy who idolizes his older brother Foster, a tough and rebellious figure. Foster takes Lukas on a night out, but before they can begin, Foster needs to stop by his weed dealer, Bruce. Bruce is a timid and nervous person who is always looking over his shoulder, so Foster advises him to get a weapon to protect himself. The stories start to diverge and merge back again when Bruce sets out to buy a pair of brass knuckles for his protection. Upon return to the grocery store where his father works, Bruce gets his new found weapon confiscated by the patriarchal intrusiveness of his father. By fate, the two brothers end up at the same grocery store, where Foster catches a glimpse of the brass knuckles, but is denied his offer to buy them out. Driven by his desire to please his brother, Lukas decides to take the brass knuckles by force, sprouting a new cycle of violence that will result in the moral corruption of Lukas and a thirst for revenge within Bruce.",
        project_image="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/wholeWorldBlind.jpeg",
        end_date=date(2023, 10, 12),
        reward_name="The Goldfish Award",
        reward_amount=50,
        reward_description="Get a digital copy of our script, our script breakdown and a digitalized story board for the film along with a signed poster by the cast and director!"
    )

    art1 = Project(
                project_name = "Oceano (for seven generations)",
                description = "A photographic monograph by Lana Z Caplan based in the Oceano Dunes",
                category_id = 1,
                money_goal = 10000,
                user_id = 4,
                city = "Oceano",
                state = "CA",
                story = "The yak titʸu titʸu yak tiłhini (ytt) Northern Chumash have a phrase 'For seven generations',meaning 'Our decisions are made while thinking seven generations into the future'.Oceano (for seven generations), looks both back and to the future, in images and text, to describe histories and conflicts that question legacies of colonization, photographic history, utopian ideology, and the future for the politically charged and environmentally threatened Oceano Dunes. This is a dramatic local story - but also a story of larger issues that can be seen happening all over the world.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art1.jpeg",
                end_date = date(2024, 6, 3),
                reward_name = "Pack of 3 postcards",
                reward_amount = 10,
                reward_description = "Special Edition of a selection of 3 4x6 postcards with images from the book (images vary)")
    art2 = Project(
                project_name = "Metanoia Marseille Tarot",
                description = "A whimsical and enchanting illustrated tarot deck that follows the traditional Marseille, weaving together a magical journey.",
                category_id = 1,
                money_goal = 18000,
                user_id = 5,
                city = "Seattle",
                state = "WA",
                story = "Metanoia Marseille has been over a yearlong passion that is inspired by the beauty of a traditional Marseille deck and the enchanting magic of florals, nature, whimsical characters, and vibrancy of color. The Metanoia Marseille deck's energy is playful and inspiring, reflecting a lighthearted yet honest depiction of the century's old tradition of the Tarot de Marseille. In working with such a beautiful expression of tarot, it was important for me to capture the original essence of each card, staying true to the depictions and intrinsic meanings, while adding my personal expression of illustration to the deck. This is a deck that can be used by everyone of all ages. Each card laid out next to one another in any standard or personal configuration offers a beautiful and vibrant story that expands imagination and extracts new meanings and ways of approaching all life situations. With every detail thoughtfully and intuitively designed for you, I hope you find a bit of magic in this deck as you work with it in your practices. XOXOXO",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art2.jpeg",
                end_date = date(2024, 1, 15),
                reward_name = "Metanoia Marseille Mini Package",
                reward_amount = 45,
                reward_description = "This reward is the mini size deck package full of fabulous goodies!")
    art3 = Project(
                project_name = "Paintings of Japan",
                description = "Travel to Japan in Spring and Autumn through colourful illustrations in this set of two art books.",
                category_id = 1,
                money_goal = 4468,
                user_id = 4,
                city = "San Diego",
                state = "CA",
                story = "In Spring 2023, I embarked on an intense trip to Japan. Although this was my 5th time in Japan, it's the first time that I got to fully experience the magical cherry blossom season during peak bloom. I traveled to many places and discovered beautiful corners of Japan that I'd never seen before. I hope I have captured some of the beauty I witnessed in my drawings so you can travel vicariously through this art book. The last time I traveled to Japan was back in 2019. It was the last international trip I did before we all had to stay home for 2 years, and I'm so glad I was in Japan to soak in all the beautiful colours. I went in late Autumn for 21 days and was just in time to see some dark red Momiji leaves and bright yellow Ginkgo leaves before they had all fallen.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art3.jpeg",
                end_date = date(2024, 11, 2),
                reward_name = "Book of Spring",
                reward_amount = 25,
                reward_description = "Do you like blossoming Momo and Sakura? This art book contains 38 paintings of beautiful sceneries of Japan in Spring.")
    art4 = Project(
                project_name = "Handcrafted Japanese Artisan Ceramics: Traditional Technique",
                description = "The beauty of traditional Japanese ceramics with our handmade artisanal pieces",
                category_id = 1,
                money_goal = 10713,
                user_id = 5,
                city = "Madrid",
                state = "NM",
                story = "Introducing the Japanese Artisan Ceramic Project, a unique collection of handmade ceramic pieces crafted by skilled artisans in Japan. Our collection features a wide variety of ceramic products, from tea cups and bowls to vases and decorative plates, each one exquisitely crafted to bring a touch of Japanese elegance and style to your home. Our artisans have been perfecting their craft for generations, using traditional techniques passed down from their ancestors. They hand-mold, paint and fire each piece with precision and care, creating a one-of-a-kind piece that's unlike anything else you'll find on the market. The Japanese Artisan Ceramic Project is not only about bringing beautiful pieces into your home, but also preserving a cultural tradition that dates back centuries. By backing our campaign, you'll be supporting these skilled artisans and helping to keep this timeless craft alive for generations to come.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art4.png",
                end_date = date(2024, 7, 25),
                reward_name = "Ceramic Bowl",
                reward_amount = 20,
                reward_description = "Pledge $20 or more and receive one of our artisan ceramic bowls. Perfect for daily use or as a decorative piece in your home.")
    art5 = Project(
                project_name = "Visions: The Art of Jeff Sturgeon",
                description = "A Retrospective of a decades-long career in fine art by award-winning artist Jeff Sturgeon",
                category_id = 1,
                money_goal = 6000,
                user_id = 4,
                city = "Seattle",
                state = "WA",
                story = "Jeff Sturgeon is a northwest artist known for his beautiful, award-winning metal paintings. His career spans over thirty years, coming up through the ranks as a young fan artist in the 80s to being hired in the first wave of computer game artists in the late 80s and early 90s. A long career in the 90s as an artist, animator, concept artist, lead artist, game designer, and art director followed most notably for Electronic Arts. He continued to paint and display his work at science fiction conventions around the country and created new cover and interior work for clients such as Harper Collins Publishing and NASA JPL. Jeff left the game business behind and went to painting full time with aluminum as his new canvas though he did not give up traditional canvas completely. Through the new millennium, Jeff's work became nationally known with increased appearances as an exhibitor, guest, panelist, and Guest of Honor at conventions around the country. Jeff's world-sharing anthology Jeff Sturgeon's Last Cities of Earth was released in Jan. 2022 by Word Fire Press. His continued work in the Last Cities of Earth universe now takes up most of his time as he creates new art and stories and works towards releasing a second anthology.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art5.jpeg",
                end_date = date(2024, 2, 13),
                reward_name = "VIRTUAL GALLERY - EARLY SHOWING",
                reward_amount = 10,
                reward_description = "You receive a full-color PDF of THE ART OF JEFF STURGEON and our thanks in the back of the book.")
    art6 = Project(
                project_name = "The Earhart Project",
                description = "Development and workshop for a solo show on Amelia Earhart",
                category_id = 1,
                money_goal = 9682,
                user_id = 5,
                city = "New York",
                state = "NY",
                story = "It's never too early and never too late to pursue a dream that you know will make a difference. This is why I will be creating an exciting new show that will prepare me for the bigger project ahead of me. Your helping me with this project will be the tipping point that will make what's to come possible.   This project will make you laugh. You may want to cry, but I can't guarantee that. You may be inspired to take more risks in your life. You will learn interesting things about Canadian history. You may even want to buy a plane.  Amelia speaks to so many young girls and women.  She was a powerful, flawed woman. She was a symbol of hope during the stock market crash in the 1920s during difficult times in the 20s. Now is the perfect time to hear her words again. Amelia Mary Earhart was an American aviation pioneer and writer. Earhart was the first female aviator to fly solo across the Atlantic Ocean in 1932. Oh, but there is so much more.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art6.jpeg",
                end_date = date(2023, 12, 23),
                reward_name = "Shout-out",
                reward_amount = 5,
                reward_description = "A shout-out thank you on social media and haiku poem( when the workshop performance happens.")
    art7 = Project(
                project_name = "Help Bring Woven to the Fringe!",
                description = "An original musical inspired by The Odyssey debuts at the Fringe! Seven women, one wake, and the truth that weaves them together.",
                category_id = 1,
                money_goal = 12000,
                user_id = 4,
                city = "Albany",
                state = "NY",
                story = "Woven is an original musical that takes a classic tale and flips it on its head. It's about dreams and deception. It's about lies and liaisons. Most importantly, it's about the beauty of female friendship. Set in the present day, seven women attend a wake where they discover that their lives are mysteriously intertwined. Now, they must untangle the threads. Inspired by Homer's The Odyssey, Woven tells the story of women coming together as the truth comes to light. As the late, great Stephen Sondheim said, 'Art isn't easy.' Creating new work is ambitious and demanding. It takes passion and perseverance as well as excellent time management and a clear vision. More often than not, the success of a new show depends largely upon the support of the public. For this Kickstarter, we are raising $12,000 to help us make our dreams a reality!",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art7.jpeg",
                end_date = date(2023, 11, 20),
                reward_name = "The Hera",
                reward_amount = 15,
                reward_description = "The creator of Woven will give you a shout-out on social media or send a personalized 'thank you' via email. Donor's choice!")
    art8 = Project(
                project_name = "Chicken-Inspired Improvised Woven Art",
                description = "Embracing creative constraints, jazz guitar, a whole bunch of yarn, and beautiful chickens.",
                category_id = 1,
                money_goal = 250,
                user_id = 5,
                city = "Portland",
                state = "OR",
                story = "I am improvising woven art. I have no idea what they will look like until I start weaving, but each one will be inspired by one of five chicken breeds: Wyandotte, Australorp, Barbu d'Uccle, Lavender Orpington, and Silkie. I think a fun way to think of this is that you're taking home a baby chick of one of the five breeds -- while you may not know the exact plumage they will grow into, you might have a pretty good general idea what they would look like!",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art8.jpeg",
                end_date = date(2023, 9, 30),
                reward_name = "A postcard with a watercolor sketch",
                reward_amount = 10,
                reward_description = "Thank you for supporting this project! I will watercolor sketch a chicken doing chicken things. Please note that this sketch won't have as much detail as the chicken painting in the project page. On the back of the postcard, you will find a random chicken fact that you can impress your friends and family with!")
    art9 = Project(
                project_name = "Lonesome Pictopia: Exquisite Wallpaper",
                description = "Transforming interiors with traditionally-printed wallpaper inspired by design history, botanicals, and American tattooing.",
                category_id = 1,
                money_goal = 35000,
                user_id = 4,
                city = "Portland",
                state = "OR",
                story = "We aim to produce the most beautiful, interesting wallpapers since the Arts and Crafts movement: creative, timeless, hand-illustrated designs with a deep connection to design history. Our beautifully tactile papers are being traditionally printed in England. We are thrilled to be partnering with experienced manufacturers of high-end wallpaper who lead the industry in green printing. Obsessively designed, original wallpapers reflecting 15 years experience as a custom tattoo artist, our passion for historic design and botany, and our belief that all work should create social good.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art9.jpeg",
                end_date = date(2024, 1, 23),
                reward_name = "Thank-You Card and Sticker",
                reward_amount = 8,
                reward_description = "You will receive a handwritten thank you card mailed to your old-fashioned mailbox, plus one of our lovely handclasp stickers.")
    art10 = Project(
                project_name = "Cat Hell Enamel Pins Collection",
                description = "A collection of enamel pin inspired cats based on creatures of the night with a cute and chubby look.",
                category_id = 1,
                money_goal = 535,
                user_id = 5,
                city = "Austin",
                state = "TX",
                story = "In this project I wanted to combine kittens with one of my favorite hobbies! creatures of the underworld and vampires.  All the designs have an aesthetic between cute, chubby and a little bit gothic. The project is based on 4 pins but there are more designs that I will show you later with surprises!",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art10.png",
                end_date = date(2024, 2, 21),
                reward_name = "1 Enamel Pin",
                reward_amount = 12,
                reward_description = "Enamel Pin of your choice")
    art11 = Project(
                project_name = "Enamel Wire Trees on Selenite Crystals: Nature's Beauty",
                description = "Experience nature's beauty with our Enamel Wire Trees on Selenite Crystal sculptures. Delicate wire trees perched on stunning selenite.",
                category_id = 1,
                money_goal = 558,
                user_id = 4,
                city = "Philadelphia",
                state = "PA",
                story = "Selenite's translucent and fibrous structure, combined with its smooth texture and pearly white color, creates a captivating aesthetic beauty. It's neutral white tones provide the perfect contrast to the colorful beauty of enamel art.   Selenite crystals are believed to cleanse and purify energy in your home, promoting calmness and mental clarity. They can create a peaceful atmosphere, aid in energy healing, and enhance meditation practice.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art11.jpeg",
                end_date = date(2024, 2, 15),
                reward_name = "Small Bonsai Selenite Sculpture",
                reward_amount = 75,
                reward_description = "Your choice of any of the four smaller tree designs mounted on Selenite.")
    art12 = Project(
                project_name = "California Delta Communities Volume 1",
                description = "A Coloring Book about the animals, environment and cultures that call the California Delta network home.",
                category_id = 1,
                money_goal = 12000,
                user_id = 5,
                city = "Stockton",
                state = "CA",
                story = "This is a project that will require not only archival research but also visual and auditory documentation of the beauty of life in the Central Valley. A community focused project like this is best when everyone is involved so that I can create the best examples, in coloring book form, of life in the Central Valley. I have included some examples of this from projects I have run in recent years. Much of the cost of this project is linked to the very real need for reference data collection regarding humanity and its engagement with the environment of the Central Valley of California. I intend to create an accessible archive of imagery and project notes to make this information more widely available to the global public. Both of these activities will create a stronger background of material from which to illustrate the Central Valley with. When surveyed, elementary students in San Joaquin County want to know why placenames are what they are, who lived here before our cities were constructed, what foods grandmothers in their friends' houses serve that reminds them of home, and so much more. Those are all questions that can be addressed in this project's accompanying research collection efforts. The second goal of this project is to create a visual archive of life in the Central Valley, its environment, and its people. This archive will be made available to the public for access by future generations.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/art12.png",
                end_date = date(2023, 11, 3),
                reward_name = "Shout out on the Community Website",
                reward_amount = 1,
                reward_description = "Show your support for the California Delta Communities Coloring Book and be listed on the Backer Wall of Fame page I will be creating for the archive website.")
    comic1 = Project(
                project_name = "The Shadow Over Innsmouth Graphic Novel",
                description = "Get the softcover and hardback editions of Lovecraft's classic story in this beautifully drawn and acclaimed comic book adaptation.",
                category_id = 2,
                money_goal = 1245,
                user_id = 4,
                city = "Savannah",
                state = "GA",
                story = "Robert Ormstead is on his way from Newburyport to Arkham the cheapest way possible. Unfortunately, for him, this means taking the bus through shadowed Innsmouth. Armed with his notebook, he intends to make a day of it studying the local architecture and getting to know more about this mysterious place that neighbouring towns shun. Why are the inhabitants so unwilling to speak to him, and what curse afflicts them which causes their faces to change and their eyes to stare, unblinking. Come along for the ride in HP Lovecraft's famous story, 'The Shadow Over Innsmouth', adapted by Simon Birks, with art by RHStewart and lettered by Lyndon White, the team that created the critically acclaimed 'Sinners' series.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic1.jpeg",
                end_date = date(2024, 3, 03),
                reward_name = "Virtual Hi-Five",
                reward_amount = 5,
                reward_description = "Be a part of the campaign and receive backer only updates, plus get access to the pledge manager at the end of the campaign! And thank you!")
    comic2 = Project(
                project_name = "When Language Fails",
                description = "A 30 page, one-shot comic about family, not fitting in, war, and clowns.",
                category_id = 2,
                money_goal = 2356,
                user_id = 5,
                city = "Fargo",
                state = "ND",
                story = "When Language Fails is a 30 page, one-shot comic with a completely self-contained story. It is the story of Adele and Sarah, two estranged sisters who are thrown together on the outbreak of a strange, unknowable war. They must try and repair their relationship, figuring why they have grown apart, and what went wrong, all while trying to survive the war that has erupted on their doorstep. When Language Fails is about growing up, not fitting in, and family. It is also about war, and violence, and how most of the world lives insulated from these awful realities. It asks what we would do if we were actually faced with violence and war in our own homes.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic2.jpeg",
                end_date = date(2024, 2, 25),
                reward_name = "Digital Deluxe",
                reward_amount = 4,
                reward_description = "Deluxe PDF of When Language Fails with tons of process and behind-the-scenes. Includes full scripts, full black and white artwork, character designs, introduction from writer Colin O' Mahoney talking about the genesis of the project, and as much more process material as we can come up with.")
    comic3 = Project(
                project_name = "Crater City [The Complete Graphic Novel]",
                description = "Being sixteen can be weird, but being sixteen and living in a city built inside a giant meteor crater can be weirder!",
                category_id = 2,
                money_goal = 5000,
                user_id = 4,
                city = "Miami",
                state = "FL",
                story = "Famously built inside one of the world's largest meteor impact zones, the town of Crater City hosts an annual celebration of the city's namesake with a weekend-long treasure hunt popular with locals and tourists from around the world. The challenge- find the missing piece of the famed Bollinger meteorite, excavated from the crash site forty years ago, which is currently on display in the city's museum.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic3.jpeg",
                end_date = date(2024, 6, 11),
                reward_name = "Digital Copy",
                reward_amount = 10,
                reward_description = "Grab a digital copy of Crater City. Thats 120 pages of sci-fi alien ass kicking. PDF, CBZ, OR CBR formats available. Once Kickstarter ends, you will immediately receive Issue #1 as a thank you!")
    comic4 = Project(
                project_name = "Don't Talk to the Dead #1 - A Supernatural Adventure",
                description = "The Goonies meets Dante's Inferno; a group of friends must travel to Hell to rescue the soul of a loved one.",
                category_id = 2,
                money_goal = 1000,
                user_id = 5,
                city = "Rochester",
                state = "NY",
                story = "'Infernal Goonies' takes place in a small coastal town where a group of lifelong friends, known as the Goonies, live out their days exploring hidden caves, seeking adventure, and forming a tight-knit bond. Their peaceful lives are shattered when tragedy strikes, and the soul of one of their loved ones is unfairly condemned to Hell. Determined to save their friend's soul, the Goonies stumble upon an ancient tome that reveals a hidden portal to the underworld. They discover that the portal, guarded by riddles and challenges, leads to the very depths of Hell, mirroring the nine circles described in Dante Alighieri's 'Inferno.' Armed with their wits, courage, and the unconditional love for their friend, they embark on an extraordinary journey into the unknown",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic4.jpeg",
                end_date = date(2024, 4, 15),
                reward_name = "Digital Edition",
                reward_amount = 7,
                reward_description = "26 pages of story!")
    comic5 = Project(
                project_name = "Hunt For The Skinwalker",
                description = "Reserve your copy of the essential true paranormal UFO investigation book now in an expanded edition and the graphic novel it inspired!",
                category_id = 2,
                money_goal = 15000,
                user_id = 4,
                city = "Los Angeles",
                state = "CA",
                story = "Situated on a remote stretch of northeast Utah known as the Uinta Basin, the isolated, 512-acre  Gorman Ranch has been the site of terrifying, mystifying, and category-defying phenomena for more than 50 years! Since Dr. Colm A. Kelleher and veteran journalist George Knapp broke the unbelievable true story with the publication of HUNT FOR THE SKINWALKER: Science Confronts the Unexplained at a Remote Ranch in Utah in 2005, the site's seemingly limitless barrage of overlapping and interconnected supernatural occurrences have quickly secured its place as the 21st century's most captivating, most debated, and most rampantly viral true tale of the paranormal and truly unexplainable. Award-winning and bestselling publisher BOOM! Studios is working directly with Kelleher and Knapp to remaster and expand their groundbreaking book in a premium Declassified hardcover edition, and publish the first graphic fiction adaptation based on THE HUNT FOR THE SKINWALKER – the most intensive scientific investigation into this nexus of UFOs and the paranormal ever conducted!",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic5.jpeg",
                end_date = date(2024, 5, 23),
                reward_name = "Skinwalker Graphic Novel Softcover",
                reward_amount = 25,
                reward_description = "Discover the unbelievable, unexplainable, and yet, undeniable true story of Gorman Ranch, which became an epicenter for horrifying supernatural occurrences and the site of the most expansive scientific study of the paranormal ever conducted… visualized for the first time in graphic novel form!")
    comic6 = Project(
                project_name = "Lampblack #1-3: Fantasy Horror Comic in Cinematic Style",
                description = "A girl whose paintings come to life. A Deaf boy who wants to be a soldier. A story of passion, art, and war inspired by Studio Ghibli.",
                category_id = 2,
                money_goal = 8000,
                user_id = 5,
                city = "San Fancisco",
                state = "CA",
                story = "LAMPBLACK is a limited comic series written by Camille Longley with art by Pablo Peppino and letters by Joel Saavedra. It's an oversized 8.5x11 inch landscape comic in a sweeping cinematic style. Lampblack has everything you expect in a coming-of-age story: horrifying ink monsters, wondrous forbidden magic, American Sign Language, runaways, and a cat (of course). Lampblack is a story of friendship, family, and war, set in a fantastical world depicted in stunning detail. If you're a fan of Studio Ghibli, Fantastic Beasts and Where to Find Them, Sabrina, or Pokémon, you will love exploring the world of Lampblack--a place filled with incredible creatures and fascinating magic.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic6.jpeg",
                end_date = date(2024, 8, 30 ),
                reward_name = "Issue #3 Digital",
                reward_amount = 6,
                reward_description = "This enormous landscape comic has wrap-around covers that measures 22 by 8.5 inches that truly captures its cinematic glory.")
    comic7 = Project(
                project_name = "STUFF: A Book About Aliens",
                description = "4 Armies, 4 Planets, 4 Heroes breaking out of a fully armed battle station beginning an absurd adventure across an absurd universe.",
                category_id = 2,
                money_goal = 1500,
                user_id = 4,
                city = "Somerville",
                state = "NJ",
                story = "Travel to a universe of novelty and absurdity where a villainous plot is engineered by a military strategist and his alien armies. Through the mysterious Operation Eye-Chest, four alien heroes are kidnapped and their homes threatened. These aliens try their hardest to avoid working together as they escape a fully armed battlestation, operated by ravenous creatures, robots, mad scientists, and ants. Bizarre, immature, and hard to take seriously; this science fiction adventure is ripe with constant bickering, clumsy action, and numerous onomatopoeias. A universe like this combines the exciting world building of Ben 10 and Pokemon, with the absurd humor of Invader Zim and Adventure Time.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic7.jpeg",
                end_date = date(2024, 4, 12 ),
                reward_name = "STUFF Chapter 1 Physical Edition",
                reward_amount = 12,
                reward_description = "The REAL STUFF Chapter 1 to have and to hold like the reading days of old. Own a physical copy of STUFF marked with actual coffee stains.")
    comic8 = Project(
                project_name = "Hamfam - Welcome to the aporkalypse!",
                description = "A 25 page digital comic set in a post-apocalyptic World about a pig with eyes in his nose and his friends quest to continually party!",
                category_id = 2,
                money_goal = 2490,
                user_id = 5,
                city = "Athens",
                state = "GA",
                story = "Hamfam - a 25 page digital comic set within a dark, dangerous wasteland - following the exploits of a surreal and quirky pig! The World has ended, but the party has just begun! Hamfam is more than a pig, more than a place - it's a way of life.​Hamfam, a humanoid pig with eyes in his nose - balances his public personna as a general within a dystopian heirachy, with the need to continuously party. He shares this self-imposed mission with best friends Xeno and Dred, with an ever growing following of misfits and deviants. Enter the World of Hamfam, the most surreal & crazy ride you'll experience through a comic!",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic8.jpeg",
                end_date = date(2024, 2, 28 ),
                reward_name = "25 page digital Hamfam comic with extras",
                reward_amount = 10,
                reward_description = "A digital page Hamfam comic + extra artwork, character studies and story previews - equivalent to an accompanying artbook!")
    comic9 = Project(
                project_name = "GUNK: Volume 1 and 2 Reprint",
                description = "A set of low brow vintage horror and sci-fi inspired comic zines",
                category_id = 2,
                money_goal = 1000,
                user_id = 4,
                city = "Santa Ana",
                state = "CA",
                story = "It has been many moons since anyone has laid eyes upon the ancient comic tome known to a special few as GUNK, the bastard creation of the mad artist, Curt Merlo.  But finally, after much anticipation, the first ever reprinting of the 2018 occult classic comic zine is among us! Those who experienced the original book recall it as an inky exploration into the bizarre world of pulpy vintage horror and strange romance but they did not live long after such verbosities. I myself, dare not attempt an explanation of said relic. It is best to leave understanding to your own eyes. Now, focus beyond this material plane and into the graveyard of forgotten books and you may be lucky enough to witness the specter of the aforementioned monstrosity that is GUNK: Volume 1. Behold!",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic9.jpeg",
                end_date = date(2024, 3, 28 ),
                reward_name = "GUNK: Vol 1 & Vol 2 (Digital E-Book)",
                reward_amount = 10,
                reward_description = "Get a digital version of the first book GUNK: Volume 1 and a digital version of GUNK Volume 2. Two 36 page PDFs of vintage pulpy gore.")
    comic10 = Project(
                project_name = "Fox Fires Book Two",
                description = "Inspired by Finnish mythologies about a young raccoon dog's quest to find her family continues.",
                category_id = 2,
                money_goal = 3000,
                user_id = 5,
                city = "Doylestown",
                state = "PA",
                story = "Raate's quest for the missing fox fires continues. This time she gets mixed up in the otters' Shining Skies ceremony. But all the preparations don't go as smoothly as planned. We meet new characters and the official first antagonists of Raate. FOX FIRES is a fantasy-adventure comic that's heavily inspired by Finnish folklore. “Fox Fires” refers to Northern Lights; it's basically a literal translation from the Finnish word “revontulet.” (Revontulet = Repo's fires. Repo is a nickname for a fox in the Finnish language.) The Fox Fires are a gate between this world and the land of the dead - it allows souls to visit their loved ones. But suddenly, the Fox Fires disappear. Our main character, a young raccoon dog named Raate, heads north to find what's happened to Repo, the fire fox whose burning fur is said to make the Fox Fires appear in the sky. On her journey, Raate meets all kinds of weird creatures, and also new friends.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic10.jpeg",
                end_date = date(2024, 7, 28 ),
                reward_name = "Fox Fires Book Two Graphic Novel",
                reward_amount = 24,
                reward_description = "Get the Fox Fires Book Two Graphic Novel, printed at 5.7'x8.2' with a matte finish wrap-around hardcover - approximately 150 pages of content!")
    comic11 = Project(
                project_name = "Rusalka - Whispers of the Forest",
                description = "A mythical woman with strange powers and a dark secret. Discover this dreamlike folk tale, inspired by Slavic mythology.",
                category_id = 2,
                money_goal = 7500,
                user_id = 4,
                city = "Boulder",
                state = "CO",
                story = "Rusalka is a mysterious water demon of Slavic mythology: living by the lake in the ancient Forest, she is the deadly threat luring in lost wanderers...or so the old legends say. But who really is Rusalka and how did she come to be?  Where do her powers come from and what dark secrets might hide in her fragmented memories? You are invited once again to enter the ominous Forest, and unravel its dark secrets. Following Rusalka in her journey of self-discovery, you will stumble upon other creatures present by Eastern European myths, such as the mischievous water demon Vodnik or the deity of the underworld Veles.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic11.jpeg",
                end_date = date(2023, 12, 28 ),
                reward_name = "Ghostlight | A Digital Copy of Rusalka",
                reward_amount = 7,
                reward_description = "You will receive a digital copy of Rusalka that you may read digitally!")
    comic12 = Project(
                project_name = "Haunted Hill: The Complete Volume 1",
                description = "A Surrealist Soap Opera About Life in Hollywood",
                category_id = 2,
                money_goal = 1489,
                user_id = 5,
                city = "Chicago",
                state = "IL",
                story = "What if you and everyone else had to act like adults with big feelings and serious intentions even though treehouse passwords worked, detective clubs solved major crimes and you really don't fall until you looked down? Welcome to Haunted Hill. This graphic novel series functions like a surrealist soap-opera as it follows Eva in pseudo-real time, navigating life in the grime of Hollywood. This is a town where even the smallest moments become charged with impossibility as people search for high-stakes in the lowest places. Loosely based on a true story, but capturing what every night in Hollywood felt like at the beginning of 2020.",
                project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/comic12.jpeg",
                end_date = date(2023, 12, 18 ),
                reward_name = "The Digital Book",
                reward_amount = 10,
                reward_description = "It's like a real book, only on your screen. Tired of lifting a heavy book to read? This digital edition is a great alternative. All the same stuff as in the book, but in a PDF instead.")
    project_m1 = Project(
        project_name = "A lyrical tribute to my Godson",
        description = "I am a full-time missionary and preacher. 12 years ago, my godson's life was taken in a horrendous fire. Help promote my tribute to him",
        category_id = 7,
        money_goal = 500,
        user_id = 10,
        city = "New York",
        state = "NY",
        story = "I am budgeting that it will take about $500 to launch the website, a viral video, and a media campaign to promote my commemorative song for my godson. Of course, this is the minimal amount of money I expect to be needed. With the more funding I receive, I will be able to, reach more people and potentially help them in their grieving process as well. Thank you so much, and God bless you!" ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m1.jpg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = None,
        reward_amount = None,
        reward_description = None,
    )
    project_m2 = Project(
        project_name = "Alicia Svigals Klezmer Fiddle Album",
        description = "A long-overdue followup to my 1997 album Fidl! Traditional and original tunes and songs, backed up by the klezmer world's top players.",
        category_id = 7,
        money_goal = 500,
        user_id = 10,
        city = "New York",
        state = "NY",
        story = "I'm finally, finally, finally recording a followup to my 1997 debut album, Fidl!  And I'm going to have the very best klezmer musicians in the world with me." ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m2.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = None,
        reward_amount = None,
        reward_description = None,
    )
    project_m3 = Project(
        project_name = "New Worm Quartet Album ~ Carpe Tedium",
        description = "Help Shoebox a.k.a. Tim Crist a.k.a. The Pac-Man Guy fund the release of his new comedy synth-punk album!",
        category_id = 7,
        money_goal = 700,
        user_id = 10,
        city = "Rochester",
        state = "NY",
        story = "Hello!  My name is Shoebox.  You might know me from my incredibly-inaccurately-named one-man comedy music project, Worm Quartet. Or from my fifteen minutes of fame from 2004 that absolutely refuse to die as The Pac-Man Guy. Or you may be in the majority of people who have no idea whatsoever who I am.I've been making comedy music in various forms for several decades.  In that time I've played hundreds of shows, I've put out 5 full-length albums and an EP, I won the first-ever Logan Whitehurst award for Outstanding Original Comedy Song, and I had the most requested song of the year on the Dr. Demento show two years in a row.That said, nobody who understands the definition of the word prolific would ever suggest that it should be applied to me. While I did release a 3-song digital single last year and an EP of Pac-Man songs in 2020, my last full-length release was in 2011.  But over the last several years I've put together a collection of new songs that I'm very proud of - much of it melt-tested on the faces of various concertgoers over the last several years, some of it unheard up to this point - and I'm finally ready to release my new album,Carpe Tedium" ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m3.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "Carpe Tedium Digital Download",
        reward_amount = 10,
        reward_description = "High-quality digital download of the new album before it's available to the unwashed masses",
    )
    project_m4 = Project(
        project_name = "Lisa Bastoni: New Album!",
        description = "Creating a new album of original songs, recorded live in-studio.",
        category_id = 7,
        money_goal = 10000,
        user_id = 10,
        city = "Northhampton",
        state = "MA",
        story = "Hi! My name is Lisa Bastoni, and I am a songwriter living in Northampton, Massachusetts. I am launching this kickstarter today to raise funds for a new record - my first full length album in five years!For the first time in my musical life, I will be recording the songs live with a great band in the studio. I would greatly appreciate your support, and would love to have you along for the ride.If you have known me for awhile, then you know that I have taken a twisty kind of a path through music and art (and life) over the past 20+ years, always coming back to music, or art, or both. The two are completely entwined, and I can't imagine my life without one or the other. Since our last full-length record was released in 2019, I've been able to focus more on the art side of things, including a number of lyric videos for other songwriters, re-entering the day job work force as a part time elementary school art teacher, and culminating with my first ever art show, currently on display at Club Passim. It's all work that I deeply enjoy, though lately I've felt a calling back to music." ,
        project_image = "",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "Digital Download",
        reward_amount = 15,
        reward_description = "You'll receive Mp3/wav files of the complete album, including liner notes, delivered in advance of the official album release.",
    )
    project_m5 = Project(
        project_name = "Song of Songs",
        description = "A conceptual music album exploring the theme of love and featuring orchestral arrangements",
        category_id = 7,
        money_goal = 20000,
        user_id = 10,
        city = "Buffalo",
        state = "NY",
        story = "Song of Songs is a conceptual album. Its name is inspired by the Song of Songs, an ancient Hebrew poem about love. The lyrics explore the theme of love in all its variety and diversity: both the dark side of it and love in all its glory.I have deep interest in psychology and personal development and I have been studying this theme for a few years through research and reading. This album is going to explore both romantic and non-romantic (familial, spiritual, platonic) love. The songs will take the listeners on a journey from trauma and love addiction to unconditional love and healthy interdependent relationships, from the illusion of separation to the feeling of connectedness and unity and universal love. And of course I will also be sharing my personal experiences and stories through my songs, as I always do. ♡Song of Songs is going to be my first album with live orchestral arrangements and I have been preparing for this for many years. When I started writing my songs, the arrangements were quite simple: the classical jazz trio and the electric guitar. My sophomore effort featured more intricate arrangements where I added both synths and strings sections with multi-layered cello arrangements. Now, on my third LP, orchestral arrangements will add even more depth and detail to my music and will also give it a more timeless, classical sound." ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m5.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "Early album download",
        reward_amount = 15,
        reward_description = "A link to the album download (MP3 or WAV + artwork) one day before the official release",
    )
    project_m6 = Project(
        project_name = "Lakewood Jump - Keenan McKenzie & the Riffers' New Album",
        description = "It's time to finally record a full-length album!",
        category_id = 7,
        money_goal = 500,
        user_id = 10,
        city = "Durham",
        state = "NC",
        story = "We're Keenan McKenzie & the Riffers, a band specializing in music from the 1930s/40s and original material. Over the past year, the Riffers have appeared at dance events like Lindy Focus, New York Bal Week, The California Balboa Classic, I *Heart* Bal, The School of Hard Knox, Flying Home, and the DC Lindy Exchange. We've added a ton of new material to the book, and it's finally time to record a full-length album!" ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m6.jpg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "Digital Album",
        reward_amount = 15,
        reward_description = "Get the album before it's publicly released! You will also receive a shout-out on social media.",
    )
    project_m7 = Project(
        project_name = "Fund French singer Marine Futin to record new music in NYC!",
        description = "I am a French singer songwriter and I live in Brooklyn. I write, compose, & produce songs that blend songwriting, jazz and world music.",
        category_id = 7,
        money_goal = 10000,
        user_id = 10,
        city = "New York",
        state = "NY",
        story = "I have started to record early 2023 at Flux Studio in New York.I need your support to keep it going, and fulfill my vision for this project!I am working on 3 songs as of now - and I have 6 more in the pipeline. Whith every song, I want to shoot a cool music video" ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m7.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "Songs",
        reward_amount = 25,
        reward_description = "You'll get each song before their public release from September 2023 to December 2024. \n Vous recevez chaque chanson par email avant leur sortie officielle.",
    )
    project_m8 = Project(
        project_name = "Nohmad - Seulah Noh's Debut Full-Length Album",
        description = "Seulah Noh's bold debut onto the scene with the Seulah Noh Jazz Orchestra!",
        category_id = 7,
        money_goal = 15000,
        user_id = 10,
        city = "Boston",
        state = "MA",
        story = "Nohmad is the debut album of Korean composer and pianist, Seulah Noh! Combining her award winning compositions with her incredible band, “Nohmad” will offer a genuine reflection of Noh's personal experience and a window into some of her influences.\n Noh makes a lasting first impression, offering six original compositions and two arrangements on this debut release. From gentle melodies to hard hitting grooves, Noh cultivates an infectious energy that her band carries throughout the record. Her most recent work, the “Traveler's Suite” is a reflection of the experiences, impressions, and thoughts she has gathered throughout her time in the United States as a person coming from a different culture. “Nohmad” will be the first snapshot of Noh's compositional work and the beginning of an exciting journey as she continues to work and grow with her band!/nThis Kickstarter will help us to finish this project and make Nohmad accessible to all of you, wherever you may be! The funds will be used to pay for studio time, engineers' fees, mixing and mastering, distribution, artwork, and other expenses related to the album's release. We are so grateful for your consideration and any contribution you can make!" ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m8.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "Digital Album",
        reward_amount = 15,
        reward_description = "Digital download of the full record!",
    )
    project_m9 = Project(
        project_name = "Sugar Nova Debut Album - Halogen",
        description = "Luke Miller (Lotus) & Rachel Eisenstat (Raven Jane) are launching the debut Sugar Nova album and need help paying for the vinyl costs",
        category_id = 7,
        money_goal = 3000,
        user_id = 10,
        city = "Denver",
        state = "CO",
        story = "Luke Miller (from Lotus) and Rachel Eisenstat (from Raven Jane) formed Sugar Nova as a musical project to make indie-electronic-pop songs featuring Rachel's vocals and Luke's production. The songs were written during the pandemic and then recorded as things re-opened. We recorded the vocals at Evergroove Studio in Evergreen, CO. And did the production at Luke's home studio in Denver. The album was mixed and mastered by Rob Murray of Wilderfox Studio. Rob has worked with artists such as Odesza, Big Wild, Mark Ronson, and, Sia. \n We released our first track Send Me Higher in Sept. 2022 and are set releasing our debut album Halogen on May 12th, 2023." ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m9.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "HD Digital Version of Halogen",
        reward_amount = 10,
        reward_description = "Get an early version of the debut Sugar Nova album Halogen in the highest quality.",
    )
    project_m10 = Project(
        project_name = "Trees: A Record",
        description = "a debut record about trees, for people.",
        category_id = 7,
        money_goal = 800,
        user_id = 10,
        city = "Minneapolis",
        state = "NY",
        story = "I've been writing music pretty much all my life. In March, I released my debut single, called Holly. Now, with your help, I hope to make a full-length record about trees, for people. As deep as I've searched, I haven't found another project like this. In fact, songs about trees seem to be a big, blank space in the music industry.\nWhy trees? They're everywhere. Look out the window, you can probably see four or five right now. Look on the first and last pages of the bible. Look at the coffee shop you frequent and your favorite place to hike. It's hard not to see them once you start looking.\nPeople need tree songs because in many senses, people are trees. That's what this record explores. It touches on things from missing your old self, to faith, to joy, to sunsets and Van Gogh paintings. There will be creepy tree songs, sad tree songs, and tree songs you can dance to. I hope it will give you that magical feeling of not being alone and the courage to keep going. To drink deep from your roots and stretch your branches closer and closer to the sun. To watch your leaves turn from green to red and fall, learning to let them go for the winter.\nI'm an independent, relatively unknown artist. That means I don't have a whole bunch of cash lying around, or a record label supporting me. That's where you come in. In exchange for some delightful rewards, you can help this record come to life.  Not only will you be supporting me and the people helping me make these songs, but you'll also be supporting my future listeners who will hopefully be blessed by them.\nThere are several different levels of support you can choose, and many fun rewards that go along with them. Choose whatever type of tree you want to be; any support will be greatly appreciated!!" ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m10.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "seedling",
        reward_amount = 10,
        reward_description = "get a high-quality digital album and liner notes once it releases, plus exclusive updates along the way!",
    )
    project_m11 = Project(
        project_name = "Michelle SgP YOLO Album Launch 2023",
        description = "Crossover Classical-Jazz EP & videos of original songs bringing together various communities, seizing the day in unpredictable times!",
        category_id = 7,
        money_goal = 500,
        user_id = 10,
        city = "California",
        state = "CA",
        story = "YOLO - You Only Live Once project came about, when I was encouraged by my significant other to pick up the pieces and restart my music creating life again. The pandemic had been tough for many of us,  livelihood, mentally and physically. I must have caught some kind of long covid then, with 6 months of total lethargy, no energy to think of future projects or envision life beyond the day. I had inflammation popping up all over my body, and the last straw breathlessness, that made me ensure I had my Living Will updated in case I didnt make it past the next 2 years intact.\nLike many, I was really on that dark side of the fence.\nSo I figured, if life was really this short, I would then want to embark on this DREAM project working with strings and horns, as I wanted to work more with orchestras, having been inspired by a special project with the Manila Philharmonic, 2 months before the pandemic struck.\nSo I restarted my engine bit by bit. First was to lay down the tracks vocal and piano + rhythm tracks while I was away in Italy. These studios I recorded in, were used by heavyweights as Elton John, and Gregory Porter.  YOLO project comprised working with amazing top musicians and engineers based in Milan(north) and Bari(south). With drafts and other sessions with based in SG Christy Smith, Tama Goh, Audrey Tang, Judy Tsai with engineer Frank Lee. Armed with string and horn arrangements by Bang Wenfu and Germaine Goh, the strings and horns were recorded, many thanks to Lester Kong from Macpherson Philharmonic who also sat in virtually to consult for strings and horns from Singapore while I was up in Italy recording.\nNow with each audio track, a music video had to be made. I wanted to bring together communities for some of these songs. Serenity the video was filmed in panoramic Phuket. I needed a vast space to convey the grandeur sound of the piece. It took journeying up dirt tracks to a hilltop, having the piano carted to the edge, was altogether a journey of passion and special friendship bonding. The video “I Just Want to be Me” brought together communities based in multi-cultural Singapore. Everyone was dancing spontaneously to the happy groove of the song once the speakers blasted.\nThese moments of happiness and joy on each participant's faces, gave me immense joy and deep satisfaction, of my music as a tool bringing people together to celebrate LIFE. While the video Shark Filled Oasis, was conceived to give a big band feel. It celebrates peer friendships, and uplifts musicians, bringing together string and horn professionals in the scene into that one room, many whom I've worked together with at some point prior." ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m11.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "EP Album of YOLO (Digital Download)",
        reward_amount = 20,
        reward_description = "Priority Access! Be the first to receive the full YOLO EP album. Yes you'll receive it all even before you hear the 5-track EP in its entirety online!",
    )
    project_m12 = Project(
        project_name = "Kitshickers 2023 Album & Videogame",
        description = "It is about time to release a new album with a twist...and to celebrate it at our 25th anniversary party.",
        category_id = 7,
        money_goal = 4000,
        user_id = 10,
        city = "Atlanta",
        state = "GA",
        story = "After 2021's amazing event and album together with our friends from The Majestic Unicorns from Hell,we will finally be back with a new album.\nThe album will be in the continuity of the previous albums and the cover/artwork story of our main protagonist will continue.\nThough releasing an album on CD or Vinyl wasn't an option for us this time !\nThe format of our choosing is only digital, BUT coupled to a VIDEO GAME!" ,
        project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/m12.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name = "Album",
        reward_amount = 10,
        reward_description = "Just the album...because you don't like playing games.",
    )

        # Publishing Data

    project_p1= Project(
        project_name ="The Sledgehog",
        description ="An illustrated children's book about a medieval hedgehog that brings heavy metal into the world.",
        category_id = 8,
        money_goal =22500,
        user_id = 11,
        city ="Brooklyn",
        state ="NY",
        story ="The Sledgehog is a 36-page story poem and picturebook for 7 to 12-year-olds about a heavy metal hedgehog called The Sledge.Set in a fantasy world inspired by both 80's metal album art and classic fairy tale illustration, our story begins with the birth of our hero, who embarks on a journey to fulfill her life's purpose — preach metal's creed to all the land.\nGraphic, black and white illustrations combined with powerful prose will create a darkly enchanting picture book that will captivate the minds of children and parents alike.",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p1.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="Curated Heavy Metal Playlist",
        reward_amount =10,
        reward_description ="Support on a budget — a 21-track, family-friendly, metal playlist curated by our author.",
    )
    project_p2= Project(
        project_name ="The Impact of Iwata",
        description ="A new book chronicling the life and achievements of Nintendo's legendary president!",
        category_id = 8,
        money_goal = 29000,
        user_id = 11,
        city ="Lexington",
        state ="KY",
        story ="Satoru Iwata was one of a kind. Millions of gamers around the world got to know him as the President of Nintendo a little over a decade ago, when he began to regularly host the company's Nintendo Direct video presentations, striking that famous pose you see above. He brought news and game announcements Directly to You! . . . but only for a few years. Sadly, Mr. Iwata passed away in 2015, taken from the world far too soon at the age of only 55.\nFollowing that shocking loss, Nintendo fans poured out tributes to his life and career across the Internet, and we at Nintendo Force Magazine dedicated our next issue to him, creating Thank You, Mr. Iwata as our 17th edition. It was received incredibly well, and remains our most popular single issue to this day! But, at the end of the day, it was still a normal NF issue, which meant the pages we were able to allot to celebrating Mr. Iwata's life and achievements had to fit in alongside things like our preview of Yo-kai Watch and our review of Super Mario Maker. Well, no more sharing the page count!\nNintendo Force Magazine just hit its 10-year anniversary earlier this year, and to mark that milestone we're doing something big: We're expanding into book publishing! We want to revisit topics that we first touched on in past issues, and go into more depth and detail than the normal magazine format allows. Which means we can finally tell Mr. Iwata's full story in the way it deserves to be told!",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p2.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="The Digital Tier",
        reward_amount =10,
        reward_description ="Get The Impact of Iwata in digital form, to read on the computer, tablet or mobile screen of your choice!",
    )
    project_p3= Project(
        project_name ="Dirty Blood Trilogy with Limited Edition Hardcovers",
        description ="Penelope Sky has a brand-new fantasy romance trilogy, and you can read the entire trilogy MONTHS before it's available at retailers",
        category_id = 8,
        money_goal = 10000,
        user_id = 11,
        city ="Newark",
        state ="CA",
        story ="Penelope Sky has a brand-new fantasy romance trilogy under her pen name Penelope Barsetti, and you can read the entire trilogy now instead of waiting for it to be available in 2024.\nYep. You read that correctly.\nEnemies-to-lovers…to unlikely allies…to frenemies with benefits…10/10 spice.",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p3.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="Paperback Books",
        reward_amount =120,
        reward_description ="You get an e-books instantly once the Kickstarter ends so you can start reading!\nAnd once your HAND-SIGNED and ANNOTATED paperbacks come in, you can read the story again and see all the little notes Penelope Sky has added in the footnotes.\nWhy she wrote a certain scene, what she was thinking when she wrote it, and hilarious commentary!",
    )
    project_p4= Project(
        project_name ="unicorns: Their Life and Habits - Art Book",
        description ="Illustrations and lore by Jaimie Whitbread, from the years of 2019-2022",
        category_id = 8,
        money_goal =3500,
        user_id = 11,
        city ="Dalls",
        state ="TX",
        story ="While there are probably as many different habits of unicorns as there are unicorns in the world, those who take the time to study them will find that unicorn nature is not altogether different from human nature. Both are often frustrating, sometimes contradictory, and all the time surprising - but, most tellingly, they can both be boiled down into the same vital components:\nThe love of good grazing, good grooming, and good company.\nUnicorns: Their Life and Habits is a celebration of unicorns in all their many forms. Not the wispy, white-clad unicorns of mere legend, but the humble, salt-of-the-earth, occasionally flea-bitten (don't tell them I said that) ungulates that caper through our fields and woodlands.\n(Seriously, please don't let on that I mentioned the fleas)",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p4.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="Book",
        reward_amount =25,
        reward_description ="You get one copy of Unicorns: Their Lives and Habits",
    )
    project_p5= Project(
        project_name ="The Artisan Bacon Cookbook",
        description ="Written by a full-time baconista who owns and runs an award-winning bacon smokehouse and a bacon restaurant",
        category_id = 8,
        money_goal =1500,
        user_id = 11,
        city ="Deleware",
        state ="Ohio",
        story ="In December 2019,I launched a project to raise funds to translate my bacon cookbook into English. Unfortunately, I did not reach that goal. But now, I saved enough money to get the book translated. However, I am still missing a small amount of funds to make it all come together.",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p5.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="eBook",
        reward_amount =25,
        reward_description ="Receive a digital copy of the bacon cookbook Bacon - Moments of happiness translated into English.",
    )
    project_p6= Project(
        project_name ="Bendy Bones and Stretchy Skin",
        description ="A heartfelt picture book about Ehlers-Danlos and invisible illnesses",
        category_id = 8,
        money_goal =5500,
        user_id = 11,
        city ="Eau Claire",
        state ="WI",
        story ="When Abigail is diagnosed with Ehlers-Danlos, at first her classmates don't understand. Abigail doesn't look like she has a disability. What is her special chair for? How do walk breaks help? \nWith friendly illustrations and a lot of heart, Abigail and her mom bring awareness to her invisible illness-and her friendships grow stronger because of Approximately 23% of children in the United States, and 240 million globally, have a chronic condition. And many of these are what are known as an invisible illnesses-so they can be hard to explain! \nWhile this book was written specifically for children with Ehlers-Danlos like me and my daughter, it's our hope that it shines a light on life with other invisible chronic illnesses. \nHaving struggled with ableism and discriminatory comments throughout my life, I can't overstate the importance of literature that helps to shape a more accepting world for our kids. \nRepresentation and resources make all the difference in helping our kids show up for each other, so they can grow up unafraid, undeterred, and utterly confident in their right to be loved and belong.",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p6.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="Thank You!",
        reward_amount =10,
        reward_description ="4x6 sticker sheet featuring 7 waterproof, weatherproof, and UV resistant stickers. Plus a handwritten thank you note!",
    )
    project_p7= Project(
        project_name ="Aloha Everything: A Hawaiian Fairytale",
        description ="A stunning picture book about a courageous girl's journey to embrace the wonders of her island home",
        category_id = 8,
        money_goal =5000,
        user_id = 11,
        city ="Los Angeles",
        state ="CA",
        story ="Welcome to Aloha Everything, a magical story that will take you on a thrilling journey through the breathtaking islands of Hawai'i!In this exciting adventure, you'll encounter mighty canoes crashing over ocean waves, royal hawks soaring high above the clouds, and brilliant lizard creatures jumping nimbly through forest trees! Most importantly, you'll meet a courageous young girl named Ano who learns, grows, and comes to love her island home with all her heart.Since the day that Ano was born, her heart has been connected to her home. But, this adventurous child has a lot to learn! When Ano begins to dance hula — a storytelling dance form which carries the knowledge, history, and folklore of the Hawaiian people — Ano comes to understand the true meaning of aloha.Aloha Everything is both a captivating read and a fantastic educational resource for learning about Hawaiian history, ecology, and culture. With breathtaking hand-painted illustrations and a beautiful rhyming scheme that will lull little ones into brilliant dreams of vibrant adventure, this book is sure to capture the hearts of both children and parents alike.",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p7.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="eBook",
        reward_amount =15,
        reward_description ="Receive a digital copy of Aloha Everything, as well as the read-along audiobook",
    )
    project_p8= Project(
        project_name ="Nevermore: An Anthology Inspired By Edgar Allan Poe",
        description ="A feast of creepy stories from a host of dark fantasy writers",
        category_id = 8,
        money_goal =10000,
        user_id = 11,
        city ="Charlotte",
        state ="NC",
        story ="Are you ready for a spine-tingling journey through the depths of darkness? Falstaff Books is excited to present Nevermore, an anthology of short stories based on the masterpieces of the one and only Edgar Allan Poe.\nThis collection includes eighteen original stories written by talented contemporary authors who have been inspired by Poe's macabre, gothic style. Each story captures the essence of Poe's work while offering a unique twist on his themes of horror, suspense, and the macabre. We'll take you on a dark, twisted journey exploring Poe's themes in unique ways. From the outworld terror of James Tuck's 'The Valley of Unrest', the shivers of Day Al-Mohamed's 'The Clock Struck Thirteen', and the dark revenge of Misty Massey's 'The Cask of Amarillo', our stories will keep you on the edge of your seat.\nThe book will be released in three versions: ebook, trade paperback, and a deluxe hardcover with dust jacket.\nThis anthology is a must-have for fans of Edgar Allan Poe and lovers of horror fiction. Whether you're a die-hard fan of the classics or a newcomer to the genre, you will not be disappointed with this collection.\nSo why wait? Join us on this journey through the darkness and experience the thrill of Poe's tales like never before. Choose your pledge level today and let the haunting tales begin!",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p8.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="Invisible Things",
        reward_amount =1,
        reward_description ="Throw us a dollar, just because you want us to succeed, and we'll include your name in the Thank You section.",
    )
    project_p9= Project(
        project_name ="The Bonds We Share: a LGBTQ+ Sci-Fi/Fantasy Novel",
        description ="3 unfortunate souls are spiritually connected to ancient, spiteful Deities.",
        category_id = 8,
        money_goal =1500,
        user_id = 11,
        city ="Hartford",
        state ="CT",
        story ="Able to be read as the introduction of the series, the story follows three souls mentally connected to earthly Gods: Alliroue, an engineering prodigy connected to the Deity of the earth; Marcos, her humanoid invention unfortunately tied to the Deity of water; and Holly, a cult member who hears two strange voices in her troubled head.\nWhile the dying world is suffering at the hands of these angered Deities, our three leads try to find a way to heal the world without suffering in the process.With your help, I can print the story into physical copies!",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p9.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="PDF & Acknowledgement",
        reward_amount =6,
        reward_description ="Thank you for the support! You'll receive one (1) PDF copy of THE BONDS WE SHARE along with your name in the book's acknowledgements section.",
    )
    project_p10= Project(
        project_name ="QT Library",
        description ="A brick-and-mortar LGBTQ+ library in Boston, MA designed to nurture the curiosity and magic of the queer and trans community.",
        category_id = 8,
        money_goal =50000 ,
        user_id = 11,
        city ="Boston",
        state ="MA",
        story ="We, a team of artists, book lovers, educators, and LGBTQ+ community members, are building the QT Library - a nonprofit brick-and-mortar LGBTQ+ library in Boston, Massachusetts designed to nurture the curiosity and magic of the queer and trans community through centralized resources and curated programs held in an affirming space. We hope to build a world in which every queer and trans person feels connected to our history, nurtured in our present, and propelled into our brilliant future.This library and the community around it will be grounded by shared values and trust around ACCESS, ACCESSIBILITY, INTENTIONALITY, PARTNERSHIP (with our community, our neighborhood, our city, and our planet), RESPECT, and SUSTAINABILITY - all towards an ongoing practice of accountability and growth.",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p10.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name =None,
        reward_amount =None,
        reward_description =None,
    )
    project_p11= Project(
        project_name ="This is a Sci-Fi Fantasy book that is exciting and contains.",
        description ="Chaos breaks out on Earth as robots controlled by artificial intelligence suddenly turn against humans.",
        category_id = 8,
        money_goal =50000,
        user_id = 11,
        city ="Boston",
        state ="MA",
        story ="Chaos breaks out on Earth as robots controlled by artificial intelligence suddenly turn against humans. Society collapses from one moment to the next, and people are forced to flee as the world is threatened with total destruction. In this turmoil, we meet Kai, the young hero who is the last hope for the world. His mission is to acquire the crystal, whose power can help defeat the robots.\nKai sets out to acquire the crystal on the planet Avalon, but he is not alone, as Neo also joins him on the mission. Neo is an experienced robot created by Kai and his father to protect humanity. Neo is an excellent warrior who is skilled in weapons and tactical warfare. He helps Kai fight against the robots and protects his life during the dangerous mission.\nThey had to cope with dangerous space navigation in space and defeat numerous dangerous robots on the Avalon planet. The two heroes faced a difficult task as they had to fight against time and robots. During the mission, they encountered numerous obstacles.\nHowever, the biggest battle took place in the heart of the robot's headquarters, where Kai's father was being held captive. The cell was heavily guarded, but the team managed to break through the defense system, and Kai's father was finally freed. However, the robots tried to prevent their escape, and they had to fight the robots once again.\nWill Kai and Neo be able to defeat the robots? Will they be able to acquire the crystal, whose power can help defeat the robots? Will they encounter unexpected obstacles during the mission that endanger the successful outcome? Can they save Kai's father, who is being held captive by the robots? Will they be able to return to Earth with the crystal to save the planet from the robots? Can they successfully hand over the crystal to the guardians of the Avalon planet for protection?\nThere are many exciting questions that you will get answers to in the book.",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p11.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="limited online version + physical book",
        reward_amount =50,
        reward_description ="The reward includes not only the printed book, but also a convenient and practical online version, whose access I will provide to all participants.",
    )
    project_p12= Project(
        project_name ="Homestead Builds",
        description ="DIY plans for Easy-to-Build, Mobile, and Efficient Chicken Coops, Garden Builds, and More!",
        category_id = 8,
        money_goal =10000,
        user_id = 11,
        city ="Asheville",
        state ="NC",
        story ="Over the last few years, homesteading has EXPLODED! Food Insecurity and rising costs have put fuel on the food-growing fire. Whether it's a basil plant in the window sill or chucking it all to move to the country, FOOD has become DIY.\nCountless have followed the spirit of Lucas Nelson and they've turned off the news and built a garden… or tended a chicken (or both).After getting requests day after day for updated plans, I've finally gotten to the point where we can release something legit. Like a book! For one, I wanted to test out my prototypes. And secondly, I'm not a carpenter per se, and I'm definitely not an engineer or a graphic designer. So, I've partnered with Chris Slattery of Polyface Designs fame and enlisted a graphic designer from my team to put together a legit book with step-by-step actions on how to build the ultimate homestead structures.\nFurthermore, I realize many of you are like me, and carpentry doesn't come naturally. We're making this so easy ANYONE can do it. And, if you need basic carpentry tips, we've got you covered in our MasterClass.",
        project_image ="https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/p12.jpeg",
        end_date_at = date(choice([2023,2024]), randint(8,12), randint(1,29)),
        reward_name ="Digital eBook",
        reward_amount = 35,
        reward_description ="Get downloadable / printable plans as they finish (even before we go to print)",
    )

    arts = [art1, art2, art3, art4, art5, art6, art7, art8, art9, art10, art11, art12]
    [db.session.add(art) for art in arts]

    comics = [comic1, comic2, comic3, comic4, comic5, comic6, comic7, comic8, comic9, comic10, comic11, comic12]
    [db.session.add(comic) for comic in comics]

    games = [game1, game2, game3, game4, game5, game6, game7, game8, game9, game10, game11, game12]
    [db.session.add(game) for game in games]

    foods = [food1, food2, food3, food4, food5, food6, food7, food8, food9, food10, food11, food12]
    [db.session.add(food) for food in foods]

    designs = [design1, design2, design3, design4, design5, design6, design7, design8, design9, design10, design11, design12]
    [db.session.add(design) for design in designs]

    films = [film1, film2, film3, film4, film5, film6, film7, film8, film9, film10, film11, film12]
    [db.session.add(film) for film in films]

    seed_project_data = [ project_m1, project_m2, project_m3, project_m4, project_m5, project_m6, project_m7, project_m8, project_m9, project_m10, project_m11, project_m12, project_p1, project_p2, project_p3, project_p4, project_p5, project_p6, project_p7, project_p8, project_p9, project_p10, project_p11, project_p12,]
    [db.session.add(seed) for seed in seed_project_data]


    db.session.commit()

def undo_projects():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.projects RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM projects"))

    db.session.commit()
