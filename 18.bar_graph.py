import matplotlib.pyplot as pyplot

labels = ("Python", "Java", "C", "JavaScript", "PHP")
index = (1, 2, 3, 4, 5)  #provides the locatipon on X axis
sizes = [55, 10, 30, 15, 22]

# barchat setup
pyplot.bar(index, sizes, label=labels)

#x and y layout
pyplot.ylabel("Usage")
pyplot.xlabel("Programming Language")

# display the graph
pyplot.show()
