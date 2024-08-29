#in a school fest three randomly choosen students out of 100 students( having roll no. 1 to 100 ) have to present bouquets to guest  help the school authorities choose three students randomly
import random

student1, student2, student3 = random.sample(range(1,100), 3)
print('Roll nos:', student1, student2, student3)
