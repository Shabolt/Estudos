machine = 0

emp1f = int(input())
emp2f = int(input())
emp3f = int(input())

emp1to1f = emp1f*0
emp1to2f = emp1f*2
emp1to3f = emp1f*4

emp2to2f = emp2f*0
emp2to1f = emp2f*2
emp2to3f = emp2f*2

emp3to3f = emp3f*0
emp3to2f = emp3f*2
emp3to1f = emp3f*4

scenario1 = emp1to1f + emp2to1f + emp3to1f
scenario2 = emp1to2f + emp2to2f + emp3to2f
scenario3 = emp1to3f + emp2to3f + emp3to3f

scenarios = [scenario1, scenario2, scenario3]
minscenario = min(scenarios)

if minscenario == scenario1:
    machine += 1
elif minscenario == scenario2:
    machine += 2
elif minscenario == scenario3:
    machine +=3

print(minscenario)