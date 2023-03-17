"""Advanced Python + flet App Password Strength Check"""

import flet
from flet import *

# Setting two Controls
CONTROLS = []
STATUS = []


# Decoration Area
def store_control(function):
    def wrapper(*args, **kwargs):
        reference = function(*args, **kwargs)
        # Control "0" is part of the kwargs' parameters
        if kwargs["control"] == 0:
            CONTROLS.append(reference)
        else:
            STATUS.append(reference)

        return reference

    return wrapper


# The Class for my password check logic.
class PasswordStrengthChecker():
    def __init__(self, password):
        self.password = password

    # Here we will be calling all our functions from.
    def length_check(self):
        # Depending on our input, this is where we return integers
        # based on the input length. Our UI will speak better here.
        length = len(self.password)
        if length > 0 and length < 8:
            return 0
        elif length >= 8 and length < 12:
            return 1
        elif length >= 12 and length < 16:
            return 2
        elif length >= 16:
            return 3

    # Time to check the character types.
    def character_check(self):
        characters = set(self.password)
        lower_case = set("abcdefghijklmnopqrstuvwxyz")
        upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        digits = set("0123456789")
        special_characters = set("~`!@#$%^&*()-_þʼ«æ…+={}[]|/\:;`><.?")

        score = 0
        if any(char in lower_case for char in characters):
            score += 1
        if any(char in upper_case for char in characters):
            score += 1
        if any(char in digits for char in characters):
            score += 1
        if any(char in special_characters for char in characters):
            score += 1

        if score == 1:
            return 0
        elif score == 2:
            return 1
        elif score == 3:
            return 2
        elif score == 4:
            return 3

    # We are going to check the repatriation.
    def repeat_check(self):
        if len(self.password) == 0:
            return 2  # When this number is applied in our UI, it will make sense.
        else:
            for i in range(len(self.password) - 2):
                if self.password[i] == self.password[i + 1] == self.password[i + 2]:
                    return 0  # This means that the string has been repeated.
            return 1  # This number represent no reputation.

    # Time to check sequential occurrences.
    def sequential_check(self):
        if len(self.password) == 0:
            return 2
        else:
            for i in range(len(self.password) - 2):
                # Password in range of 3 characters will be checked. will return Weak Password.
                if (
                        self.password[i: i + 3].isdigit()
                        or self.password[i: i + 3].islower()
                        or self.password[i: i + 3].isupper()
                ):
                    return 0
            return 1


