from datetime import date
from ..models import Project, db

food1 = Project(
    project_name = "Estate 98 Ultra-Concentrated Coffee: Make Coffee Your Way",
    description = "Use a few drops to create hot or iced coffee, lattes & more in seconds | Experience the richness of El Salvadors finest coffee beans.",
    category_id = 5,
    money_goal = 10000,
    user_id = 8,
    city = "Miami",
    state = "FL",
    story = "Estate 98 coffee beans have been cultivated on volcanic soil and picked by hand for six generations in the lush mountains of El Salvador. We are proud to introduce our 10x ultra-concentrated coffee, which offers the most exquisite flavor and quality. Now you can experience the full potential of your creativity by adding just a few drops of our premium liquid ultra-concentrated coffee to your favorite drink! At Estate 98, our 100 percent strictly high-grown Arabica coffee (Bourbon varietal) is picked individually by hand and dried on patios; honoring the age-old processing method for the most exquisite coffee flavor and quality.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_1_coffeeconcentrate.png",
    end_date = date(2024, 6, 23),
    reward_name = "Super Early Bird | Estate 98 4-pack",
    reward_amount = 72,
    reward_description = "Back this reward for four (4) bottles of Estate 98. Perfect for those who travel, a family of coffee drinkers and those who feel like gifting something great."
)

food2 = Project(
    project_name = "Curbside to Dine-In: Help Buddy's Chicken & Waffles Expand!",
    description = "After almost two years of operating in ghost kitchens, we are ready to open our flagship location right here in Tacoma!",
    category_id = 5,
    money_goal = 40000,
    user_id = 9,
    city = "Tacoma",
    state = "WA",
    story = "When I made the move from Baltimore to Tacoma in January 2020, I had no clue where life would take me. Little did I know that a pandemic would spark the idea for Buddy's—a small coffee shop serving fried chicken and variety of waffles. As someone who always had a passion for cooking but lacked confidence, I honestly thought the waffles would be the star of the show. Shockingly, the fried chicken recipe that I developed after years of watching Mommie & Grandma in the kitchen is what got Buddys featured on the evening news. Now, we need your help to make this dream a reality. With this Kickstarter campaign, we aim to establish Buddys Chicken & Waffles as the go-to destination for incredible chicken and waffles in the entire state of Washington. Your support will enable us to secure the new space, equip the kitchen, and create an unforgettable dining experience that honors Uncle Thurms' 16-year legacy.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_2_chicken_waffles.png",
    end_date = date(2023, 11, 10),
    reward_name = "Chicken & Waffles and a Sticker!",
    reward_amount = 25,
    reward_description = "Try any one of our 9 different waffles with our famous fried chicken AND get a shiny new sticker!"
)

food3 = Project(
    project_name = "Frankly Delicious - Mini Chocolate Bars",
    description = "Chocolate made from ethically and sustainably sourced cocoa and other ingredients, but small.",
    category_id = 5,
    money_goal = 2500,
    user_id = 8,
    city = "Leeds",
    state = "WA",
    story = "Frankly Delicious is a group of artisan chocolate makers who make chocolate from scratch using ethically sourced cocoa. Unfortunately, most chocolate is made from cocoa that has been grown by farmers who earn less than $2 a day and often rely on illegal child labour. All of the cocoa we use to make our chocolate is grown by cocoa farmers who earn a fair price for their crop and because of this can hire qualified workers when needed. Right now we sell 10 different chocolate bars, with new, limited edition flavoured being added each month, and they are 60g bars. As well as using ethically sourced cocoa, all of our ingredients and flavourings are fully natural. From locally roasted coffee in our coffee white chocolate bar to freeze dried fruits in bars like our raspberry white chocolate alternative and blackcurrant dark chocolate bars.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_3_frankly_chocolate_bars.png",
    end_date = date(2024, 3, 12),
    reward_name = "4 Bars - Vegan - Most Popular",
    reward_amount = 19,
    reward_description = "1x Madagascar 70 percent dark chocolate bar, 1x Oat m!lk chocolate bar, 1x Coconut m!lk chocolate bar, 1x Raspberry white chocolate alternative bar"
)

