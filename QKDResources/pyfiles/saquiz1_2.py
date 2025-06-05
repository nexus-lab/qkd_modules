import cmath
import random

from IPython.display import Math, display
from ipywidgets import Box, Button, HBox, Label, Layout, Output, VBox, interact, widgets

from QKDResources.pyfiles.helpermethods import (
    empty,
    getComplex,
    qcorrect,
    qformaterror,
    qincorrect,
    qunknownerror,
)

numInputLayout = Layout(width="55px")
strInputLayout1 = Layout(width="90px")
strInputLayout2 = Layout(width="130px")

hidden = Layout(visibility="hidden")
visible = Layout(visibility="visible")
QValid2_1 = widgets.Valid(value=False, readout="Incorrect", layout=hidden)
QValid2_2 = widgets.Valid(value=False, readout="Incorrect", layout=hidden)
QValid2_3 = widgets.Valid(value=False, readout="Incorrect", layout=hidden)
QValid2_4 = widgets.Valid(value=False, readout="Incorrect", layout=hidden)
QLabel2_1 = widgets.HTML(value="")
QLabel2_2 = widgets.HTML(value="")
QLabel2_3 = widgets.HTML(value="")
QLabel2_4 = widgets.HTML(value="")

qstr1_2_1 = widgets.Text(placeholder="a + bi", disabled=False, layout=strInputLayout1)
qstr1_2_2 = widgets.Text(placeholder="a + bi", disabled=False, layout=strInputLayout1)
qstr1_2_3 = widgets.Text(placeholder="a + bi", disabled=False, layout=strInputLayout2)
qstr1_2_4 = widgets.Text(placeholder="a + bi", disabled=False, layout=strInputLayout2)
qstr1_2_5 = widgets.Text(placeholder="a + bi", disabled=False, layout=strInputLayout2)

Q1_output = Output()
Q2_output = Output()
Q3_output = Output()
Q4_output = Output()
with Q1_output:
    display(Math(r"1.\ \text{Solve for } x \text{ where } x^2 + 2x + 10 = 0."))
with Q2_output:
    display(
        Math(
            r"\text{Let } c_1 = 2 + 50i \text{ and } c_2 = 3 + 0.5i. \text{ Compute the following:}"
        )
    )
    display(Math(r"2.\ c_1 + c_2"))
with Q3_output:
    display(Math(r"3.\ c_1 \times c_2"))
with Q4_output:
    display(Math(r"4.\ 7 \times c_2"))

Qbtn_2 = widgets.Button(
    description="Check Answers",
    disabled=False,
    button_style="success",  # 'success', 'info', 'warning', 'danger' or ''
    tooltip="Check Answers",
    icon="check",
)

SAQuiz1_2 = VBox(
    [
        Label("Q01.02 Self Assessment Quiz"),
        Label("May be used for in-class hands-on practice."),
        Q1_output,
        HBox(
            [
                qstr1_2_1,
                Label("and"),
                qstr1_2_2,
                QValid2_1,
                QLabel2_1,
            ]
        ),
        Q2_output,
        HBox([qstr1_2_3, QValid2_2, QLabel2_2]),
        Q3_output,
        HBox([qstr1_2_4, QValid2_3, QLabel2_3]),
        Q4_output,
        HBox([qstr1_2_5, QValid2_4, QLabel2_4]),
        VBox([HBox([Qbtn_2])], layout=Layout(align_items="center")),
    ]
)


def QCheckAnswers_1(btn):
    count = 0
    try:
        if getComplex(qstr1_2_1.value) == (-1 + 3j) and getComplex(qstr1_2_2.value) == (
            -1 - 3j
        ):
            qcorrect(QValid2_1, QLabel2_1)
            count += 1
        else:
            if getComplex(qstr1_2_1.value) == (-1 - 3j) and getComplex(
                qstr1_2_2.value
            ) == (-1 + 3j):
                qcorrect(QValid2_1, QLabel2_1)
                count += 1
            else:
                qincorrect(QValid2_1, QLabel2_1)
    except ValueError as error:
        qformaterror(QValid2_1, QLabel2_1)
    except:
        qunknownerror(QValid2_1, QLabel2_1)

    try:
        if getComplex(qstr1_2_3.value) == (5 + 50.5j):
            qcorrect(QValid2_2, QLabel2_2)
            count += 1
        else:
            qincorrect(QValid2_2, QLabel2_2)
    except ValueError as error:
        qformaterror(QValid2_2, QLabel2_2)
    except:
        qunknownerror(QValid2_2, QLabel2_2)

    try:
        if getComplex(qstr1_2_4.value) == (-19 + 151j):
            qcorrect(QValid2_3, QLabel2_3)
            count += 1
        else:
            qincorrect(QValid2_3, QLabel2_3)
    except ValueError as error:
        qformaterror(QValid2_3, QLabel2_3)
    except:
        qunknownerror(QValid2_3, QLabel2_3)

    try:
        if getComplex(qstr1_2_5.value) == (21 + 3.5j):
            qcorrect(QValid2_4, QLabel2_4)
            count += 1
        else:
            qincorrect(QValid2_4, QLabel2_4)
    except ValueError as error:
        qformaterror(QValid2_4, QLabel2_4)
    except:
        qunknownerror(QValid2_4, QLabel2_4)

    if qstr1_2_1.value == "" or qstr1_2_2.value == "":
        empty(QValid2_1, QLabel2_1)
    if qstr1_2_3.value == "":
        empty(QValid2_2, QLabel2_2)
    if qstr1_2_4.value == "":
        empty(QValid2_3, QLabel2_3)
    if qstr1_2_5.value == "":
        empty(QValid2_4, QLabel2_4)

    if count == 4:
        Qbtn_2.button_style = "info"
        Qbtn_2.description = "Way to Go!"
        Qbtn_2.icon = "check"
    if count == 3:
        Qbtn_2.button_style = "warning"
        Qbtn_2.icon = "times"
        Qbtn_2.description = "Close!"
    if count < 3:
        Qbtn_2.button_style = "danger"
        Qbtn_2.icon = "times"
        Qbtn_2.description = "Try Again"


Qbtn_2.on_click(QCheckAnswers_1)
