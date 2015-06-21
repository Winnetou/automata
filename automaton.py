#!/usr/bin/env python
'''
# Cellular automata and their simple ontology:
# cellular automaton has a certain state and a range of possible state
# in trivial cases, range has just one value and possible states have just one valiue
# two possible states give us discerete automata
# automata should be also allow for fully continuous linear change of its state - this has to be implemented 
# cellular automaton has n number of appendages which defines the number of factual interactions with other automata in a given moment
# interaction with another automaton can change the state of automaton 
# cellular automaton has responsiveness factor. that defines scale of reaction to interaction. 
# interaction itself has no property: it merely reflects the state of automaton. 

'''


'''
Very important thing to consider now ::::
you would want to be able to control how they join with their appendages
for that reason 
you can have a property on population class that will set the rules for joining:
shall it join close neighbours only?
it matters because it will mean that all actions will be local
in population A B C D E F G H I
A is connected with B and C
B with C and D
that means that A influences B, B influences C and C influences A.
So it is a question of how much connections overlap

'''

from random import choice #as choice

#class Abstract_Automaton():
#    """ Defines Automaton. """

#some helpers
'''
def give_range(state_range):
    """ Take one, two or three ints
    and return range(first, second, third)
    """ 
    if len(state_range) == 0:
        return [1]
    if len(state_range)==1:
        return range(state_range[0],state_range[0]+2)
    elif len(state_range)==2:
        return range(state_range[0], state_range[1])
    elif len(state_range)>2:
        return range(state_range[0], state_range[1], state_range[2])
    
'''

class Automaton():
    """ 
    Defines Automaton.
    Ultimate goal is to have a generator function
    to create a population of automata
    defined not by number of appendages of every single automaton
    but by n-hands-shake rule. 
    Eg.: give population of 10000 automata obeying 5-hands-shake rule.
    Number of appendages every automaton has will be thus dependent of n-hands-shake rule.
    Properties defined here:
    :prop state_range
    state 
    initial_state
    responsiveness
    appendages - initially, a list of zeros, as class: Population if initialized, it makes automata join

    Methods defined here:

    """
    def __init__(self, state_range=[0,1], initial_state=None, responsiveness=1, appendages=1):
        
        #state_range - automaton can be in discrete or linear state. 
        #state_range is expected to be a list or a tuple of two ints for discrete automata 
        #
        if not isinstance(state_range, (list, tuple)) or not all(isinstance(w, int) for w in state_range):
            raise ValueError("state_range must be a list or a tuple of two or three integers")
        # we dont want to have (0,0) as state_range or any such shit
        if len(state_range) < 2:
            raise ValueError("state_range must contain at least two ints")
        self.state_range = state_range

        if not initial_state: # if it was None, pick random value from state_range
            initial_state = choice(state_range)

        if initial_state not in state_range: # 
            raise ValueError("Initial state not in range of possible states")
     
        self.state = initial_state


        if not isinstance(responsiveness, (int, float)):
            raise ValueError("Responsiveness must be int or float instance")
        
        self.responsiveness = responsiveness

        if isinstance(appendages, int):  
            self.appendages = [0 for x in range(0, appendages)]
        else:
            raise ValueError("Appendages: int expected, got rotten cabbage instead")
    
    def __str__(self):
        return "Automaton number "+str(id(self)) 
        #pass

    def __repr__(self):
        return self.__str__()

    def change_state(self, neighbour_state):
        """ Takes state of another automaton
        computes the response 
        by taking responsiveness factor """
        
        print self.state
        differance = self.state - neighbour_state
        print differance
        change = differance * self.responsiveness
        print change

        if self.state == neighbour_state:
            pass # TODO
        # neighbour has higher state, we change up
        elif self.state < neighbour_state: # 
            if self.state + change <= max(self.state_range):
                self.state += change
                print self.state
            else:
                self.state = max(self.state_range)
        # neighbour has lower state, we change down
        elif self.state > neighbour_state: 
            if self.state - change >= min(self.state_range):
                self.state -= change
                print self.state
            else:
                self.state = min(self.state_range)



        


