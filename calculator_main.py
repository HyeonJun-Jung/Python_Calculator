import sys
import math
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation_number = QGridLayout()
        layout_Answer = QGridLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.equation = QLineEdit("")
        self.answer = QLineEdit("")

        ### Layout_Answer에 LineEdit 추가
        layout_Answer.addWidget(self.answer)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation_number 레이아웃에 추가
        layout_operation_number.addWidget(button_plus, 4, 3)
        layout_operation_number.addWidget(button_minus, 3, 3)
        layout_operation_number.addWidget(button_product, 2, 3)
        layout_operation_number.addWidget(button_division, 1, 3)

        ### %, CE, C, 1/x, x^2, x^(1/2) 버튼 생성
        button_mod =  QPushButton("%")
        button_CE =  QPushButton("CE")
        button_C =  QPushButton("C")
        button_reciprocal = QPushButton("1/x")
        button_Square = QPushButton("x^2")
        button_SquareRoot = QPushButton("x^(1/2)")

        ### %, CE, C, 1/x, x^2, x^(1/2) 버튼에 기능 추가
        button_mod.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_CE.clicked.connect(self.button_clear_clicked)
        button_C.clicked.connect(self.button_clear_clicked)
        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)
        button_Square.clicked.connect(self.button_square_clicked)
        button_SquareRoot.clicked.connect(self.button_squareRoot_clicked)

        ### %, CE, C, 1/x, x^2, x^(1/2) 버튼 을 layout_operation_number 레이아웃에 추가
        layout_operation_number.addWidget(button_mod, 0, 0)
        layout_operation_number.addWidget(button_CE, 0, 1)
        layout_operation_number.addWidget(button_C, 0, 2)
        layout_operation_number.addWidget(button_reciprocal, 1, 0)
        layout_operation_number.addWidget(button_Square, 1, 1)
        layout_operation_number.addWidget(button_SquareRoot, 1, 2)

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        # BackSpace와 Equal을 Layout에 추가
        layout_operation_number.addWidget(button_backspace, 0, 3)
        layout_operation_number.addWidget(button_equal, 5, 3)

        ### 숫자 버튼 생성하고, layout_Operation_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_operation_number.addWidget(number_button_dict[number], 4 - x, y)
            elif number==0:
                layout_operation_number.addWidget(number_button_dict[number], 3 + 2, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_operation_number.addWidget(button_dot, 3 + 2, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_operation_number.addWidget(button_double_zero, 3 + 2, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_Answer)
        main_layout.addLayout(layout_operation_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)
        answer = self.answer.text()
        answer += str(num)
        self.answer.setText(answer)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)
        self.answer.setText("")

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.equation.setText(str(solution))
        self.answer.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.answer.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)
        answer = self.answer.text()
        answer = answer[:-1]
        self.answer.setText(answer)

    def button_square_clicked(self):
        equation = float(self.answer.text())
        equation = math.pow(equation, 2)
        self.equation.setText(str(equation))
        self.answer.setText(str(equation))

    def button_squareRoot_clicked(self):
        equation = float(self.answer.text())
        equation = math.sqrt(equation)
        self.equation.setText(str(equation))
        self.answer.setText(str(equation))

    def button_reciprocal_clicked(self):
        equation = float(self.answer.text())
        equation = 1/equation
        self.equation.setText(str(equation))
        self.answer.setText(str(equation))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())