food4 = Project(
    project_name = "The Sourdough Framework",
    description = "Master the art of sourdough baking at home with this comprehensive guide, covering science, basics, and advanced techniques.",
    category_id = 5,
    money_goal = 14500,
    user_id = 9,
    city = "Hamburg",
    state = "NY",
    story = "Gluten Tag. I'm a German software engineer and passionate bread nerd.  My mission is to democratise baking by enabling everyone around the world to bake delicious bread at home. Right now when you follow online recipes to bake bread (and even more so sourdough) you will likely fail. The flour is different, you use different yeast strains and you work with different temperatures. For this reason I have started The Bread Code - a YouTube channel that dives deeper into bread making at looks at the science and why behind the process. By understanding what's happening in the background I enable you to bake delicious bread at home in your environment.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_4_sourdough.jpeg",
    end_date = date(2023, 10, 2),
    reward_name = "Physical book and sourdough infographic",
    reward_amount = 70,
    reward_description = "You'll receive the physical version of the book and a handy poster of a sourdough info graphic that assists you with daily tasks in the kitchen."
)

food5 = Project(
    project_name = "Grazed Snax: A pastured based snack line.",
    description = "We are regenerative farmers launching a snack line. Starting with an original pork stick made from 100% pasture-raised pork, sugar free.",
    category_id = 5,
    money_goal = 29000,
    user_id = 8,
    city = "Durham",
    state = "NC",
    story = "In 2019 the farm started in our front yard with chickens. Withing 18 months we raised over 6,000 broilers and 100 hogs and finished 40 head of cattle. All our livestock rotates from pasture to pasture daily. Rotation spreads livestock fertility, minimizing fertilization needs and allowing for vegetation recovery. Each paddock is occupied less than half of the time. Keeping nutrients on-farm helps reduce the need for outside inputs. We want to expand Grass Grazed to make nutrient dense products accessible to consumers nationwide.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_5_grazed_snax.jpeg",
    end_date = date(2023, 11, 10),
    reward_name = "Sticks + MERCH",
    reward_amount = 50,
    reward_description = "8 Original Pork Sticks + Farm T-shirt"
)

food6 = Project(
    project_name = "Homefire Tea & Botanicals - Pour A Cup Of Comfort",
    description = "Tea blends and medicinals that will bless you down to your bones.",
    category_id = 5,
    money_goal = 1500,
    user_id = 9,
    city = "Janesville",
    state = "WI",
    story = "Homefire Tea & Botanicals is a dream shared by two people who really love tea, plants, and taking care of folks. Combined we have over 30 years of experience studying, interacting with, and recommending plants for the benefit of the human experience. When they were asked for recommendations to help people deal with their problems or find a moment of quiet enjoyment, two things came up over and over: Tea and tinctures. Our initial blends have been perfected in small batches and are ready to debut.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_6_tea_botanicals.png",
    end_date = date(2023, 12, 5),
    reward_name = "Simple Sample",
    reward_amount = 10,
    reward_description = "4 samples of your choice of blends (each makes about 3 cups)."
)

