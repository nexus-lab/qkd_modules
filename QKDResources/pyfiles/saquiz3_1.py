import cmath
import math
import random

from IPython.display import Math, display
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets, Output

from QKDResources.pyfiles.complexgraph import createGraph, setGraph
from QKDResources.pyfiles.helpermethods import (
    buttonsuccess,
    checkComplex,
    checkfloat,
    checkfloatpair,
    makeButton,
    newCordBox,
    newfillblank,
    newfloatbox,
    newPolar,
)

# Layouts
numInputLayout = Layout(width="55px")
strInputLayout1 = Layout(width="90px")
strInputLayout2 = Layout(width="130px")
center = Layout(align_items="center")
# Boxes
SAQuiz3_1 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q01.05 Self Assessment Quiz'),
        widgets.HTML(
            value='<b><font size="-1"<b>May be used for in-class hands-on practice.</b>'
        ),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def rad2deg(radians):
    pi = math.pi
    degrees = 180 * radians / pi
    return degrees


def deg2rad(degrees):
    pi = math.pi
    radians = pi * degrees / 180
    return radians


# Logic
def QCheckAnswers3_1(btn):
    count = 0
    for q in qlist3_1_1:
        count += checkfloatpair(q[1].value, q[2].value, q[0], q[4], q[5])
    for q in qlist3_1_2:
        count += checkfloatpair(q[1].value, q[2].value, q[0], q[4], q[5])
    for q in qlist3_1_3:
        count += checkfloatpair(q[1].value, q[2].value, q[0], q[4], q[5])
    buttonsuccess(Qbtn3_1, count, 8, 5)


def graphstart(btn):
    toGraph = cmath.rect(
        qlist3_1_3[int(btn.tooltip[-1:])][1].value,
        deg2rad(qlist3_1_3[int(btn.tooltip[-1:])][2].value),
    )
    setGraph(toGraph.real, toGraph.imag)


def graphstart2(btn):
    toGraph = cmath.rect(
        qlist3_1_1[int(btn.tooltip[-1:])][1].value,
        deg2rad(qlist3_1_1[int(btn.tooltip[-1:])][2].value),
    )
    setGraph(toGraph.real, toGraph.imag)


def graphstart3(btn):
    toGraph = qlist3_1_2[int(btn.tooltip[-1:])][1].value + (
        1j * qlist3_1_2[int(btn.tooltip[-1:])][2].value
    )
    setGraph(toGraph.real, toGraph.imag)


def createQuiz3_1():
    createGraph()
    display(SAQuiz3_1)
    display(
        widgets.HTMLMath(
            value='<font size="+1">Convert the following into polar representations.'
        )
    )

    qlist3_1_3.append(newPolar("1.\ c = 1+i", [math.sqrt(2), 45], strInputLayout1))
    qlist3_1_3.append(
        newPolar("2.\ c = 21+48i", [math.sqrt(2745), 66.37], strInputLayout1)
    )
    qlist3_1_3.append(
        newPolar("3.\ c = 3-45i", [math.sqrt(2034), 273.81], strInputLayout1)
    )
    count = 0
    for q in qlist3_1_3:
        rho_output = Output()
        with rho_output:
            display(Math(r"\rho = "))
        theta_output = Output()
        with theta_output:
            display(Math(r"\theta = "))
        temp = widgets.Button(
            description="Graph It",
            disabled=False,
            button_style="success",  # 'success', 'info', 'warning', 'danger' or ''
            tooltip="Graph It " + str(count),
            icon="check",
        )
        temp.on_click(graphstart)
        count += 1
        display(q[3])
        display(
            HBox(
                [
                    rho_output,
                    q[1],
                    theta_output,
                    q[2],
                    temp,
                    q[4],
                    q[5],
                ]
            )
        )
    display(
        widgets.HTMLMath(
            value='<font size="+1">Convert the following polar representations into cartesian representations.'
        )
    )
    qlist3_1_2.append(
        newCordBox(
            r"4.\ \rho=25 \text{ and } \theta=60^\circ",
            [12.5, 21.65],
            numInputLayout,
        )
    )
    qlist3_1_2.append(
        newCordBox(
            r"5.\ \rho=15 \text{ and } \theta=45^\circ",
            [10.61, 10.61],
            numInputLayout,
        )
    )
    qlist3_1_2.append(
        newCordBox(
            r"6.\ \rho=45 \text{ and } \theta=30^\circ",
            [38.97, 22.5],
            numInputLayout,
        )
    )
    count = 0
    for q in qlist3_1_2:
        temp = widgets.Button(
            description="Graph It",
            disabled=False,
            button_style="success",  # 'success', 'info', 'warning', 'danger' or ''
            tooltip="Graph It " + str(count),
            icon="check",
        )
        temp.on_click(graphstart3)
        count += 1
        display(q[3])
        display(
            HBox(
                [
                    Label(value="  ("),
                    q[1],
                    Label(value=" , "),
                    q[2],
                    Label(value=") "),
                    Label(layout=Layout(width="10px")),
                    temp,
                    q[4],
                    q[5],
                ]
            )
        )
    display(
        widgets.HTMLMath(
            value='<font size="+1">Multiply the following using polar representations.'
        )
    )
    qlist3_1_1.append(
        newPolar(r"7.\ c_1=1+2i \text{ and } c_2=4i", [8.94, 140.4], strInputLayout1)
    )
    qlist3_1_1.append(
        newPolar(
            r"8.\ c_1=2-4i \text{ and } c_2=3-2i",
            [math.sqrt(2034), -97.13],
            strInputLayout1,
        )
    )
    count = 0
    for q in qlist3_1_1:
        temp = widgets.Button(
            description="Graph It",
            disabled=False,
            button_style="success",  # 'success', 'info', 'warning', 'danger' or ''
            tooltip="Graph It " + str(count),
            icon="check",
        )
        temp.on_click(graphstart2)
        count += 1
        display(q[3])
        display(
            HBox(
                [
                    rho_output,
                    q[1],
                    theta_output,
                    q[2],
                    temp,
                    q[4],
                    q[5],
                ]
            )
        )

    setGraph(0.0001, 0.0001)
    setGraph(0, 0)
    display(VBox([Qbtn3_1], layout=center))


# Events
Qbtn3_1 = makeButton()
qlist3_1_3 = []
qlist3_1_1 = []
qlist3_1_2 = []
Qbtn3_1.on_click(QCheckAnswers3_1)
