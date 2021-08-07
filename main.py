import random
import time

game_is_on = True

# credit for spell, potion, and magical substance names goes to https://www.fantasynamegenerators.com
class Items:
    def __init__(self, name):
        self.name = name
        self.books = {'names and info': {
            'Information on Dark lord book': """Historical background:\nThe dark lord was an orphan who sought power so he could fight back against those that ruthlessly bullied him. He learned forbidden spells and eventually started recruiting an army to further extend his powers. Anyone who stood in his way was annihilated as a threat to his ambitions. Now, he haunts the entire magical world and threatens to overthrow the government.\nBattle tactics: Before attacking, the Great lord closely studies his enemy until they know or at least predict their next move. Then he strategically organizes his large force so that his strongholds are fortefied but he also has a tactical advantage over his enemy. Then, he strikes.\nGoals for the future: Now, he wants to overthrow the existing government and establish his own rule.\n""",
            'Learning About Magical Creatures book': """Pixies: pixies are aerial creatures that are known to be deceptive. They often use their magical powders to confuse their enemies, making them distracted and drowsy.\nGoblins: Short creatures with dark brown skin and fur covering their entire body. Their natural habitat is underground and they are known to steal shiny possessions from humans.\nTrolls: Tall creatures standing at roughly 8-10 feet tall. They have green fur, a pale face, and tend to be quite muscular. Their naturally quite violent and have often been blamed for leaving great destruction behind them.\n""",
            'Battle strategies book': """Defense:\nBoxing strategy - a tactic in which the enemy is surrounded on all sides. This tactic is effective because it secures your victory since the enemy is not given the opportunity to retreat.\nDefense in depth-to delay the advance of the attackers by buying time and causing additional casualties by yielding space so that the enemy's momentum of the attack is lost.\nOffense:\nAttrition warefare- A strategy of wearing down the enemy to the point of collapse through continuous loss of personnel and material. Used to defeat enemies with low resources and high morale.\nBlitzkrieg – the attacking force, spearheaded by a dense concentration of armoured and motorised or mechanised infantry formations with close air support, breaks through the opponent's line of defence by short, fast, powerful attacks and then dislocates the defenders.""",
            'Sorcery introduction book': """Relegris:melts the enemy into slime.\nMeda:shatters the victim into pieces.\nPetrifis:vaporizes the victim into thin air.\nImmorulsis:sends the victim upwards, through the ceiling.\nAugendo:sets the victim on a devestating fire that sometimes also destroys the surroundings.\nObliula:breaks the victim into pieces.\n""",
            'Sorcery intermediate book': """Vengeuno Miseriato:throws the enemy backwards at 50 mph.\nSeveriate Aviello:burns the enemy in a fire that is very hard to extinguish.\nTranqiteus Intimaro:turns the enemy into mud.\nExterminectus Horrifiatis:disintegrates the enemy into dust.\nDelerortia Tremendempra:buries the enemy deep underground.\n""",
            'Magical Mythology book': """Some believe that there are magical creatures like witches, wizards, goblins, pixies, and even trolls living among us. Many accounts have come to light in the past few years but most have been disregarded and those who shared such accounts were labeled as dellusional. However, the reoccurance of such accounts with similiar descriptions raises the question whether such creatures are real and have been somewhere this entire time.""",
            'Potions Guide book': """Potion of Distractions:\nIngredients: primal bone, stained log, aquatweed\nUses:The potion of distractions is used to make the drinker hallucinagenic. It is often thrown at opponents at battle or snuck into drinks in order to get an advantage against the opponent who will not longer be able to make clear decisions.\nPotion of Immobilizing:\nIngredients: dark zinc, phoenix lace, half dust\nThe potion of immobilizing is used to paralyze the drinker. It is often thrown at opponents during battle or snuck into drinks to get an advantage over the opponent who will be left vulnerable to attacks after being exposed to this liquid.\nTonic of Empowerment:\nIngredients: warped nickel, nimble wool, abyssmarble, exhausted copper\nUses: This tonic is used to increase the speed, decisions making capabilities, and magical prowess of the drinker. It is also known to heighten the senses of the drinker, allowing them to hear, smell, and see things from a distance. It is often used before battle to give the drinker an advantage over their opponent in battle since they will make better moves and their attacks will have greater power than before.""",
            'Magical Substances book': """Primal Denim: burns the eyes of goblins.\nWicked Glass: lethal to pixies\nPowderlead: freezes trolls\nGloomsteel: freezes humans\nEnigmatitanium: blows apart goblins\nElectric Bark: instantly burns humans\nTranquil Bone:pushes goblins underground\nLone Nickel: enought to permanently immobilize goblins."""},

            'knowledge points': {
                'Information on Dark lord book': 60,
                'Learning About Magical Creatures book': 30,
                'Battle strategies book': 50,
                'Sorcery introduction book': 80,
                'Sorcery intermediate book': 90,
                'Magical Mythology book': 60,
                'Potions Guide book': 80,
                'Magical Substances book': 90
            }}

        self.spells = {'damage': {
            'r': 10,
            'm': 20,
            'p': 15,
            'a': 12,
            'o': 30,
            'v': 20,
            's': 30,
            't': 25,
            'e': 40,
            'd': 35
        }, 'tries': {
            'r': 2,
            'm': 3,
            'p': 2,
            'a': 2,
            'o': 4,
            'v': 3,
            's': 4,
            't': 3,
            'e': 5,
            'd': 5
        }, 'spells learned': []}

        self.spells_quiz = {
            'Question 1 - Which spell is effective against pixies?\na- Vengeuno Miseriato b-Exterminectus Horrifiatis c-Augendo d-Petrifis Immorulsis': 'd',
            'Question 2 - Which spell is effective against humans?\na- Delerortia Tremendempra b-Obliula c-Augendo d-Tranqiteus Intimaro': 'b',
            'Question 3 - Which spell is effective against trolls?\na- Delerortia Tremendempra b-Exterminectus Horrifiatis c-Tranqiteus Intimaro d-Meda': 'c',
            'Question 4 - Which spell is effective against goblins?\na- Meda b-Exterminectus Horrifiatis c-Obliula d- Vengeuno Miseriato': 'a',
            'Question 5 - Name one spell that is effective against pixies, humans, goblins, and trolls in that order\na-Severiate Aviello, Obliula, Augendo, Exterminectus Horrifiatis b-Relegris, Delerortia Tremendempra, Vengeuno Miseriato, Tranqiteus Intimaro, Meda\nc-Severiate Aviello, Exterminectus Horrifiatis, Delerortia Tremendempra, and Augendo  d-Petrifis Immorulsis, Vengeuno Miseriato, Obliula, Delerortia Tremendempra, Relegris': 'c'
        }

        self.potions_quiz = {
            'Question 1 - What is an ingredient found in the Tonic of Empowerment? a- pheonix lace b-wraped nickel c-primal bone d- dark zinc': 'b',
            'Question 2 - What is an ingredient found in the Potion of Distractions? a-nimble wool b-dark zinc c-exhausted copper d- aquatweed': 'd',
            'Question 3 - What is an ingredient found in the Potion of Immobilizing? a-stained log b-nimble wool c-half dust d-abyssmarble': 'c',
            'Question 4 - What is the Potion of Immobilizing used for? a- It is used in battle to paralyze the opponent b- It is poured into beverages to disable the drinkers c- both a and b': 'c',
            'Question 5 - What is an advantage of using the potion of distractions? a- It makes the opponent vulnerable to attack since they cannot focus on the enemy b- It physically harms the opponent who becomes paralyzed after drinking the potion. c-It gives the opponent super strength and speed, giving them an advantage in battle.': 'a',
            'Question 6 - What is the difference between the potion of distractions and the potion of empowerment? a-the potion of empowerment is used for offense, the potion of immobilizing is used for defense b- the potion of empowerment is used for defense, the potion of immobilizing is used for offense.': 'b',
            'Question 7 - What magical substances are effective against humans? a-powederlead, lone nickel b-primal denim, tranquil bone c-powderlead, enigmatitanium d-gloomsteel, electric bark': 'd',
            'Question 8 - What magical substances are effecitve against goblins? a-gloomsteel, lone nickel b- wicked glas, electric bark c- primal denim, tranquil bone d-enigmatitanium, powederlead': 'c',
            'Question 9 - What magical substances are effective against pixies? a-wicked glass, lone nickel b-powderlead, primal denim c-gloomsteel, enigmatitanium d- tranquil bone, wicked glass': 'a',
            'Question 10 - What magical susbtances are effective against trolls? a-tranquil bone, enigmatitanium b- enigmatitanium, powderlead c- powderlead, wicked glass d-primal denim, lone nickel': 'b'
        }
        self.potion_making = {'recipe': {
            'potion of distractions': '1- add three cut pieces of nimble wool 2- set the temp to 350 degress 3-add dark zinc 4- stir the potion clockwise three times 5-crush the exhausted copper and add it to the potion. 6- change the temp to 230 degrees 7- let it sit for 2 hours.',
            'potion of immobilizing': '1- add dark zinc 2- temp the solution up to 200 degrees 3- stir the solution 5 times counterclockwise 4-add cut pieces of pheonix lace. 5- add half dust 6- let the potion sit for 1 hours.',
            'tonic of empowerment': '1- add cut pieces of warped_nickel to the cauldron. 2- turn up the temp to 275 degrees 3- add abyssmarble. 4- stir the solution clockwise 4 times. 5- let the solution sit for 1 hour. 6- add cut pieces of nimble wool to the solution. 7- add exhausted copper 8- stir the solution 2 times counterclockwise and then once clockwise.'
        }, 'correct steps': {
            'potion of distractions': ['cut nimble wool', 'add cutted nimble wool', 'set temp to 350', 'add dark zinc',
                                       'stir 3 clockwise', 'crush exhausted copper', 'add crushed exhausted copper',
                                       'set temp to 230', 'wait 2'],
            'potion of immobilizing': ['add dark zinc', 'set temp to 200', 'stir 5 counterclockwise',
                                       'cut pheonix lace', 'add cutted pheonix lace', 'add half dust', 'wait 1'],
            'tonic of empowerment': ['cut warped nickel', 'add cutted warped nickel', 'set temp to 275',
                                     'add abyssmarble', 'stir 4 clockwise', 'wait 1', 'cut nimble wool',
                                     'add cutted nimble wool', 'add exhausted copper', 'stir 2 counterclockwise',
                                     'stir 1 clockwise']
        }}

        self.potions = {
            'potion of distractions': ['primal bone', 'stained log', 'aquatweed'],
            'potion of immobilizing': ['dark zinc', 'phoenix lace', 'half dust'],
            'tonic of empowerment': ['warped nickel', 'nimble wool', 'abyssmarble', 'exhausted copper']
        }
        self.next_potion = True

    def map(self):
        if self.name == 'map':
            print('You can travel to the following destinations: ')
            for path in current_room.routes:
                print(path.name)
        player1.items_used.append(self.name)

    def binoculars(self):
        print(
            'You pick up your binoculars and look out the window. Outside, you see two sets of pink eyes staring back at you. Upon closer examination, you see these creatures have a set of small, grey wings, green hair, and pale skin though the rest of their features are quite like humans. They appeared to be the height of children and were both quite slim. You stand back astonished at what you are seeing. ')
        player1.items_used.append(self.name)

    def decide_potion(self):
        while len(player1.potions_made) < 3 and self.next_potion:
            if len(player1.potions_made) >= 1:
                print(f"Potions Guide book:\n{self.books['names and info']['Potions Guide book']}")
            global build_potion
            build_potion = input('Enter the name of the potion you want to make: ').lower()
            while build_potion not in self.potions.keys():
                print('invalid input. Try again')
                build_potion = input('Enter the name of the potion you want to make: ').lower()
            print('Ingredients you need to collect from the forest- ')
            global items
            items = self.potions[build_potion]
            for item in items:
                print(item)
            self.next_potion = False
        ask_user_input()

    def book(self):
        if self.name == 'Sorcery Introduction book':
            player1.items_not_allowed.remove('Sorcery intermediate book')
        elif self.name == 'Sorcery Intermediate book':
            if 'training dummies' not in player1.items_used:
                print(
                    'You must practice the skills you learned in Sorcery Introduction book before reading about more advanced spells.')
                return
            else:
                player1.items_not_allowed.remove('telephone')
        for book_name in self.books['names and info'].keys():
            if book_name.lower() == self.name.lower():
                print(f"Contents of the book:\n{self.books['names and info'][book_name]}")
        for book_name in self.books['knowledge points'].keys():
            if book_name.lower() == self.name.lower():
                player1.knowledge += self.books['knowledge points'][book_name]
                print(f'Knowledge points: {player1.knowledge}')
        player1.items_used.append(self.name)
        if self.name == 'Potions Guide book':
            self.decide_potion()

    def func_potions_quiz(self):
        global potion_tries
        potion_tries = 0
        num_correct = 0
        redo = True
        while redo:
            potion_tries += 1
            print(
                "Now it's time to test your knowledge of potions. Read over the information below and take the quiz. You can redo the quiz until you get a score of 80% or higher.")
            print(
                f"Potions Guide book:\n{self.books['names and info']['Potions Guide book']}\n Magical Substances book:\n{self.books['names and info']['Magical Substances book']}")
            for question in self.potions_quiz.keys():
                print(question)
                user_answer = input('guess answer: ')
                correct_answer = self.potions_quiz[question]
                if user_answer == correct_answer:
                    print('correct')
                    num_correct += 1
                else:
                    while user_answer != correct_answer:
                        print('wrong. Try again')
                        user_answer = input('guess answer: ')
            print(f'Congratulations, you got {num_correct}/{len(self.potions_quiz.keys())}')
            if num_correct < 4:
                print('Since you did not get a score of 80% or higher, you will take the quiz again.')
                num_correct = 0
            else:
                redo = False
        player1.calibrate()

    def potions_cooker(self):
        global build_potion

        if 'Potions Guide book' not in player1.items_used:
            print('First read Potions Guide book to learn how to make potions.')
        elif 'Potions Guide book' in player1.items_used and build_potion and not all(
                item in player1.inventory for item in self.potions[build_potion.lower()]):
            print(
                f'First retrieve the ingredients you need to make the potion from the forest before using the potion cooker\nIngredients needed- {self.potions[build_potion]}')
        else:
            user_steps = []
            redo = True
            while redo:
                player1.potion_attempts += 1
                print(
                    f'Potion being made: {build_potion}\nYou took an empty cauldron and wooden stirring spoon from the cupboard and set it on the table. Now start adding ingredients to the cauldron in the order dictated below. You will also have to change the temperature, slice ingredients at the right time, and stir the solution in order to successfully make this potion so stay attentive!')
                print(
                    "use the keyword 'add <ingredient>' to add an ingredient to your cauldron. Use 'cut <ingredient>' or 'crush <ingredient>' to split up an ingredient "
                    "in a certain manner before adding it to the couldern. Use 'set temp to <temperature>' to change the temperature of the potion. Uset 'wait <time> to "
                    "set the cauldron aside for some time. Do not type enter units for temperature or time! Finally, Use 'stir <num_times> <direction>' to stir the solution."
                    "For example, if the instructions ask you to cut up pheonix lace, first type 'cut pheonix lace'. Then, on the next command, type 'add cutted pheonix lace'. Similiarly, "
                    "'smash <item>' translates to 'add smashed <item>' on the next line. Lastly, if you are asked to set the potion aside for 1 hour, type 'wait 1' since time trainslates to "
                    "wait <time period without units>.")
                recipe = self.potion_making['recipe'][build_potion]
                print(f'{build_potion} recipe:\n{recipe}')
                incorrect_steps = 0
                while len(user_steps) < len(self.potion_making['correct steps'][build_potion]):
                    step = input('next step: ')
                    words = step.split(' ')
                    keyword = words[0]
                    ingredient = ' '.join(words[1:])
                    if step.lower() not in self.potion_making['correct steps'][build_potion]:
                        print('Incorrect step. Try again')
                        incorrect_steps += 1
                    else:
                        if keyword == 'cut':
                            ingredient = 'cutted ' + ingredient
                            player1.inventory.append(ingredient)
                        elif keyword == 'crush':
                            ingredient = 'crushed ' + ingredient
                            player1.inventory.append(ingredient)
                        elif keyword == 'add' and ingredient in player1.inventory:
                            player1.inventory.remove(ingredient)
                        elif keyword == 'wait':
                            time_set = int(ingredient.split(' ')[-1])
                            time.sleep(time_set * 5)
                        user_steps.append(step)
                if incorrect_steps > 2:
                    print(
                        'Oh no, your potion did not turn out as expected since you made too many mistakes. Please try again.')
                    user_steps = []
                    incorrect_steps = 0
                else:
                    print(f'Congratulations, you successfully made a {build_potion}!')
                    player1.potions_made.append(build_potion)
                    redo = False
                    if len(player1.potions_made) == 1:
                        self.next_potion = False
                        potions_knowledge = len(self.potion_making['correct steps'][build_potion]) - incorrect_steps
                        player1.knowledge += potions_knowledge
                        player1.strength += potions_knowledge / 1.5
                        self.func_potions_quiz()
                    else:
                        self.next_potion = True
                        self.decide_potion()

    def training_dummies(self):
        if self.name == 'training dummies':
            if player1.health != 100:
                print('Please go to the clinic first and heal before continuing your training.')
                return
            else:
                response = ['You missed the dummy by a few inches. Try to aim for the center!',
                            'Your spell hit the dummy but missed the target zones outlining vulnerable areas. Try to aim for those zones!',
                            'Oooh that was so close! Read over the incantation instructions in the book and try again.']
                if 'Sorcery Introduction book' not in player1.items_used:
                    print('You first have to read the Sorcery Introduction book before practicing the spells.')
                    return
                if 'training dummies' not in player1.items_used:
                    print(
                        'You acquired a wand to use during the training session. You can also keep this wand for personal use by adding it to your inventory.')
                    while len(self.spells['spells learned']) < 5:
                        print(
                            "Sorcery guide:\n'r':Relegris:\n'm': Meda:\n'p': Petrifis Immorulsis:\n'a': Augendo:\n'o': Obliula:\n")
                        print('Your opponents are the training dummies. Do your worst!')
                        spell = input('cast a spell: ')
                        if spell == 'r':
                            for i in range(self.spells['tries']['r']):
                                print('Relegris!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and turned it into slime. It fell backwards in defeat.')
                            self.spells['spells learned'].append('r')
                            player1.health -= 10
                        elif spell == 'm':
                            for i in range(self.spells['tries']['m']):
                                print('Meda!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and shattered it place. It fell backwards in defeat.')
                            self.spells['spells learned'].append('m')
                            player1.health -= 15
                        elif spell == 'p':
                            for i in range(self.spells['tries']['p']):
                                print('Petrifis Immorulsis!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and sends them upwards, through the ceiling. It fell backwards in defeat.')
                            self.spells['spells learned'].append('p')
                            player1.health -= 10
                        elif spell == 'a':
                            for i in range(self.spells['tries']['a']):
                                print('Augendo!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and set it on fire. It fell backwards in defeat.')
                            self.spells['spells learned'].append('a')
                            player1.health -= 20
                        elif spell == 'o':
                            for i in range(self.spells['tries']['o']):
                                print('Obliula!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and broke it into pieces. It fell backwards in defeat.')
                            self.spells['spells learned'].append('o')
                            player1.health -= 15
                        else:
                            print('invalid input')
                            spell = input('cast a spell: ')
                        print('You brought a new dummy from the cupboard and positioned it in place.')
                        player1.strength += self.spells['tries'][spell] * 10
                        print(f'Current strength: {player1.strength}')
                        print(f'Current health: {player1.health}')

                    if player1.health < 30:
                        print(
                            f'Oh no, your health has declined to {player1.health} from all this intense training. Please go to the clinic to heal before continuing to train.')
                if 'Sorcery Intermediate book' in player1.items_used and 'training dummies' in player1.items_used:
                    while len(self.spells['spells learned']) < 10:
                        print(
                            "Sorcery guide:\n'v':Vengeuno Miseriato\n's': Severiate Aviello\n't': Tranqiteus Intimaro\n'e': Exterminectus Horrifiatis\n'd':Delerortia Tremendempra")
                        print('Your opponents are the training dummies. Do your worst!')
                        spell = input('cast a spell: ')
                        if spell == 'v':
                            for i in range(self.spells['tries']['v']):
                                print('Vengeuno Miseriato!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and flew backwards. It fell backwards in defeat.')
                            self.spells['spells learned'].append('v')
                            player1.health -= 20
                        elif spell == 's':
                            for i in range(self.spells['tries']['s']):
                                print('Severiate Aviello!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and it was caught in a strong fire. It fell backwards in defeat.')
                            self.spells['spells learned'].append('s')
                            player1.health -= 10
                        elif spell == 't':
                            for i in range(self.spells['tries']['t']):
                                print('Tranqiteus Intimaro!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and it was dissolved into mud. It fell backwards in defeat.')
                            self.spells['spells learned'].append('t')
                            player1.health -= 20
                        elif spell == 'e':
                            for i in range(self.spells['tries']['e']):
                                print('Exterminectus Horrifiatis!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and it was dissinegrated into dust. It fell backwards in defeat.')
                            self.spells['spells learned'].append('e')
                            player1.health -= 25
                        elif spell == 'd':
                            for i in range(self.spells['tries']['d']):
                                print('Delerortia Tremendempra!')
                                print(random.choice(response))
                                spell = input('cast a spell: ')
                            print(
                                'You got it! You hit the dummy within a target zone and was buried underground. It fell backwards in defeat.')
                            self.spells['spells learned'].append('d')
                            player1.health -= 25
                        else:
                            print('invalid input')
                            spell = input('cast a spell: ')
                        print('You brought a new dummy from the cupboard and positioned it in place.')
                        player1.strength += self.spells['tries'][spell] * 10
                        print(f'Current strength: {player1.strength}')
                        print(f'Current health: {player1.health}')
                    if player1.health < 30:
                        print(
                            f'Oh no, your health has declined to {player1.health} from all this intense training. Please go to the clinic to heal before continuing to train.')
        player1.items_used.append(self.name)

    def telephone(self):
        num_correct = 0
        global spells_tries
        spells_tries = 0
        redo = True
        while redo:
            spells_tries += 1
            print(
                "Now that you have learned the basics of sorcery, witch Nunnez has come to personally give you some advice as you prepare to go up against the Great Lord's army")
            print(
                "Here are the tips witch Nunnez gives you-\nThe spells Vengeuno Miseriato, Delerortia Tremendempra, and Meda are most effective against goblins.\nSeveriate Aviello, Relegris, and Petrifis Immorulsis are most effective against pixies.\nTranqiteus Intimaro and Augendo is most effective against trolls.\nExterminectus Horrifiatis and Obliula is most effective against humans\nNow she will test your knowledge with a brief quiz. You can redo this quiz until you get a score of 80% or higher so you are prepared for the battles to come.")
            for question in self.spells_quiz.keys():
                print(question)
                user_answer = input('guess answer: ')
                correct_answer = self.spells_quiz[question]
                if user_answer == correct_answer:
                    print('correct')
                    num_correct += 1
                else:
                    while user_answer != correct_answer:
                        print('wrong. Try again')
                        user_answer = input('guess answer: ')
            print(f'Congratulations, you got {num_correct}/{len(self.spells_quiz.keys())}')
            if num_correct >= 4:
                redo = False
                for spell in self.spells['tries'].keys():
                    player1.strength += self.spells['tries'][spell] * 10
                return
            else:
                print('Since you did not get a score of 80% or higher, you will take the quiz again.')
                num_correct = 0
        player1.items_used.append(self.name)