food7 = Project(
    project_name = "Help Us Publish The Flavor Seed Organic Seasonal Cookbook",
    description = "Follow our chef inspired, mother approved cookbook to create simple organic meals within 30 minutes.",
    category_id = 5,
    money_goal = 5000,
    user_id = 8,
    city = "Charlotte",
    state = "NC",
    story = "Our goal is to help families and individuals eat a non-processed food diet; quickly, easily deliciously, and organically. Our Organic blended seasonings do just that and while our flavors work great by just getting them on whatever you are cooking our fans kept asking for recipes. Not being a huge recipe guy, I sought out professional help. That's when fate and fortune aligned and Johnson & Wales University agreed to partner with Flavor Seed to not only help create this cookbook, but to help teach an entrepreneurship class and expose their students to real world small business challenges. Our team won the President's Award for most professional and rewarding experience.  While we did not complete the entire Flavor Seed Organic cookbook, we did produce the Summer edition of Flavor Seed recipes. Our Summer Cookbook (magazine) is also available as a digital download ebook.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_7_seed_cookbook.png",
    end_date = date(2023, 11, 15),
    reward_name = "Printed Summer Cookbook (magazine)",
    reward_amount = 15,
    reward_description = "Get a printed version of the smaller organic summer recipe cookbook. This printed magazine-like copy will contain recipes for the summer and is a shorter version of the overall cookbook. This is a composition of the work produced this spring semester by the Johnson and Wales students. The full version of the cookbook will contain additional summer recipes as well as the remainder seasons. This is just a starter version."
)

food8 = Project(
    project_name = "Ghost Bagel Food Truck",
    description = "Ghost Bagel of Napa, California is buying a food truck!",
    category_id = 5,
    money_goal = 60000,
    user_id = 9,
    city = "Napa",
    state = "CA",
    story = "I grew up in New York state, eating bagels nearly every weekend from my town's multiple bagel shops.  After moving to Napa, I realized that a fresh bagel was one of the few things that we couldn't find here, so I started making them myself and got pretty good.  I decided to start a little bagel business and see where it went.  After a few years of delivering a few dozen bagels per day, last year, my friend joined me and we were able to multiply the number of bagels we make.  We started doing markets and popups and Ghost started growing. To keep the momentum, we are hoping to take steps to expand our production and our distribution.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_8_ghost_bagel.png",
    end_date = date(2023, 11, 20),
    reward_name = "A dozen bagels!",
    reward_amount = 50,
    reward_description = "Get one dozen bagels whenever you'd like! (This reward is claimed at our food truck once it is open.)"
)

food9 = Project(
    project_name = "Reyna Filipina Kitchen TACOMA",
    description = "Where Brunch Flavors of the Philippines Reign Supreme",
    category_id = 5,
    money_goal = 71000,
    user_id = 8,
    city = "Tacoma",
    state = "WA",
    story = "Over the past five years, I have been sharing my love for Filipino food with the Tacoma community, and the response has been overwhelming. We have successfully operated a farmers market stand, offering fresh and distinct Filipino cuisine. Now, we am ready to take it to the next level and reach a wider audience by launching a new restaurant here in Tacoma. This restaurant, Reyna Filipina Kitchen TACOMA, which means queen in Filipino, is a tribute to my mother, Lucy, and other women who have inspired and supported me throughout my journey. We will be offering all-day brunch.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_9_filipino_restaurant.jpeg",
    end_date = date(2024, 1, 2),
    reward_name = "Thank You Note From Chef Jan",
    reward_amount = 20,
    reward_description = "A heartfelt, handwritten Salamat: Thank you note from Chef Jan"
)

food10 = Project(
    project_name = "milk & mochi — an Asian American bakery in Seattle, WA",
    description = "Sister-owned pop up is opening a brick-and-mortar bakery in Fremont!",
    category_id = 5,
    money_goal = 50000,
    user_id = 8,
    city = "Seattle",
    state = "WA",
    story = "We started as a pop up in June 2022 with a little idea but a big love of food. We're Vietnamese American: born in Vietnam, raised in Southern California, and settled in Seattle. Our bakery is an expression of the in-between experience of being both Asian and American. We create desserts that are a bit Asian and a bit Western, with a unique mix of the two that represents who we are, and our name reflects that: milk (Western) & mochi (Asian)! We make desserts that hit the sweet spot in the middle: punchy flavors, not too sweet (the ultimate Asian compliment), and airy enough to feel light, but rich enough to feel a bit decadent.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_10_milk_mochi_bakery.png",
    end_date = date(2023, 12, 10),
    reward_name = "Cream puff reservation",
    reward_amount = 20,
    reward_description = "Two cream puffs just for you! Backers will get access to make a reservation on the day of your choice (up to six months after opening). There will be a limited number of reservations per day."
)

