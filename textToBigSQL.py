import matplotlib # type: ignore
import matplotlib.pyplot as plt # type: ignore

# ground truth, result, T_gold, T_e2e, cost
data0 = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 30, 45, 10),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], 30, 45, 15),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4], 30, 45, 12)
]

data1 = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 30, 45, 10),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], 30, 45, 15),
    ([6, 7, 8], [6, 7, 8, 9, 10, 11], 25, 50, 12),
    ([2, 3, 5, 7], [2, 3, 5, 7, 11], 70, 85, 10),
    ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9, 11, 13, 15, 17], 200, 300, 30),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4], 30, 45, 12)
]

data2 = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 30, 45, 100),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], 30, 45, 150),
    ([6, 7, 8], [6, 7, 8, 9, 10, 11], 25, 50, 80),
    ([2, 3, 5, 7], [2, 3, 5, 7, 11], 70, 85, 150),
    ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9, 11, 13, 15, 17], 200, 300, 300),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4], 30, 45, 125)
]

def I(col1, col2):
    if col1 == col2:
        return 1
    else:
        return 0

def II(col1, col2):    # ordering is not checked here
    for i in col1:
        if i in col2:
            continue
        else:
            return 0
    return 1

def P(col1, col2):    # result is only used when col1 is a subset of col2
    return len(col1) / len(col2)

def ves(data):
    totalSum = 0
    N = len(data)
    for result in data:
        groundTruth = result[0]
        resultCol = result[1]
        T_gold = result[2]
        T_e2e = result[3]
        totalSum += I(groundTruth, resultCol) * (T_gold / T_e2e)
    return (1 / N) * totalSum

def vesStar(data):
    totalSum = 0
    N = len(data)
    for result in data:
        groundTruth = result[0]
        resultCol = result[1]
        T_gold = result[2]
        T_e2e = result[3]
        totalSum += II(groundTruth, resultCol) * P(groundTruth, resultCol) * (T_gold / T_e2e)
    return (1 / N) * totalSum

def vces(data):
    totalSum = 0
    N = len(data)
    for result in data:
        groundTruth = result[0]
        resultCol = result[1]
        T_gold = result[2]
        T_e2e = result[3]
        cost = result[4]
        totalSum += (II(groundTruth, resultCol) * P(groundTruth, resultCol) * (T_gold / T_e2e)) / cost
    return (1 / N) * totalSum

print("First Data:")
print(" VES = %.3f" % ves(data0))
print(" VES* = %.3f" % vesStar(data0))
print(" VCES = %.3f\n" % vces(data0))
print("Increase Partially Correct Columns:")
print(" VES = %.3f" % ves(data1))
print(" VES* = %.3f" % vesStar(data1))
print(" VCES = %.3f\n" % vces(data1))
print("Increase Costs")
print(" VES = %.3f" % ves(data2))
print(" VES* = %.3f" % vesStar(data2))
print(" VCES = %.3f\n" % vces(data2))


plt.xlabel("data")
plt.ylabel("score")
plt.axis("off")
plt.suptitle("First Data -> Increase Partially Correct Columns -> Increase Costs")

plt.subplot(1, 3, 1)
plt.plot([ves(data0), ves(data1), ves(data2)])
plt.title("VES")

plt.subplot(1, 3, 2)
plt.plot([vesStar(data0), vesStar(data1), vesStar(data2)], color = "green")
plt.title("VES*")

plt.subplot(1, 3, 3)
plt.plot([vces(data0), vces(data1), vces(data2)], color = "red")
plt.title("VCES")

plt.tight_layout()
plt.show()