class Player:
    def __init__(self, name, inventory=[], health=100, strength=0, knowledge=0):
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = []
        self.knowledge = knowledge
        self.items_used = []
        self.items_not_allowed = ['Sorcery intermediate book', 'telephone']
        self.potions_made = []
        self.potion_attempts = 0

    def calibrate(self):
        global game_is_on
        spells_tries = 1
        print(f'Player knowledge: {self.knowledge}')
        print(f'Player strength: {round(self.strength)}')
        print(f'Number of tries taken for sorcery quiz: {spells_tries}')
        print(f'Number of attempts needed to make 3 potions: {self.potion_attempts}')
        print(f'Number of tries taken for potions quiz: {potion_tries}')
        if self.knowledge > 300 and self.strength > 350 and spells_tries <= 3 and potion_tries <= 3 and self.potion_attempts <= 6:
            print(
                'You have acquired a sufficient amount of knowledge and strength to be a true sorcerer. You are ready to face villians like the Great lord and 
                'bring peace to the magical world. Congratulations, you win!')
        else:
            print(
                'Sorry, you were unable to acquire a sufficient amount of knowledge and strength to become a sorcerer. You are not ready to face the 
                'likes of evil wizards like the Great lord. Sorry, you lose.')
        game_is_on = False
        return


player1 = Player('Amy')