food11 = Project(
    project_name = "Herders to Home 2023: Luxury Mongolian Yarn and Fiber",
    description = "Herders to Home, ULA+LIA procures fibers from free-range Mongolian animals to create world-class knitting yarn",
    category_id = 5,
    money_goal = 27500,
    user_id = 9,
    city = "Honolulu",
    state = "HI",
    story = "We've made it though winter in Mongolia and after a trip to see the herders providing our fiber for this season, I'm once again coming to the Kickstarter community to raise funds to reach our batch requirements and bring our beautiful Mongolian yarn and fiber to the rest of the world! Now as official partners of of the yak wool and two cashmere cooperatives we source our fibers from, I can't wait to visit them during the campaign to share our progres",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_11_mongolian_yarn.jpeg",
    end_date = date(2023, 11, 28),
    reward_name = "Mongolian Wool/Cashmere Blend Yarn 200g",
    reward_amount = 30,
    reward_description = "With select sourcing through our cooperative partners for the soft, Sartuul sheep wool and expert processing, we are able to provide an incredibly soft and durable fiber that offers great value next to its more rare fiber relatives. Adding a 15 percent blend of our cashmere, the final products pick up some of the beautiful hand and loft that our cashmere is known for."
)

food12 = Project(
    project_name = "ALIVE - The World's First Shower Bomb For Your Morning",
    description = "ALIVE is the strongest shower bomb taken to market. An intense blend of essential oils and menthol to energize, decongest and focus.",
    category_id = 5,
    money_goal = 5600,
    user_id = 8,
    city = "Columbus",
    state = "OH",
    story = "The new ALIVE formula lasts longer and hits harder than ever before! Our new prototype bombs last around 15 minutes in the shower. Kick brain fog to the curb. Power through your day with clarity and focus. Peppermint has been shown to improve cognitive performance and alertness, strong menthol allows you to breather, and eucalyptus and pepperming are commonly known to increase dopamine.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/food_12_shower_bomb.jpeg",
    end_date = date(2023, 11, 30),
    reward_name = "Kickstarter Special - 1 Pack of ALIVE",
    reward_amount = 27,
    reward_description = "Our new ALIVE Shower Bomb - Hits harder and last longer. The only way to wake up and hit the ground running, without having to change your daily routine."
)

game1 = Project(
    project_name = "The Medusa Report",
    description = "A thrilling tabletop puzzle adventure about a missing spy, a nuclear physicist and Cold War family secrets.",
    category_id = 6,
    money_goal = 12000,
    user_id = 8,
    city = "Juneau",
    state = "AK",
    story = "The Medusa Report is a tabletop puzzle game. A treasure trove of touch-real, confidential items from a Cold War infiltration mission. By yourself, or as a team of up to 4 players, you'll investigate a mysterious agency, uncover what really happened near Nikitagrad in 1974 and above all: find out where Abigail Vandermist is hiding! The game is entirely analog. Solve puzzles, study a tactical map, decode classified letters, unravel the secrets of an old floppy disk... (don’t worry, you won’t need a floppy drive). With each deciphered message, you'll uncover more of the story and find new clues for the next puzzle. No rule sheet. No time limit. No envelopes saying 'Don't open me until you've solved X.' Every puzzle has a narrative justification and everything you need is right there, if you figure out how to look.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_1_medusa_report.png",
    end_date = date(2023, 11, 3),
    reward_name = "THE DOUBLY SPECIAL AGENT",
    reward_amount = 100,
    reward_description = "One personalized PREMIUM copy of THE MEDUSA REPORT, plus one copy of THE VANDERMIST DOSSIER. Includes Vandermist enamel pin. Kickstarter exclusive."
)

