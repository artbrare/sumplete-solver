from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from math import sqrt
from sumplete import Sumplete

service = FirefoxService(executable_path=GeckoDriverManager().install())

driver = webdriver.Firefox(service=service)

driver.get("https://sumplete.com/master/")

numbers = driver.find_elements(By.CLASS_NAME, "number")
n = int(sqrt(len(numbers))) # rows / columns

matrix = []
buttons = {}
for i, number in enumerate(numbers):
    if i % n == 0:
        matrix.append([]) # new row
    matrix[-1].append(int(number.text))
    buttons[(len(matrix)-1, len(matrix[-1]) - 1)] = number

# we store horizontal answers
hanswers = driver.find_elements(By.CLASS_NAME, "hanswer")
rows_answers = []
for hanswer in hanswers:
    rows_answers.append(int(hanswer.text))

# we store vertical answers
vanswers = driver.find_elements(By.CLASS_NAME, "vanswer")
cols_answers = []
for vanswer in vanswers:
    cols_answers.append(int(vanswer.text))

sumplete = Sumplete(matrix, rows_answers, cols_answers)
sumplete.solve()

# nice stuff
if sumplete.solved:
    for i in range(n):
        for j in range(n):
            if sumplete.answer[i][j]:
                buttons[(i, j)].click()
                buttons[(i, j)].click()
            else:
                buttons[(i, j)].click()