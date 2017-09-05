import re

equation_list = []
solution_list = []
operators = {'+', '-', '//', '*'}

def evaluate_equation(eq):
   md_match = re.search('\d (*|/) \d', evaluate_equation)

def _operation(o):
   pass

def fill_lists():
   for op1 in operators:
      for op2 in operators:
         for op3 in operators:
            eq_string = '4 ' + op1 + ' 4 ' + op2 + ' 4 ' + op3 + ' 4'
            eq_ans = eval(eq_string)
            equation_list.append(eq_string)
            solution_list.append(eq_ans)

fill_lists()
loop_index = int(input())
for i in range(0, loop_index):
   num = int(input())
   if num in solution_list:
      found_index = solution_list.index(num)
      print(equation_list[found_index] + ' = ' + str(num))
   else:
      print("no solution")