game2 = Project(
    project_name = "Soulmist : Unspoken Tales",
    description = "A book of dark and unforgiving adventures inside the heart of Erebos, for 5e.",
    category_id = 6,
    money_goal = 15000,
    user_id = 9,
    city = "Albany",
    state = "NY",
    story = "Journey inside the Darklands, where the Light never shines, and fight hordes of darkspawns, demons, and unfathomable abominations. This is a set of two adventures, taking place in the world of the Soulmist campaign setting, but that can be played in any regular 5e campaign without any issue. Our biggest priority is to deliver you the best quality products we can achieve. In order to accomplish that we have set up a network of talented individuals and companies to troubleshoot any obstacle in the road to delivering on our project.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_2_soulmist.png",
    end_date = date(2024, 1, 10),
    reward_name = "Prince of Dusk",
    reward_amount = 80,
    reward_description = "Get the full collection of Soulmist titles, in both their Hardcover and Digital versions. Included are both GM's screens featuring artwork from Soulmist and Darklands, the map of Fyera and a set of maps of all its major cities, the collector's slip case, the dice set and the spell cards. *Shipping charged after the campaign"
)

game3 = Project(
    project_name = "Pathfinder: Abomination Vaults - Hack & Slash ARPG",
    description = "The first-ever co-op Hack and Slash ARPG, based on the renowned Pathfinder Roleplaying Game! Set to release on PC (Steam).",
    category_id = 6,
    money_goal = 410000,
    user_id = 8,
    city = "Milwaukee",
    state = "WI",
    story = "The first-ever Co-op Hack and Slash ARPG based on the renowned Pathfinder Roleplaying Game! Pathfinder: Abomination Vaults is a classic Co-op Hack and Slash game, based on the epic Adventure Path of the same name, in which up to four players lead iconic Pathfinder heroes into the farthest depths of Gauntlight Keep, battle deadly monsters and abominations to reach the evil sorceress Belcorra Haruvex and put an end to her vile schemes once and for all. Genre: Online & Local Co-op/Offline Solo Hack and Slash, Action RPG, Dungeon Crawler game Platform: PC (Steam)",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_3_pathfinder_abomination.jpeg",
    end_date = date(2023, 11, 30),
    reward_name = "Digital Download",
    reward_amount = 40,
    reward_description = "Unlocks the Deluxe role in our Discord server, a digital download of our game Pathfinder: Abomination Vaults, and your name in the credits! Includes digital download of Pathfinder: Abomination Vaults game and exclusive wallpaper backgrounds for desktop and mobile."
)

game4 = Project(
    project_name = "Asteroid Dice: The giant throw & collide squishy dice game!",
    description = "Throw, bounce and collide giant foam dice in this chaotic, cosmic game! These squishy dice are also great for RPGs, DnD & Giant Gaming.",
    category_id = 6,
    money_goal = 7800,
    user_id = 9,
    city = "Boston",
    state = "MA",
    story = "The giant roll, throw and collide dice game! Grab your asteroid die from the middle, but be prepared to face-off against your opponent snowball-fight style! Once the moon dust has settled, roll and crash the dice together to get your score up, and hopefully get your opponents score down. With giant squishy foam dice this game is as tactile as it is fun. You will need strategy, speed and skill to come out on top. The Kickstarter Edition, Fireball Expansion Edition and all of the Kickstarter artwork is limited and exclusive to this campaign only. They will not be available outside of Kickstarter. We are also offering an exclusive Shape Invaders Bundle (a sneak preview into our next game) including an Alpha of an App!",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_4_asteroid_dice.png",
    end_date = date(2023, 12, 12),
    reward_name = "Astronaut",
    reward_amount = 5,
    reward_description = "Help support our Kickstarter, get access to the pledge manager, and get 7 awesome pieces of space-art as phone backgrounds from our talented collaborating artist: Khairul Anam!"
)

