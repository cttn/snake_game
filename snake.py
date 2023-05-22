import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import random

class SnakeGame(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        self.snake = [(0, 0)]
        self.direction = Qt.Key_Right
        self.food = self.generate_food()

        self.setWindowTitle("Snake Game")
        self.setGeometry(100, 100, 400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)

        if self.check_collision():
            self.game_over(painter)
            return

        self.move_snake()
        self.draw_snake(painter)
        self.draw_food(painter)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down):
            self.direction = event.key()

    def move_snake(self):
        head = self.snake[0]
        if self.direction == Qt.Key_Left:
            new_head = (head[0] - 10, head[1])
        elif self.direction == Qt.Key_Right:
            new_head = (head[0] + 10, head[1])
        elif self.direction == Qt.Key_Up:
            new_head = (head[0], head[1] - 10)
        elif self.direction == Qt.Key_Down:
            new_head = (head[0], head[1] + 10)

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def draw_snake(self, painter):
        painter.setBrush(Qt.white)
        for position in self.snake:
            painter.drawRect(position[0], position[1], 10, 10)

    def draw_food(self, painter):
        painter.setBrush(Qt.red)
        painter.drawRect(self.food[0], self.food[1], 10, 10)

    def generate_food(self):
        # Generar una nueva posición aleatoria para la comida
        # Aquí puedes personalizar el rango de posición de la comida
        # Generar una nueva posición aleatoria para la comida
        x = random.randint(0, self.width() - 10)
        y = random.randint(0, self.height() - 10)
        return x // 10 * 10, y // 10 * 10

    # Verificar si la serpiente ha chocado contra una pared o contra su propio cuerpo
    def check_collision(self):
        head = self.snake[0]
        x, y = head

        # Verificar si la serpiente ha chocado contra una pared
        if x < 0 or x >= self.width() or y < 0 or y >= self.height():
            return True

        # Verificar si la serpiente ha chocado contra su propio cuerpo
        if head in self.snake[1:]:
            return True

        return False

    def game_over(self, painter):
        painter.setPen(Qt.white)
        painter.setFont(QFont('Arial', 20))
        painter.drawText(self.rect(), Qt.AlignCenter, "Game Over")

        self.timer.stop()

    def run(self):
        self.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = SnakeGame()
    game.run()