class Population():
    """ Defines a population of automata.
    Population is a list of Automaton instances.
    If every automaton is to be fully defined
    you can create empty population and join one by one
    Else, you can let function create_population() do the job

    On init, it ascribes neighbours to every member
    by replacing zeros in appendages
    with id of the object
    that defines a link between two automata
    
    Now, the question is how to distribute automata:
    let us say that we want to check population of
    uniformly distributed automata
    or you want to cluster them
    or spread them or Juno knows what
    """
    def __init__(self):
        self.population = []
    


    def join_cohort(self, number, state_range, initial_state, responsiveness, appendages):
        ''' Method for creating a set of n automata with defined properties
        and joining them to the population'''
        if number<1 or not isinstance(number, int):
            raise TypeError("number must be int higher than 0")
        for x in range(0, number+1):
            new_automaton = Automaton(state_range, initial_state, responsiveness, appendages)
            self.population.append(new_automaton)
    

    def create_social_bonds(self, distribution="local"):
        '''For existing population, we join appendages'''
        if distribution == "local":    
            for automaton in self.population:
                #  if it has still some appendages available
                for appendage in [a for a in automaton.appendages if a == 0 ]:
                    if  [anth for anth in self.population if not anth is automaton\
                                                                        and 0 in anth.appendages\
                                                                        and not id(automaton) in anth.appendages ]:#
                        # find the first auttomaton different from itself and having one free appendage
                        other_automaton = next(aut for aut in self.population\
                                                                if not aut is automaton\
                                                                and 0 in aut.appendages\
                                                                and not id(automaton) in anth.appendages)  #iterate over automata in population, this will be most likely creating local bonds
                        first_zero = automaton.appendages.index(0)# for readability
                        automaton.appendages[first_zero] = id(other_automaton)#take first occurence of 0 and replace it with ID
                        # now we make this relation relfexive
                        second_first_zero = other_automaton.appendages[other_automaton.appendages.index(0)]
                        other_automaton.appendages[second_first_zero] = id(automaton)

        
        if distribution == "random":
            for automaton in self.population:
                for appendage in [a for a in automaton.appendages if a == 0 ]:#
                    if  [anth for anth in self.population if not anth is automaton\
                                                                        and 0 in anth.appendages\
                                                                        and not id(automaton) in anth.appendages ]:#
                        other_automaton = choice([anth for anth in self.population\
                                                                if not anth is automaton\
                                                                and 0 in anth.appendages\
                                                                and not id(automaton) in anth.appendages])
                        first_zero = automaton.appendages.index(0)# for readability
                        automaton.appendages[first_zero] = id(other_automaton)#take first occurence of 0 and replace it with ID
                        # now we make this relation relfexive
                        second_first_zero = other_automaton.appendages[other_automaton.appendages.index(0)]
                        other_automaton.appendages[second_first_zero] = id(automaton)
        


    def create_social_bonds_with_hands_shake_rule(self, hands_shake):
        '''
        Here we need some graph theory.
        Function creates 
        Create a population where number of hands shakes
        between two automata is equal or less then hands_shake
        '''
        if not isinstance(hands_shake, int):
            raise ValueError("hands_shake: int expected, got rotten cabbage instead")
        #FIXME TODO FINISHME    

        pass


    def play_rounds(self, rounds, synchronously=True):
        ''' 
        That's the real game
        '''
        if not isinstance(rounds, int):
            raise ValueError("Rounds: int expected")
        if synchronously:
            pass
            #'ere we play synchronous game
        else:
            for x in xrange(0, rounds+1):
                random_automaton = choice(self.population)
                random_appendage = choice([ap for ap in random_automaton.appendages if ap!=0 ])
                random_neighbour = next(aut for aut in self.population if id(aut) == random_appendage)
                random_neighbour.change_state(random_automaton.state)