game5 = Project(
    project_name = "French Quarter: A let the good times roll and write game!",
    description = "Welcome to the heart of New Orleans! Explore the French Quarter in this new loaded roll and write game.",
    category_id = 6,
    money_goal = 18000,
    user_id = 8,
    city = "Detroit",
    state = "MI",
    story = "In French Quarter,  you are in town for a weekend trip with plans to spend your Saturday evening taking in as many of the citys unique sights and sounds as you possibly can in a mere eight hours. Whether it’s the distinct food, local culture, shopping hotspots, mystic customs, or vibrant nightlife, there’s something to experience on practically every corner. There is live jazz everywhere you go, and NOLA is world-famous for its street performers. Make sure you do not miss the spontaneous wedding parades, known locally as second lines, that roll through the streets!",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_5_french_quarter.png",
    end_date = date(2023, 11, 22),
    reward_name = "French Quarter - Kickstarter Edition",
    reward_amount = 29,
    reward_description = "INCLUDES: French Quarter - Kickstarter Edition, All Achieved Stretch Goals, Kickstarter Bonus Content, A hearty thank you!"
)

game6 = Project(
    project_name = "Penumbra City",
    description = "A ttrpg set in the mysterious world of Harrow.",
    category_id = 6,
    money_goal = 13000,
    user_id = 9,
    city = "Tucson",
    state = "AZ",
    story = "Penumbra City is a rules-medium, campaign-world-rich tabletop roleplaying game designed for 3-6 players. It is already 80% written and is playable, we just need your help to finish the last round of playtesting and get it printed and into your hands. Penumbra City is a class-based game with simplified core mechanics but a broad range of character class abilities. Healing is hard to come by, so the decision to fight must never be taken lightly. While one player takes the role of the Game Master, players roll all dice. Most rolls are made with d20s. Penumbra City uses a reputation economy; it is a world where money has lost its luster, and it is a characters reputation with the various gangs, factions, and coalitions that determine their access to resources.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_6_penumbra.png",
    end_date = date(2024, 1, 18),
    reward_name = "Digital Edition",
    reward_amount = 15,
    reward_description = "This tier includes downloadable digital editions (PDF) of Penumbra City, our Zine Bundle, and our Class Character Sheets"
)

game7 = Project(
    project_name = "The Wagadu Chronicles - Afrofantasy MMO for role-play",
    description = "An Afrofantasy world to explore both as an isometric MMO built for in-character roleplay and as a 5E-compatible tabletop setting!",
    category_id = 6,
    money_goal = 100000,
    user_id = 8,
    city = "Madison",
    state = "WI",
    story = "We believe that role-playing isn't always just about about grinding and growing stats. It's the embodying of a role; the presence of a backstory and all of the quirks and details that define your unique character. Many of us have experienced old-school role-play around a table with pencils and a bunch of dice. We know how immersive it is to speak like our characters and to be surrounded by other players who are making decisions based on their characters profiles. Role-play truly submerses you in another world, more powerfully than any NPC  quest could. Imagine a videogame where everyone around you is role-playing. The noble Emere with whom you are travelling does not want to desecrate any tombs and ignores the loot; the Swala hunter you just met chants a ritual prayer before every hunt and the Asiman merchant never attacks or kills anyone because she believes her goddess wants peace to rule in Wagadu.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_7_wagadu.jpg",
    end_date = date(2023, 11, 1),
    reward_name = "Afrofantasy Lore Bundle",
    reward_amount = 55,
    reward_description = "INCLUDES: 🎮 Digital Edition of The Wagadu Chronicles MMO 📂 The 7th Era Setting 5E Rulebook (PDF) 📂 Guide to Afrofantasy Roleplay (PDF) 📂 The Art of Wagadu (PDF) 🗝 Access to MMO closed Beta - Sixth Era 💎 Golden Sun Spear (In-Game Item) 🔶 Name in Credits 🔷 Discord Role"
)

