class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def incrementPoints(self):
        self.points +=1
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))
    def toNumericalChoice(self):
        switcher={
            "rock":0,
            "paper":1,
            "scissor":2
        }
        return switcher[self.choice]

class GameRound:
    def __init__(self, p1, p2):
        self.rules=[[0,-1,1],
                    [1,0,-1],
                    [-1,1,0]]
        p1.choose()
        p2.choose()
        result=self.compareChoices(p1,p2)
        print("Round resulted in a {result} for {pname}.".format(result=self.getresultAsString(result), pname=p1.name))
        if result>0:
            p1.incrementPoints()
        elif result<0:
            p2.incrementPoints()
    def compareChoices(self,p1,p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getresultAsString(self,result):
        res={
            0:"draw",
            1:"win",
            -1:"lose"
        }
        return res[result]

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant(str(input("Name of Player 1 : ")))
        self.secondParticipant = Participant(str(input("Name of player 2 : ")))
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer=input("Continue game y/n: ")
        if answer=='y':
            GameRound(self.participant,self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name=self.participant.name,p1points=self.participant.points,p2name=self.secondParticipant.name,p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame=True
    def determineWinner(self):
        resultString="It's a Draw!"
        if self.participant.points > self.secondParticipant.points:
            resultString="Winner is {name}".format(name=self.participant.name)
        elif self.participant.points<self.secondParticipant.points:
            resultString="Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()