class Room:
    global current_room

    def __init__(self, name=None, description=None, items=None, routes=None):
        self.name = name
        self.description = description
        self.items = items
        self.routes = routes

    def pick(self, item):
        if item not in current_room.items:
            print('invalid input')
        elif item.name in player1.items_not_allowed:
            print('You must complete a step mentioned previously before you are allowed to proceed to the next level.')
        else:
            current_room.items.remove(item)
            print(f'{item.name} added to inventory')
            player1.inventory.append(item.name)
            print(f'Current inventory: {player1.inventory}')

    def go_to(self, place):
        global current_room
        item_found = False
        for room in current_room.routes:
            if place in room.name:
                print(f'You have travelled to {place}')
                current_room = room
                item_found = True
                break
        if not item_found:
            print('invalid input')

    def use(self, item):
        pass


bedroom = Room()
magic_land = Room()
sorcery_room = Room()
forest = Room()
clinic = Room()
potions_room = Room()

sys_map = Items('map')
binoculars = Items('binoculars')
magical_mythology_book = Items('Magical Mythology book')
information_on_dark_lord_book = Items('Information on Dark Lord book')
magical_creatures_book = Items('Learning About Magical Creatures book')
battle_strategies_book = Items('Battle Strategies book')
sorcery_introduction_book = Items('Sorcery Introduction book')
sorcery_intermediate_book = Items('Sorcery Intermediate book')
training_dummies = Items('training dummies')
telephone = Items('telephone')
wand = Items('wand')
potions_guide_book = Items('Potions Guide book')
magical_substances_book = Items('Magical Substances book')
potions_cooker = Items('Potions Cooker')
primal_bone = Items('primal bone')
stained_log = Items('stained log')
aquatweed = Items('aquatweed')
dark_zinc = Items('dark zinc')
phoenix_lace = Items('phoenix lace')
half_dust = Items('half dust')
warped_nickel = Items('warped nickel')
nimble_wool = Items('nimble wool')
abyssmarble = Items('abyssmarble')
exhausted_copper = Items('exhausted copper')