game8 = Project(
    project_name = "Command of Nature",
    description = "An immersive, deck-building tabletop game from the creators of Here to Slay and Casting Shadows",
    category_id = 6,
    money_goal = 50000,
    user_id = 9,
    city = "St. Louis",
    state = "MO",
    story = "Harness the magic of the forest and go head-to-head with your rivals in this strategic deck-building game for 2 or 4 players. You will play as a powerful Sage, summoning warriors from the Twig, Leaf, Droplet, and Pebble factions and fighting to prove your prowess. As the battle continues, you will level up and gain access to extraordinary abilities and fierce new recruits. Protect your Sage at all costs and vanquish your opponents to earn the title of Master of the Elements! As part of this project, we created exclusive and collectible items that you won't get anywhere else as a thank you for supporting us on Kickstarter. These items will not be available online or in retail stores at a later date.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_8_command_of_nature.jpg",
    end_date = date(2023, 12, 24),
    reward_name = "Kickstarter Exclusive Edition Game",
    reward_amount = 39,
    reward_description = "INCLUDES: Command of Nature: Kickstarter Exclusive Edition Game"
)

game9 = Project(
    project_name = "Flickade",
    description = "Experience an exciting and engaging game for those who enjoy flicking objects with precision and strategy.",
    category_id = 6,
    money_goal = 1200,
    user_id = 8,
    city = "Kimberly",
    state = "ID",
    story = "Introducing Flickade, my second-ever game creation and first venture on Kickstarter. This thrilling flicking game challenges your precision and strategic skills. I've meticulously designed every ship piece in Blender and brought them to life with 3D printing. Even the extensively refined case design is 3D printed. It not only screws on perfectly but also boasts an aesthetically pleasing appearance. Each set comes with a sticker on the bottom, featuring a condensed version of the rules, and an additional sticker with answers to common questions that you can place wherever you like. Master the game within just 5 minutes and immerse yourself in hours of fun. Flickade includes 20 ships (10 per player) with 4 small speedboats, 10 medium destroyers, and 6 large aircraft carriers, all 3D printed out of PLA. PLA is a type of plastic that doesn't rely on petroleum and is mainly corn starch or sugar cane. This environmentally conscious choice ensures that our game is both fun and eco-friendly. Each round lasts approximately 15 to 30 minutes, making it perfect for quick matches or extended gaming sessions. The game is designed primarily for two players, but Flickade can be easily adapted for multiple participants with additional sets. Flickade is recommended for ages 4 and up, making it an ideal choice for family game nights. We offer a vibrant selection of eight distinct colors, paired to create four dynamic color combinations for your Flickade sets: Red/Blue, Gray/Orange, White/Magenta, and Brown/Green. Each set's container comes in a sleek black finish by default but can be customized upon request.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_9_flickade.jpg",
    end_date = date(2023, 11, 10),
    reward_name = "Flickade: 2-Player Set",
    reward_amount = 30,
    reward_description = "Flickade full set and a big thank you!"
)

game10 = Project(
    project_name = "Slothtopia - A reimagined life simulator game for PC/Switch",
    description = "A charming life simulator game where you can fish, farm, build relationships, and even catch and train monsters",
    category_id = 6,
    money_goal = 5000,
    user_id = 9,
    city = "Huntington Beach",
    state = "CA",
    story = "Slothtopia: A family-friendly charming life simulator game where you can fish, farm, build relationships, and even catch monsters as an adorable, hard working sloth. Catch fish at sea, come home and pick fresh herbs from the garden, and make a meal for your friends. Build friendships and romance with other villagers. Catch local monsters and train them to help you with tasks around the island. These are just a few of the things to do on the magical island of Slothtopia! Catching island monsters can be difficult. Hone your skills by picking magical fruits and hiding in the tall grass until you spot one. Once caught you will be required to provide for your monster. You can pet, feed, and train your monster to level up your relationship and it's abilities. Unlike some other popular monster catching games, we do not battle our monsters. We use them much more like service animals. They are excellent companions, but also serve a distinct purpose. You must train them to utilize their special skills. Once trained, you can send your monster on tasks like catching fish, farming, and even romancing that special someone.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_10_slothtopia.jpg",
    end_date = date(2023, 12, 1),
    reward_name = "Alpha Access Bundle: Slothtopia",
    reward_amount = 40,
    reward_description = "Get access to Slothtopia in it's earliest stages for testing. In addition get your name in credits and an exclusive hang-glider skin."
)

