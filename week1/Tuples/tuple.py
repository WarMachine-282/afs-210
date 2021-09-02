from collections import defaultdict

classes = (("VII", 1), ("V", 1), ("V", 2), ("VI", 1), ("VI", 2), ("VI", 3))
numList = defaultdict(list)
for classList, classId in classes:
    numList[classList].append(classId)

print(numList)