class AppWindow(UserControl):
    def __init__(self):
        super().__init__()

    # We will have to call the inner functions here.
    def check_password(self, e):
        password_strength_checker = PasswordStrengthChecker(e.data)
        password_length = password_strength_checker.length_check()
        self.password_length_status(password_length)
        # Integers expected according to the length of our passwords.

        character_checker = password_strength_checker.character_check()
        self.character_check_status(character_checker)

        repeat_check = password_strength_checker.repeat_check()
        self.repeat_check_status(repeat_check)

        sequential_check = password_strength_checker.sequential_check()
        self.sequential_check_status(sequential_check)

    # Just to be sure if the Criteria are satisfied.
    def criteria_satisfied(self, index, status):
        if status == 3:
            STATUS[index].controls[0].offset = transform.Offset(0, 0)
            STATUS[index].controls[0].opacity = 1
            STATUS[index].controls[0].content.value = True
            STATUS[index].controls[0].update()
        else:
            STATUS[index].controls[0].content.value = False
            STATUS[index].controls[0].offset = transform.Offset(-0.5, 0)
            STATUS[index].controls[0].opacity = 0
            STATUS[index].controls[0].update()

    def password_length_status(self, strength):
        if strength == 0:
            CONTROLS[0].controls[1].controls[0].bgcolor = "red"
            CONTROLS[0].controls[1].controls[0].width = 40
        elif strength == 1:
            CONTROLS[0].controls[1].controls[0].bgcolor = "yellow"
            CONTROLS[0].controls[1].controls[0].width = 70
        elif strength == 2:
            CONTROLS[0].controls[1].controls[0].bgcolor = "green400"
            CONTROLS[0].controls[1].controls[0].width = 100
        elif strength == 3:
            CONTROLS[0].controls[1].controls[0].bgcolor = "green900"
            CONTROLS[0].controls[1].controls[0].width = 130
        else:
            CONTROLS[0].controls[1].controls[0].width = 0

        CONTROLS[0].controls[1].controls[0].opacity = 1
        CONTROLS[0].controls[1].controls[0].update()

        return self.criteria_satisfied(0, strength)

    def character_check_status(self, strength):
        if strength == 0:
            CONTROLS[1].controls[1].controls[0].bgcolor = "red"
            CONTROLS[1].controls[1].controls[0].width = 40
        elif strength == 1:
            CONTROLS[1].controls[1].controls[0].bgcolor = "yellow"
            CONTROLS[1].controls[1].controls[0].width = 70
        elif strength == 2:
            CONTROLS[1].controls[1].controls[0].bgcolor = "green400"
            CONTROLS[1].controls[1].controls[0].width = 100
        elif strength == 3:
            CONTROLS[1].controls[1].controls[0].bgcolor = "green900"
            CONTROLS[1].controls[1].controls[0].width = 130
        else:
            CONTROLS[1].controls[1].controls[0].width = 0

        CONTROLS[1].controls[1].controls[0].opacity = 1
        CONTROLS[1].controls[1].controls[0].update()

        return self.criteria_satisfied(1, strength)

    def repeat_check_status(self, strength):
        if strength == 0:
            CONTROLS[2].controls[1].controls[0].bgcolor = "red"
            CONTROLS[2].controls[1].controls[0].width = 65
        elif strength == 1:
            CONTROLS[2].controls[1].controls[0].bgcolor = "green900"
            CONTROLS[2].controls[1].controls[0].width = 130

        else:
            CONTROLS[2].controls[1].controls[0].width = 0

        CONTROLS[2].controls[1].controls[0].opacity = 1
        CONTROLS[2].controls[1].controls[0].update()

        if strength == 1:
            strength == 3
            return self.criteria_satisfied(2, strength)
        else:
            return self.criteria_satisfied(0, strength)



        # Making this a little different.

    #  if strength == 1:
    #     strength =3

    # This is for sequential Check
    def sequential_check_status(self, strength):
        if strength == 0:
            CONTROLS[3].controls[1].controls[0].bgcolor = "red"
            CONTROLS[3].controls[1].controls[0].width = 65
        elif strength == 1:
            CONTROLS[3].controls[1].controls[0].bgcolor = "green900"
            CONTROLS[3].controls[1].controls[0].width = 130

        else:
            CONTROLS[3].controls[1].controls[0].width = 0

        CONTROLS[3].controls[1].controls[0].opacity = 1
        CONTROLS[3].controls[1].controls[0].update()

        if strength == 1:
            strength == 3
            return self.criteria_satisfied(2, strength)
        else:
            return self.criteria_satisfied(2, strength)

        # return self.criteria_satisfied(3, strength)


    # I outline the password Checking process here.
    @store_control
    def check_criteria_display(self, criteria, description, control: int):
        return Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            spacing=5,
            controls=[
                Column(
                    spacing=2,
                    controls=[
                        Text(value=criteria, size=12, width='bold'),
                        Text(value=description, size=12, color="white54"),
                    ],
                ),
                Row(
                    spacing=0,
                    alignment=MainAxisAlignment.START,
                    controls=[
                        Container(
                            height=5,
                            opacity=0,
                            animate=350,
                            border_radius=10,
                            animate_opacity=animation.Animation(350, "decelerate"),
                        )
                    ]
                )
            ],
        )

    # UI checkbox for paasword criteria.
    @store_control
    def check_status_display(
            self, control: int):
        return Row(
            alignment=MainAxisAlignment.END,
            controls=[
                Container(
                    opacity=0,
                    offset=transform.Offset(-0.5, 0),
                    animate_offset=animation.Animation(700, "decelerate"),
                    animate_opacity=animation.Animation(700, "decelerate"),
                    border_radius=50,
                    width=21,
                    height=21,
                    alignment=alignment.center,
                    content=Checkbox(
                        scale=Scale(0.7),
                        fill_color="#7df6dd",
                        check_color='blue',
                        disabled=True,
                    ),
                ),
            ]
        )


    # Main Display
    def password_strength_display(self):
        return Container(
            width=400,
            height=500,
            bgcolor="#1f262f",
            border_radius=10,
            padding=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=4,
                controls=[
                    Divider(height=5, color="transparent"),
                    Text("Password Strength Checker", size=24, color='white',
                         width="bolder"),
                    Text(
                        "Please Input your password and Check the Strength!",
                        size=14,
                        color='white',
                        width="w400",
                    ),
                    Divider(height=25, color="transparent"),
                    # Our Criteria has been called above, so we can now use it here.
                    self.check_criteria_display(
                        "1.Length Check",
                        "Strong passwords are 12 characters or above",

                        # We will decorate this int above.
                        control=0,
                    ),
                    self.check_status_display(control=1),
                    Divider(height=10, color="transparent"),
                    self.check_criteria_display(
                        "2. Character Check",
                        "Will Check Upper, lower, and special characters",
                        # We will decorate this int above.
                        control=0,
                    ),
                    self.check_status_display(control=1),
                    Divider(height=10, color="transparent"),
                    self.check_criteria_display(
                        "3. Repeat Checker",
                        "Checking for Any repetitions...",
                        # We will decorate this int above.
                        control=0,
                    ),
                    self.check_status_display(control=1),
                    Divider(height=10, color="transparent"),
                    self.check_criteria_display(
                        "4. Sequential Checker",
                        "This will Check for sequences...",
                        # We wi ll decorate this int above.
                        control=0,
                    ),
                    self.check_status_display(control=1),
                ],
            ),
        )

    # Text Input Area
    def password_text_field_display(self):
        return Row(
            spacing=20,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Icon(
                    name=icons.LOCK_OUTLINE_ROUNDED,
                    size=16, opacity=0.85),
                TextField(
                    border_color="transparent",
                    bgcolor="transparent",
                    height=20,
                    width=200,
                    text_size=14,
                    content_padding=3,
                    cursor_color="white",
                    cursor_width=1,
                    color="black",
                    hint_text="Type password here...",
                    hint_style=TextStyle(
                        size=14,
                    ),
                    on_change=lambda e: self.check_password(e),
                    password=True,
                )
            ],
        )

    # User input Area.
    def password_input_display(self):
        return Card(
            width=350,
            height=60,
            elevation=14,
            offset=transform.Offset(0, -0.25),
            content=Container(
                padding=padding.only(left=15),
                content=Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        self.password_text_field_display(),
                        IconButton(icon=icons.COPY,
                                   icon_size=18),
                    ],
                )
            )
        )

    def build(self):
        return Card(
            elevation=20,
            content=Container(
                width=400,
                height=520,
                border_radius=10,
                bgcolor="#1f262f",
                content=Column(
                    spacing=0,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self.password_strength_display(),
                        self.password_input_display(),
                    ],
                ),
            ),
        )


def main(page: page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.add(AppWindow())
    page.update()


if __name__ == '__main__':
    flet.app(target=main)
