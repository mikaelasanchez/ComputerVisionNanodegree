import math
import torch


def sigmoid(x):
    return 1/(1 + math.e ** -x)


def softmax(x):
    return torch.exp(x) / torch.sum(torch.exp(x), dim=1).view(-1, 1)


def perceptron_prob(w1, w2, b):
    return sigmoid(w1*0.4 + w2*0.6 + b)


print(perceptron_prob(2, 6, -2))
print(perceptron_prob(3, 5, -2.2))
print(perceptron_prob(5, 4, -3))

# Feed forward
# x = (x1, x2), y = 1
#
# w1x1 + w2x2 + b


def ln(x):
    return math.log(x, math.e)


def mean_squared_error(predicted, real):
    result = 0
    for i in range(len(real)):
        result += (real[i] - predicted[i])**2
    return result/len(real)


predictions = [4, 5, 6, 7, 8]
real_values = [3, 4, 7, 7, 7]

print(mean_squared_error(predictions, real_values))