rooms = [bedroom, magic_land, sorcery_room, potions_room, forest, clinic]
items_ls = [sys_map, binoculars, magical_mythology_book, information_on_dark_lord_book, magical_creatures_book,
            battle_strategies_book, sorcery_introduction_book,
            sorcery_intermediate_book, training_dummies, telephone, wand, potions_guide_book, magical_substances_book,
            potions_cooker, primal_bone, stained_log, aquatweed, dark_zinc, phoenix_lace, half_dust, warped_nickel,
            nimble_wool, abyssmarble, exhausted_copper]
bedroom.name = 'bedroom'
bedroom.description = "You are lying in bed on night, unable to fall asleep. You feel uneasy and an unexplicable sense of dread as if something was coming. You reassure yourself that you are getting worked up for no reason and eventually fall asleep. You wake up to the sound of glass shattering. You open your window to see two pink eyes looking down upon you. You turn on the light and see two pixies before you. They say that you possess magical prowess. They want you to come with them to learn how to harness your abilities, by teaching you sorcery and potion making. In return, they expect you to help them take down evil villans like the Great Lord that have been terrorizing their land. Will you go to magic land with these pixies?"
bedroom.items = [binoculars, magical_mythology_book]
bedroom.routes = [magic_land]

magic_land.name = 'magic land'
magic_land.description = "You are greeted by many magical creatures like humans, pixies, hobbits, trolls, and goblins. All these creatures have assembled in Dumbley's training camp to prepare for battle. The elders tell you that an evil wizard called Timur Lark or 'The Great Lord' is trying to overthrow the current government and establish a tyranny. He is very evil and will try to wipe out entire species like pixies and goblins while brutally oppressing others. You must train in sorcery and potions in order to prepare for the worst!"
magic_land.items = [sys_map, information_on_dark_lord_book, magical_creatures_book, battle_strategies_book]
magic_land.routes = [sorcery_room, potions_room, clinic, forest]  # potions_room, combat_training_room]

