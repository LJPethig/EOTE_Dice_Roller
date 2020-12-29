import sys
import dice_list
from random import choice

from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication,
                             QPushButton, QSpinBox, QGridLayout, QFormLayout)
from PyQt5.QtGui import QPixmap, QFont


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        width = 370
        height = 550
        x = 20
        y = 70

        self.setGeometry(x, y, width, height)

        self.setFont(QFont('Ocean', 24))

        self.label_desc = '            The\nEdge of the Empire\n      Dice Roller'
        self.label = QLabel(self.label_desc)
        self.label.setFont(QFont('Ocean', 32, QFont.Bold))

        self.boost_dice_label = QLabel('Boost dice : ')
        self.ability_dice_label = QLabel('Ability dice : ')
        self.proficiency_dice_label = QLabel('Proficiency dice : ')
        self.setback_dice_label = QLabel('Setback dice : ')
        self.difficulty_dice_label = QLabel('Difficulty dice : ')
        self.challenge_dice_label = QLabel('Challenge dice : ')
        self.force_dice_label = QLabel('Force dice : ')

        self.boost_dice_spinner = QSpinBox(minimum=0, maximum=6)
        self.boost_dice_spinner.setFixedSize(45, 32)
        self.ability_dice_spinner = QSpinBox(minimum=0, maximum=6)
        self.ability_dice_spinner.setFixedSize(45, 32)
        self.proficiency_dice_spinner = QSpinBox(minimum=0, maximum=6)
        self.proficiency_dice_spinner.setFixedSize(45, 32)
        self.setback_dice_spinner = QSpinBox(minimum=0, maximum=6)
        self.setback_dice_spinner.setFixedSize(45, 32)
        self.difficulty_dice_spinner = QSpinBox(minimum=0, maximum=6)
        self.difficulty_dice_spinner.setFixedSize(45, 32)
        self.challenge_dice_spinner = QSpinBox(minimum=0, maximum=6)
        self.challenge_dice_spinner.setFixedSize(45, 32)
        self.force_dice_spinner = QSpinBox(minimum=0, maximum=6)
        self.force_dice_spinner.setFixedSize(45, 32)

        self.roll_button = QPushButton('Roll dice')
        self.roll_button.setFixedSize(150, 40)
        self.roll_button.clicked.connect(self.pass_dice)

        self.quit_button = QPushButton('Quit')
        self.quit_button.setFixedSize(150, 40)
        self.quit_button.clicked.connect(self.quit_app)

        self.outer_layout = QVBoxLayout()
        self.outer_layout.addWidget(self.label)

        self.lower_layout = QHBoxLayout()
        self.lower_layout.addWidget(self.roll_button)
        self.lower_layout.addWidget(self.quit_button)

        self.inner_layout = QFormLayout()

        self.inner_layout.addRow(self.boost_dice_label, self.boost_dice_spinner)
        self.inner_layout.addRow(self.ability_dice_label, self.ability_dice_spinner)
        self.inner_layout.addRow(self.proficiency_dice_label, self.proficiency_dice_spinner)
        self.inner_layout.addRow(self.setback_dice_label, self.setback_dice_spinner)
        self.inner_layout.addRow(self.difficulty_dice_label, self.difficulty_dice_spinner)
        self.inner_layout.addRow(self.challenge_dice_label, self.challenge_dice_spinner)
        self.inner_layout.addRow(self.force_dice_label, self.force_dice_spinner)

        self.setLayout(self.outer_layout)
        self.outer_layout.addLayout(self.inner_layout)
        self.outer_layout.addLayout(self.lower_layout)

        self.output_window = OutputWindow()
        self.result_window = ResultWindow()

        self.show()

    def quit_app(self):
        self.output_window.close()
        self.result_window.close()
        self.close()

    def pass_dice(self):
        self.clear_window(self.output_window)  # clear output window
        # create list from all spinner values to pass to roll_die function
        # dice_to_roll list of tuples (dice_type, dice_img_folder, number_of_dice)
        dice_to_roll = []
        if self.boost_dice_spinner.value():
            dice_to_roll.append(('boost_die_d6', 'Boost_d6', self.boost_dice_spinner.value()))
        if self.ability_dice_spinner.value():
            dice_to_roll.append(('ability_die_d8', 'Ability_d8', self.ability_dice_spinner.value()))
        if self.proficiency_dice_spinner.value():
            dice_to_roll.append(('proficiency_die_d12', 'Proficiency_d12', self.proficiency_dice_spinner.value()))
        if self.setback_dice_spinner.value():
            dice_to_roll.append(('setback_die_d6', 'Setback_d6', self.setback_dice_spinner.value()))
        if self.difficulty_dice_spinner.value():
            dice_to_roll.append(('difficulty_die_d8', 'Difficulty_d8', self.difficulty_dice_spinner.value()))
        if self.challenge_dice_spinner.value():
            dice_to_roll.append(('challenge_die_d12', 'Challenge_d12', self.challenge_dice_spinner.value()))
        if self.force_dice_spinner.value():
            dice_to_roll.append(('force_die_d12', 'Force_d12', self.force_dice_spinner.value()))
        if dice_to_roll:
            return self.roll_die(dice_to_roll)

    def clear_window(self, window_to_clear):
        # clear all widgets in passed window instance
        for i in reversed(range(window_to_clear.main_layout.count())):
            window_to_clear.main_layout.itemAt(i).widget().deleteLater()

    def roll_die(self, dice_to_roll):
        dice_effects = ''  # string of all dice roll effect letters.

        for i in range(len(dice_to_roll)):  # iterate over types of dice to roll
            for dice_num in range(dice_to_roll[i][2]):  # iterate over number of dice to roll
                die_type = dice_to_roll[i][0]
                die_face = choice(getattr(dice_list, die_type))  # getattr required to pass variable(die_type) as attribute
                # die_face is a tuple (die_face_img, effect)
                die_img_folder = dice_to_roll[i][1]  # folder location of dice type image
                self.die_face_img = QPixmap(f"EOTE_dice_images/{die_img_folder}/{die_face[0]}.png")
                dice_effects += (die_face[1])  # add rolled dice effect to list
                self.die_face_label = QLabel()
                self.die_face_label.setPixmap(self.die_face_img)
                self.output_window.main_layout.addWidget(self.die_face_label, i, dice_num)
        return self.process_dice_effects(dice_effects)

    def process_dice_effects(self, effects):
        # tally all dice effects and calculate results
        # success cancels failure, advantage cancels threat, triumph and despair do not cancel each other
        success = effects.count('S')
        advantage = effects.count('A')
        triumph = effects.count('X')
        failure = effects.count('F')
        threat = effects.count('T')
        despair = effects.count('D')
        light_side = effects.count('W')
        dark_side = effects.count('B')

        success_result = 0
        failure_result = 0
        advantage_result = 0
        threat_result = 0

        if success > failure:
            success_result = success - failure
        elif failure > success:
            failure_result = failure - success
        if advantage > threat:
            advantage_result = advantage - threat
        elif threat > advantage:
            threat_result = threat - advantage
        return self.output_results(success_result, failure_result, advantage_result, threat_result,
                                   triumph, despair, light_side, dark_side)

    def output_results(self, success, fail, advantage, threat, triumph, despair, light, dark):
        # display calculated results to window
        self.clear_window(self.result_window)  # clear result window
        if success:
            success_label = QLabel(f'{success} Success')
            self.result_window.main_layout.addWidget(success_label)
        if fail:
            failure_label = QLabel(f'{fail} Failure')
            self.result_window.main_layout.addWidget(failure_label)
        if advantage:
            advantage_label = QLabel(f'{advantage} Advantage')
            self.result_window.main_layout.addWidget(advantage_label)
        if threat:
            threat_label = QLabel(f'{threat} Threat')
            self.result_window.main_layout.addWidget(threat_label)
        if triumph:
            triumph_label = QLabel(f'{triumph} Triumph')
            self.result_window.main_layout.addWidget(triumph_label)
        if despair:
            despair_label = QLabel(f'{despair} Despair')
            self.result_window.main_layout.addWidget(despair_label)
        if light:
            light_label = QLabel(f'{light} Light side')
            self.result_window.main_layout.addWidget(light_label)
        if dark:
            dark_label = QLabel(f'{dark} Dark side')
            self.result_window.main_layout.addWidget(dark_label)


class OutputWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(413, 70, 200, 550)
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.show()


class ResultWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(900, 70, 370, 550)
        self.setFont(QFont('Ocean', 24))
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

