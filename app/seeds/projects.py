from datetime import date
from ..models import Project, db

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
