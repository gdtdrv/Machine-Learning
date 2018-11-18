accuracy = 0
tp = 0
tn = 0
fp = 0
fn = 0

# reading the train data
traindata = []
myReadFile = open("Train.txt", "r")
while True:
    theline = myReadFile.readline()
    if len(theline) == 0:
        break
    data = theline.split(",")
    for pos in range(len(data)):
        data[pos] = float(data[pos])
    traindata.append(data)
myReadFile.close()

# reading the test data
testdata = []
myReadFile2 = open("Test.txt", "r")
while True:
    theline = myReadFile2.readline()
    if len(theline) == 0:
        break
    data = theline.split(",")
    for pos in range(len(data)):
        data[pos] = float(data[pos])
    testdata.append(data)
myReadFile2.close()

# separating the x and the y for the training set
x_train = []
y_train = []

print(len(traindata[0]))

for i in range(0, len(traindata)):
    x_train.append(traindata[i][:-1])
    y_train.append(traindata[i][-1])

# separating x and y for the testing set
x_test = []
y_test = []

for i in range(0, len(testdata)):
    x_test.append(testdata[i][:-1])
    y_test.append(testdata[i][-1])

print(len(x_train))
print(len(y_train))

# create a list, which contains all of the distances
# find the distances
for testrow in range(0, len(testdata)):  # go through all of the data in the testing set
    distances = []
    for trainrow in range(0, len(traindata)):
        sum_eachdistance = 0
        eachdistance = 0
        for index in range(0, len(traindata[trainrow])-1):  # go compare it to all of the data in the training set
            eachdistance = (x_train[trainrow][index] - x_test[testrow][index]) ** 2
            sum_eachdistance = sum_eachdistance + eachdistance
        distances.append((sum_eachdistance) ** 0.5)
        n = distances.index(min(distances))

    if (y_test[testrow] == y_train[n]):
        accuracy = accuracy + 1
        if (y_test[testrow] == 2):
            tp = tp + 1
        else:
            tn = tn + 1
    else:
        if (y_test[testrow] == 2):
            fp = fp + 1
        else:
            fn = fn + 1

precision = tp / (tp + fp)
recall = tp / (tp + fn)