game11 = Project(
    project_name = "Pelican Playing Cards",
    description = "Elegant playing cards printed by USPCC, tuck box printed by Gambler's Warehouse",
    category_id = 6,
    money_goal = 10000,
    user_id = 8,
    city = "Las Vegas",
    state = "NV",
    story = "Hey, I'm a magician and Guinness World Record card thrower from Lithuania. Over the past decade, I've traveled the world performing magic in theaters, on cruise ships, and at corporate events. I'm extremely excited for this debute in the world of PLAYING CARDS! Ive had a passion for playing cards since I started practicing magic at 12 years old. Everywhere I went I would always look for new or interesting decks. I would even have my friends and family bring them back from their trips. Ever since, the dream of creating MY OWN DECK OF PLAYING CARDS has always been in the back of my mind. I never felt ready or confident enough to create something unique, but eventually I realized that I would never be ready. I needed to trust the process and start. Now, after spending two years on this project, I am thrilled to be one step away from releasing my very first deck, which I have named... drum roll... PELICAN! Now I am excited to invite you to be a part of bringing these cards to life! But why Pelican? First of all, it sounds really cool! Just say it out loud with me: 'Pelican Playing Cards'! I bet you want to say it again, don't you? BUT there's also a deeper meaning behind the name! Pelicans can hunt in groups, yet they also spend time alone. I believe that life is all about balance - being alone, being in a group - and you can help others when youre at peace with yourself.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_11_pelican_cards.jpg",
    end_date = date(2023, 11, 20),
    reward_name = "1 Pelican Deck",
    reward_amount = 19,
    reward_description = "100 percent custom playing cards."
)

game12 = Project(
    project_name = "SLAV BORG - A Post-Soviet Semi-Fantasy RPG",
    description = "Rev the engines with your goblin crew, steal some sweet new orc wheels and put the brakes on the Eastern Bloc’s slimiest necromancer.",
    category_id = 6,
    money_goal = 8035,
    user_id = 8,
    city = "Philadelphia",
    state = "PA",
    story = "In SLAV BORG, cunning, speed, and covertness reign supreme. You will traverse the borderland with your goblin crew, outmaneuver orcs in illegal (and fixed) street races, and try to put the brakes on the sleaziest necromancer this side of the Eastern Bloc. SLAV BORG is a stand-alone game that’s also compatible with MORK BORK and other OSRs. And you know what this means: tons of new tables, monsters, NPCs, and various additional components you can use to craft a playstyle and narrative that best suit your greedy spirit. The game can be played in three different modes. SLAV BORG’s main RPG campaign will throw you right in the middle of the Realm of Zgol, where you will try to carve out your own skid by leveling your crew, upgrading your vehicles, and burning rubber across multiple story chapters. The stakes, along with the players' death count, escalate even further in SLAV BORG's second play mode: one-shot adventures. Finally, theres the roguelike mode, where each run is randomized with new locations, events, and scenarios. Using the classic framework of sword and sorcery, we are telling our SLAV BORG tales against the real-world backdrop of the social and economic struggles of the Polish-German-Czech borderland. This way, we want to craft a fantasy world that mirrors the reality that shaped us, with one of Europes biggest coal mines on one side, and rampant crime and lawlessness on the other. Welcome to the Realm of Zgol.",
    project_image = "https://kickstarterclonebucket.s3.us-west-1.amazonaws.com/game_12_slav_borg.jpg",
    end_date = date(2023, 9, 25),
    reward_name = "NECROMANCER [PRINTED DELUXE + DIGITAL]",
    reward_amount = 70,
    reward_description = "INCLUDES: Hardcover book. Character sheet notebook. Paper miniatures (if unlocked). Modular cardboard Gurlitz racetrack/dungeon (if unlocked). Printed poster with map and dungeon. Digital book [PDF]. Digital poster with a dungeon. Digital character sheet. Digital map. Digital coloring book"
)
