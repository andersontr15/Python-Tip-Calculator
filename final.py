#Tip calculator and total bill calculator; modus operand (10-20%)
#10% = mediocre service, 15% good service, 20% great service
#tip accordingly
# Created by Theodore Anderson

print """Hello, welcome to Theo's calculator for calculating tips and meal totals
Please feel at ease while we aid you with your calculations."""


meal = input("How much was your meal?:")

ok = 0.10
good = 0.15
great = 0.20

import time
time.sleep(3)

quality_of_service = raw_input("Was your service ok, good, or great?:")

if quality_of_service == 'ok':
    print "you should tip %ok:" %(ok*meal)
if quality_of_service == 'good':
    print "you should tip %s:" %(good*meal)
if quality_of_service == 'great':
    print "you should tip %s:" % (great*meal)



print """Thank you for using Theo's tip calculator. 
		We hope you are satisfied with our service"""


