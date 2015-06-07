'''
another idea for automaton game:
cells join and form bigger units
there are rules for how when and where they join
they have this appendiges
depending on appendiges they join in one or another way
this can be also used for myu playing my moral game
social bonds are formed in taht way after allm, are they not?

Look: if automaton does not allow for unbound appendix, every structure created from such automata will be round-shaped.

Now: level 1 automata have rules to join and create level 2 automata
level 2 have another properties, emerging and they in turn join to form level 3 automata
which in turn have .... and so on and on 
But properties of second order automata must be kind of different, eh?
level 1 automata have defined appendages of two or more types
every automaton can have one or more appendages, their number can vary from automaton to automaton
Now, the 1st level automata will connect to form 2nd level automata, which will also have appendages, emerging appendages, 



 As automata join into higher levels, they can be more or less persisten. They form new organizations, and these can last longer or not

          ___________________
          |                  |      |\
          |                  |      | \
          |                  |      |  \
          |                  |      |   \
          |__________________|      |____\



Lets say that level 1 automata have size.
This is how you can approach emergence of shapes/appendages in level 2 automata and later in level 3 automata


emregence:
try to have two types of automata. They have simply different rules for joining with other automata.
For example A1 has appednix to its left, a2 to its right. 
or lets say like that:
letters here are first level automata with specific appendages represented by letters:

        A  A
         A  B
          A  A
         A  A
        A  A
this connection will be quite strong, because 5 out of 6 appendages are connected.
How long it will last? For as long as it can - it will be separated when stronger bonds will tear it apart.

'''
'''
For the general ontology of automata:
automaton can have state. Or not, ie. be stateless.
Automaton must have an appendage, either to interact with other automata
or to form structures with them

So we should have base class for Abstract Automaton
and two inheriting classes

'''


class StatelessAutomaton(list):
    """
    Actually, it could be an instance of list.
    Because appendages can be just pairs:
    {type:automaton_id.appendage_number }

    so the automaton shall be:
    [[x:46667.1], [x:873888:2], [y:762739:2]]


    Automaton with n-appendages (where n is >0 and <5) of different types.
    Here we do not play the game of influence. No interaction between automata is possible.
    Only possibility is that of forming higher order structures.
    By default, appendages are of only one - x type.
    By default, automaton has two appendages.
    #Later we can play with automata with growing appendages: 
    # and automata with changing types of appendages
    """

    def __init__(self, appendages={'x':4} ):
        '''
        Appendages must be a dict.
        '''
        if not isinstance(appendages, dict):
            raise ValueError("Appendages must be a dict")
        if not all(isinstance(x, str) for x in appendages.iterkeys()):
            raise ValueError("Appendage symbol shall be a string")

        if not all(isinstance(y, int) for x in appendages.itervalues()):
            raise ValueError("Appendage number shall be an int")

        if sum([y for y in appendages.itervalues()])>4:
            raise ValueError("Total number of appendages shall be less or equal to 4")
            
        for element in appendages.iterkeys():
            for number in range(0, appendages[element]+1)
                self.append([element,0])
                # And now the follwowing problem:
                # shall appendages have directions?


    def __str__(self):
        return self.__repr__
    def __repr__(self):
        return "Automaton "+str(id(self))

''' Note: we cannot use numpy.arrays, they can include only ints or floats'''
#'''PL: na razie nie mamy pomyslu na to jak przelamac dominujaca pozycje kwadracikow.
#pobawmy sie kwadracikami '''
class Space(list):
    '''
    Space populated by stateless automata
    being a list of lists
    it allows us to make sense of space
    and distance in space
    [x00, x01, x02, x03, x04]
    [x10, x11, x12, x13, x14]
    [x20, x21, x22, x23, x24]
    Here you can compute the distance.
    Distance matters. Connections make sense only for neighbouring automata.
    Now, the obctacle is that in this model we play four-side sqare-like automata.
    Now, automata must move. 
    That must mean that automata must move. 
    When automata move, also second class automata move.
    '''
    


