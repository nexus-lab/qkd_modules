from QKDResources.pyfiles.helpermethods import makeQuestion, prepareQuestion, qonclick
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


def q3onClick(btn):
    qonclick(btn, q3)


q1 = prepareQuestion(
    r"1.\ \begin{bmatrix}1\\1\\0\end{bmatrix}, \begin{bmatrix}1\\2\\-1\end{bmatrix}, \begin{bmatrix}1\\0\\1\end{bmatrix}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"\left|\begin{matrix}1&1&1\\1&2&0\\0&-1&1\end{matrix}\right|= 0 \text{ Therefore, the set of vectors are not linearly indepdendent.}",
)
q2 = prepareQuestion(
    r"2.\ \begin{bmatrix}2\\-1\\1\end{bmatrix}, \begin{bmatrix}3\\-4\\-2\end{bmatrix}, \begin{bmatrix}5\\-10\\-8\end{bmatrix}",
    ["hint 1"],
    r"\left|\begin{matrix}2&3&5\\-1&-4&-10\\1&-2&-8\end{matrix}\right|= 0 \text{ Therefore, the set of vectors are not linearly indepdendent.}",
)
SAQuiz4_2 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.04 Self Assessment Quiz'),
        widgets.HTML(
            value='<b><font size="-1"<b>Maybe used for in-class hands-on practice.</b>'
        ),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz5_1():
    display(SAQuiz4_2)
    display(
        widgets.HTMLMath(
            value='<font size="+1">Show that the following set of vectors is not linearly independent,'
        )
    )
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
