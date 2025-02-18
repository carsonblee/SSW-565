from student import Student
from teacher import Teacher
from chess import Chess
from checkers import Checkers

if __name__ == "__main__":
    student = Student()
    teacher = Teacher()

    # Instances of a Chess game
    chess_game = Chess()
    chess_game.SetPlayerOne(student)
    chess_game.SetPlayerTwo(teacher)

    # Verify the number of players
    print(f"Number of players in Chess: {chess_game.GetNumberOfPlayers()}")

    # Call the play method
    chess_game.Play()

    # Instances of Checkers game
    checkers_game = Checkers()
    checkers_game.SetPlayerOne(student)
    checkers_game.SetPlayerTwo(teacher)

    # Verify the number of players
    print(f"Number of players in Checkers: {checkers_game.GetNumberOfPlayers()}")

    # Call the play method
    checkers_game.Play()