sorcery_room.name = 'sorcery room'
sorcery_room.description = "In the sorcery room, you can read books on sorcery to learn about new spells and practice them on training dummies. Once you have learned all you can from the books, you can also contact a sorcerer to learn more advanced spellwork and battle techniques against the Great Lord."
sorcery_room.items = [sys_map, wand, sorcery_introduction_book, sorcery_intermediate_book, training_dummies, telephone]
sorcery_room.routes = [clinic, magic_land, potions_room, forest]  # [potions_room, combat_training_room, dungeons]

clinic.name = 'clinic'
clinic.description = "In the clinic, the medics will heal you back to full health. Please wait a few seconds as the medics batch up your bruises..."
clinic.items = [sys_map]
clinic.routes = [sorcery_room, magic_land, potions_room, forest]  # [potions_room, combat_training_room, dungeons]

potions_room.name = 'potions room'
potions_room.description = "In the potions room, you can learn how potions are made and what they are used for. First, read about potions and magical substances in the given books. Then, collect the necessary materials to conjure the potions from the forest. Come back to this room once you are done collecting materials and make the potions. Then, collect any herbs or powders you want in your inventory."
potions_room.items = [sys_map, potions_guide_book, magical_substances_book, potions_cooker]
potions_room.routes = [forest, sorcery_room, clinic, magic_land]  # [potions_room, combat_training_room, dungeons]

