from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run_game(self):
        while not self.model.is_game_over():
            self.view.display_board(self.model.get_board())
            print(f"Ход игрока {self.model.current_player}")
            position = int(input("Введите номер ячейки (0-8): "))
            self.model.make_move(position)

        self.view.display_board(self.model.get_board())
        result = self.model.check_winner()
        self.view.display_result(result)

if __name__ == "__main__":
    game_controller = Controller()
    game_controller.run_game()