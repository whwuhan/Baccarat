from Component.Poker import *
from SystemConfig.Environment import *

if __name__ == "__main__":
    p1 = Poker(CardFace.CF_A, CardSuit.CS_HEARTS)
    print(p1.__dict__)
    print(p1.get_value())
    
    pokers = Poker.create_pokers()
    for p in pokers:
        print(p.__dict__)