forest.name = 'forest'
forest.description = f"In the forest, you can collect the ingredients needed to make potions. To collect an ingredient, add it to your inventory. Then go back to the potions room to use these ingredients."
forest.items = [sys_map, primal_bone, stained_log, aquatweed, dark_zinc, phoenix_lace, half_dust, warped_nickel,
                nimble_wool, abyssmarble, exhausted_copper]
forest.routes = [potions_room, sorcery_room, clinic, magic_land]  # [potions_room, combat_training_room, dungeons]
if 'Potions Guide book' in player1.items_used:
    print(f"Here are the ingredients you need for your potion - {items}")
current_room = bedroom


def check_answer(input_msg):
    global game_is_on
    global current_room

    if 'help' in input_msg:
        print("Welcome to the magical trainer game. During this game, you will learn how to cast spells and make potions through guided practice. You will also learn how to use these powers to fight magical creatures like pixies, goblins, and trolls.\n To look at the items and paths avaliable in the room, type 'look'. You can add items you see in the room to your inventory by typing 'take <item_name>'. Any item you add to your inventory, you can be used throughout the game from that point on. You can access the inventory at any point by typing 'inventory'. You can also use items in the room by typing 'use <item_name>' in the console. Each time you use a item, a different output will be displayed and you must follow the instructions given to complete the game. The paths are what rooms you can visit from a given room. To go to a room, type 'go to <room_name>' in the console. If you need these help instructions again, type 'help' in the console.")
    elif 'look' in input_msg:
        print(f'Current room: {current_room.name}')
        print(current_room.description, '\n')
        print('The following items are found in the room: ')
        for item in current_room.items:
            if current_room.name.lower() == 'forest':
                print(item.name, end=' ')
            else:
                print(item.name)

        print(f'\nFrom here you can go to:')
        for path in current_room.routes:
            print(path.name)
        if current_room == clinic:
            if player1.health == 100:
                print('Your already have a full health. Please come back after doing some training.')
            else:
                time.sleep(5)
                player1.health = 100
    elif 'inventory' in input_msg:
        print(player1.inventory)
    elif 'take' in input_msg:
        words = input_msg.split(' ')
        item = ' '.join(words[1:]).lower()
        for i in items_ls:
            if i.name.lower() == item:
                item = i
        current_room.pick(item)
        print('Items avaliable in the room-')
        for item in current_room.items:
            if current_room.name.lower() == 'forest':
                print(item.name, end=' ')
            else:
                print(item.name)
        print('\n')
    elif 'go to' in input_msg:
        words = input_msg.split(' ')
        place = ' '.join(words[2:])
        current_room.go_to(place)
    elif 'use' in input_msg:
        words = input_msg.split(' ')
        thing = ' '.join(words[1:])
        item_found = False
        for i in items_ls:
            if i.name.lower() == thing.lower() and i.name not in player1.items_not_allowed:
                if i.name.lower() == 'map':
                    i.map()
                elif i.name.lower() == 'binoculars':
                    i.binoculars()
                elif 'book' in i.name.lower():
                    i.book()
                elif i.name.lower() == 'training dummies':
                    i.training_dummies()
                elif i.name.lower() == 'telephone':
                    i.telephone()
                elif i.name.lower() == 'wand':
                    print('item already in use')
                elif i.name.lower() == 'potions cooker':
                    i.potions_cooker()
                item_found = True
                break
            elif i.name.lower() == thing.lower() and i.name in player1.items_not_allowed:
                print(
                    'You must complete Sorcery Introduction book, Sorcery Intermediate book, and telephone in that order. After each step, you can practice the spells you learned using the training dummies before moving onto the next step.')
        if not item_found:
            print('item not found')
    elif 'end' in input_msg:
        print('Thank you for playing!')
        game_is_on = False
    elif 'pause' in input_msg:
        print('Game paused')
        game_is_on = False
    else:
        print('Invalid input')


def ask_user_input():
    while game_is_on:
        user_input = input('what do you want to do: ')
        check_answer(user_input)


def start():
    print("Magical Training Game\nType 'help' in the console to get started.")
    name = input('Enter your name: ')
    print(f'Hello {name}')
    ask_user_input()


start()





