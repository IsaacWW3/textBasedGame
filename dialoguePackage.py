class dialogue:
    # The triple quotation isn't strictly comments, it recognizes as a string, but allows it to exist by itself

    '''
    Nodes is where you will store all the dialogue for the game
    It is a dict of dicts where the dict stores the dialogue options for certain scenes
    The dialogue scenes are dicts so the options can be stored with a descriptive key
    They would work just as well as a list, you just need to keep track of the indicies
    '''

    def __init__(self):
        self.nodes = {

            'tavern': {
                '1': node('Innkeeper: "Greetings! Glad to see you finally woke up!"',
                          ['You: "I am so confused"']),
                '2': node('Innkeeper:  "No worries my friend! Have a seat."',
                          ['You: "Okay,  I have a few questions..."']),
                '3': node('Innkeeper: "Feel free to ask my anything!"',
                          ['You: "Do you know how I got here?"',
                           'You: "Have you heard anything about the Demon Lord?"']),
                '3.1': node(
                    'Innkeeper: "You were found on the edge of the Elderwood Forest outsidede the village! a kind trader brought you here."',
                    ['You: "Have you heard anything about the Demon Lord?"']),
                '3.2': node(
                    'Innkeeper: "Ive heard rumors of the Demon Lords army making movement toward Frostfall, but nothing else."',
                    ['You: "Do you know where Frostfall is?"']),
                '3.2.1': node(
                    'Innkeeper: "Frostfall is a decent size town to the north, its actually the largest town in the area!"',
                    ['You: "Okay! Thanks for the info"']),
                '3.2.1.1': node('Innkeeper: "Safe travels friend!"', is_terminating_node=True)
            },
            'frostfall': {
                '1': node('Wizard: "Nice to meet you hero, my name is Kexus."',
                          ['You: "Uh... so what was that..."', 'You: "Nice to meet you!"']),
                '1.1': node('Kexus: "That was one of the Demon Lords generals, Dragorath."',
                            ['You: "Why did he attack Frostfall?"']),
                '1.1.1': node('Kexus: "The Demon Lord has recently been trying to expand his domain, sadly he went after Frostfall today"',
                              ['You: "I see... Where should we go from here?"']),
                '1.2': node('Kexus: "Are there any questions you have for me hero?"',
                            ['You: "Who was that?"', 'You: "Why did that guy attack Frostfall?"']),
                '1.1.1.1': node('Kexus: "Well hero, why are you here?"',
                                ['You: "Im here because I had a vision of a god (I think) who told me I was the chosen hero to fight the Demon lord']),
                '1.1.1.1.1': node('Kexus: "That was certainly... unexpected... hmm... come with me."', is_terminating_node=True)
            },
            'library':  {
                '1': node('Keuxs: "Any questions?"',
                          ['You: "You knew the hero Les?"', 'You: "Nope"']),
                '1.1': node('Kexus: "Yes I knew them... they were... such a kind soul"',
                            ['You: "I think Les was the god that I met!"', 'You: "What can you tell me about Les?"']),
                '1.1.1': node('Kexus: "You met Les? They must have been the one to tell you to defeat the Demon Lord.'
                              '\n This is very interesting, do you know how you communicated with them?"',
                              ['You: "No, I have no clue how or why I was able to talk to Les."',
                               'You: "I think I died in another world and was reincarnated into this one"']),
                '1.1.1.1': node('Kexus: "This is very perplexing, perhaps there is a way for you to communicate with them again"',
                                is_terminating_node=True),
                '1.2': node('Kexus: "Ah, I see, continue reading then"', is_terminating_node=True),
                '1.1.2': node('Kexus: "Les was a hero of humanity, kind of heart and a the sweets soul known to mankind.'
                              '\n I honestly miss him dearly, everyone does..."',
                              ['You: "The book also mentions Essie, what happened to her?"',
                               'You: "If I was able to talk to Les once, I should be able to again right?"']),
                '1.1.2.1': node('Kexus: "Essie was devestated after the loss of Less... she now wanders around as a drunkard"',
                                ['You: Thats kind of sad... do you think we could find her?"']),
                '1.1.2.1.1': node('Kexus: "Perhaps we could, and now that I think maybe you can communicate with Les again!',
                             is_terminating_node=True),
                '1.1.2.2': node('Kexus: "Yes you should! Follow me!"', is_terminating_node=True),
                '1.1.1.2': node('Kexus: "Another world? This wouldnt be the first time something like this happened..."',
                                ['You: "What do you mean?"']),
                '1.1.1.2.1': node('Kexus: "Never mind that, I think you might be able to communicate with Les again! Follow me!"',
                                  is_terminating_node=True)
            }
        }

        """
               This is the tree attrib of this class, it's just how the dialogue is organized in a tree
               It is broken up like nodes where 'tavern' refers to the dialogue scene
               Because it is declared after the nodes, we can use ".self" to get the nodes from the above
               So, "self.nodes['tavern']['1']" can be broken down to...
                   "self" -> this object
                   "nodes" -> access the nodes dict
                   "['tavern']" -> the dictionary at the 'tavern' key of the dictionary
                   "['1']" -> the string at the '1' key of the 'tavern' dictionary

               You can represent the tree as, well, a tree where the different options branch into other options.
               You could use this without nodes with a bit of modification, but nodes are also good because they
               store answers too. This is efficient because the dialogue is already in memory, so all you are doing 
               is pointing to the address rather than making a whole new object.
               """

        self.tree = {
            'tavern': crotch(self.nodes['tavern']['1'], {
                '1': crotch(self.nodes['tavern']['2'], {
                    '1': crotch(self.nodes['tavern']['3'], {
                        '1': crotch(self.nodes['tavern']['3.1'], {
                            '1': crotch(self.nodes['tavern']['3.2'], {
                                '1': crotch(self.nodes['tavern']['3.2.1'], {
                                    '1': crotch(self.nodes['tavern']['3.2.1.1'])
                                })
                            })
                        }),
                        '2': crotch(self.nodes['tavern']['3.2'], {
                            '1': crotch(self.nodes['tavern']['3.2.1'], {
                                '1': crotch(self.nodes['tavern']['3.2.1.1'])
                            })
                        })
                    })
                })
            }),
            'frostfall': crotch(self.nodes['frostfall']['1'], {
                '1': crotch(self.nodes['frostfall']['1.1'], {
                    '1': crotch(self.nodes['frostfall']['1.1.1'], {
                        '1': crotch(self.nodes['frostfall']['1.1.1.1'], {
                            '1': crotch(self.nodes['frostfall']['1.1.1.1.1'])
                        })
                    })
                }),
                '2': crotch(self.nodes['frostfall']['1.2'], {
                    '1': crotch(self.nodes['frostfall']['1.1'], {
                        '1': crotch(self.nodes['frostfall']['1.1.1'], {
                            '1': crotch(self.nodes['frostfall']['1.1.1.1'], {
                                '1': crotch(self.nodes['frostfall']['1.1.1.1.1'])
                            })
                        })
                    }),
                    '2': crotch(self.nodes['frostfall']['1.1.1'], {
                        '1': crotch(self.nodes['frostfall']['1.1.1.1'], {
                            '1': crotch(self.nodes['frostfall']['1.1.1.1.1'])
                        })
                    })
                })
            }),
            'library': crotch(self.nodes['library']['1'], {
                '1': crotch(self.nodes['library']['1.1'], {
                    '1': crotch(self.nodes['library']['1.1.1'], {
                        '1': crotch(self.nodes['library']['1.1.1.1']),
                        '2': crotch(self.nodes['library']['1.1.1.2'], {
                            '1': crotch(self.nodes['library']['1.1.1.2.1'])
                        })
                    }),
                    '2': crotch(self.nodes['library']['1.1.2'], {
                        '1': crotch(self.nodes['library']['1.1.2.1'], {
                            '1': crotch(self.nodes['library']['1.1.2.1.1'])
                        }),
                        '2': crotch(self.nodes['library']['1.1.2.2'])
                    })
                }),
                '2': crotch(self.nodes['library']['1.2'])
            })
        }

    def getTree(self, key):
        return self.tree[key]


