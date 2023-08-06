from project import userChoice, checkChoice, botChoice, finalAnswer

def test_botChoice():
    assert botChoice() == "rock" or "scissors" or "paper"

#!!Please use pytest -s for this!!
def test_userChoice():
    assert userChoice() == "rock" or "scissors" or "paper"

#!!Please use pytest -s for this!!
def test_checkChoice():
    assert checkChoice("") == None
    assert checkChoice("scissors") == None

#!!Please use pytest -s for this!!
def test_finalAnswer():
    assert finalAnswer("rock","paper") == "You lost!"
    assert finalAnswer("paper","rock") == "You won!"
    assert finalAnswer("paper","paper") == "Uh-oh! Thats a tie."
