days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

кількість_секунд = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
print("кількість секунд:", кількість_секунд)