'''
Nodes store the string question as an input, the other two are optional
is_terminating_node is a variable, setting it to true indicates it will end the tree and there are no more options
answers is a list of the possible answers the user can input
'''


class node:
    def __init__(self, question, answers: list = [], is_terminating_node: bool = False):
        self.question = question
        self.answers = answers
        self.is_terminating_node = is_terminating_node


"""
crotch, named after the part of the tree that multiple branches form from the trunk is
a class that takes the parentNode, the main node you are referencing and a dict,
branchNodes, that is optional because the parentNode could be a terminating node. The
branchNodes are the dialogue options that stem from the parent node.
"""


class crotch:
    def __init__(self, parentNode, branchNodes: dict = {}):
        self.pNode = parentNode
        self.bNodes = branchNodes

    # doPrint just prints the possible answers to the parentNode
    def doPrint(self):
        # print(self.question)
        i = 0
        for x in self.pNode.answers:
            print(str(i + 1) + ": " + self.pNode.answers[i])
            i = i + 1

    # callAnswer is a recursive function that loops through every node along the tree according to user input
    def callAnswer(self):
        repeat = True
        # Prints the node's question
        print(self.pNode.question)
        # Will do the try except loop as long as the input is false
        # it won't even attempt to run the loop if it is a terminating node because it terminates
        while repeat and not self.pNode.is_terminating_node:
            # The try statement allows for inputs that cause errors to just say "Please enter a valid input!"
            try:
                self.doPrint()
                user_input = input()
                self.bNodes[user_input].callAnswer()
                repeat = False
            except:
                print("Please enter a valid input!")


aDialogue = dialogue()
#  aDialogue.getTree('library').callAnswer()
