import matplotlib.pyplot as pyplot
labels = ("Python", "Java", "C", "JavaScript", )
sizes = [40, 25, 20, 15]

pyplot.pie(sizes, labels=labels, autopct= '%1.f%%', counterclock=False, startangle=105)
#to display the figure
pyplot.show