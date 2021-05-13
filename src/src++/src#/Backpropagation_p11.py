"""
The ReLU is the most popular and commonly used activation function. It can be represented as –

f(x) = max(0, x)

It takes a real value as input. The output is x, when x > 0 and is 0, when x < 0. It is mostly preferred over sigmoid and tanh.

Advantages >>>>>>>>>>>>>>>>>>

Accelerates the convergence of SGD compared to sigmoid and tanh(around 6 times).
No expensive operations are required.

Disadvantages >>>>>>>>>>>>>>>

It is fragile and might die during training. If the learning rate is too high the weights may change to a value that causes the neuron to not get updated at any data point again.
"""
# Debating against the ReLU and the Leaky ReLU

# There are some interesting complications to the ReLU when it comes to optimizing weights and biases
# for ReLU...
# >>> IF the weigth and the bias are both = to 0 then the ReLU on a graph will be a straight line. The input can be 4 million but it doenst matter because the biases and the weights prevent it.
# >>>> If the weight is above 0 and the bias remains equal to 0, the steepness of the line on the graph will change. But the bend will still start at 0 because our bias is 0.
# >>>>> Now if the weight remains the same (1.00) but we change the bias to be 0.50 then activation of the function will happen sooner.
"""
 >>>>>> With a negative weight and this single neuron, the function has become a question of when this
neuron deactivates. Up to this point, you’ve seen how we can use the bias to offset the function
horizontally, and the weight to influence the slope of the activation. Moreover, we’re also able to
control whether the function is one for determining where the neuron activates or deactivates.

^^^^^ THE ABOVE ARE ALL WITH JUST ONE NEURON WE WILL EXPLORE MULTI-DIMENSIONAL ReLU ACTIVATIONS NEXT.
"""
# WITH MULTI-DIMENSIONAL neurons is were the magic happens.

"""
Now we see some fairly interesting behavior. The bias of the second neuron indeed shifted the
overall function, but, rather than shifting it horizontally, it shifted the function vertically. What
then might happen if we make that 2nd neuron’s weight -2 rather than 1?

What we have here is a neuron that has both an activation and a
deactivation point. When both neurons are activated, when their “area of effect” comes into play,
they produce values in the range of the granular, variable, and output. If any neuron in the pair is
inactive, the pair will produce non-variable output:

"""

# WILL USE A SNIPPET OF THIS CODE in the P.5

# WHen we import something as a name we are calling it sum
# Capital x is just a common practice dw


# The Softmax activation function.
# We will use this for the output layer.
# The main reason we need another function for the output layer is we need osmehting to create a probability to that the Network can make a prediction.
# We can make a prediction maybe correctly whenusing the ReLU and when we ahve all positive values but when we have a negative value, Relu clips negatives to zero.
# SO both neurons are negative the network outputs are both zero. SO it cant be make a prediction.
# Hence we need a function whos equation doesnt clip the output to a zero.
# YAYYYY softmax.
#  \sigma(\vec{z})_{i}=\frac{e^{z_{i}}}{\sum_{j=1}^{K} e^{z_{j}}}
# We also expionetiate the function so we can mkae them non negative.
# Then we get a very high number, so then we "normalize" them (divide them) so we get a vector of small values.
# THEN WE ADD IT UP and get hte final number f that neuron.

"""
With a randomly-initialized model, or even a model initialized with more sophisticated
approaches, our goal is to train, or teach, a model over time. To train a model, we tweak the
weights and biases to improve the model’s accuracy and confidence. To do this, we calculate how
much error the model has. The loss function, also referred to as the cost function, is the
algorithm that quantifies how wrong a model is. Loss is the measure of this metric. Since loss is
the model’s error, we ideally want it to be 0.
"""
# Basically it talks to the Netowrk and it tells it how bad it did. Like a test score.
# The lower the loss funciton outputs the better our network did.

# Preferably we could clssify a (True, False) and then tell the network how correct he is (50% cux only true or false).
# We cant do that becasue we want the network to be confident in tis answer.
# As you can probably guess there are diffrebt types of Loss functions
# The softmax function outputs a probability distro so we need to Calculate loss with something that only comapres prob distros
# CATAGORIAL CROSS ENTROPY >>>>
# Why Categorical Cross Entropy >>> when introducing back propogation it becomes easier to change the values.
# Categories are like groups on types of data.
# One-Hot encoding>>>>>>
# Each output class(OT layer neuron) doesnt retrun a lable saying whatver you wnat to output, yet it will output an integer.

# One Hot encdoing BASICALLY HELPS US SEE WHICH NEURON IS "HOT" or WHICH NEURON IS ACTIVATED.
# A vector is created for each category classes. All of the numbers are zeroes unless the coressponding class number's index in the vector is the number "1".
"""

softmax_output = [[0.7, 0.1, 0.2],
                  [0.1, 0.5, 0.4],
                  [0.02, 0.9, 0.08]]
"""
"""
The first value, 0, in class_targets means the first softmax output distribution’s intended
prediction was the one at the 0th index of [0.7, 0.1, 0.2]; the model has a 0.7 confidence
score that this observation is a dog. This continues throughout the batch, where the intended target
of the 2nd softmax distribution, [0.1, 0.5, 0.4], was at an index of 1; the model only has a
0.5 confidence score that this is a cat — the model is less certain about this observation. In the
last sample, it’s also the 2nd index from the softmax distribution, a value of 0.9 in this case — a
pretty high confidence
"""

# Introducing Optimization
# Optimization is a way to adjust the weights and biases to get a better result and to get higher accuracy abnd lower cost function value

"""
Randomly changing and searching for optimal weights and biases did not prove fruitful for one
main reason: the number of possible combinations of weights and biases is infinite, and we need
something smarter than pure luck to achieve any success. Each weight and bias may also have
different degrees of influence on the loss — this influence depends on the parameters themselves
as well as on the current sample, which is an input to the first layer. These input values are then
multiplied by the weights, so the input data affects the neuron’s output and affects the impact that
the weights make on the loss. The same principle applies to the biases and parameters in the next
layers, taking the previous layer’s outputs as inputs. This means that the impact on the output
values depends on the parameters as well as the samples — which is why we are calculating the
loss value per each sample separately. Finally, the function of how a weight or bias impacts the
overall loss is not necessarily linear. In order to know how to adjust weights and biases, we first
need to understand their impact on the loss.
"""
"""
The derivatives that we’ve solved so far have been
cases where there is only one independent variable in the function — that is, the result depended
solely on, in our case, x. However, our neural network consists, for example, of neurons, which
have multiple inputs. Each input gets multiplied by the corresponding weight (a function of 2
parameters), and they get summed with the bias (a function of as many parameters as there are
inputs, plus one for a bias). As we’ll explain soon in detail, to learn the impact of all of the inputs,
weights, and biases to the neuron output and at the end of the loss function, we need to calculate
the derivative of each operation performed during the forward pass in the neuron and the whole
model. To do that and get answers, we’ll need to use the chain rule.
"""
# The Partial derivative is a calculation of how much impact a neuron has on a function output.
# Basically like the rate of change.

# Gradients are just a 1d array / Vector of the partial derivatives of an input.

# Chain rule: The forward pass through our model is a chain of functions similar to these examples. We are passing in samples, the data flows through all of the layers, and activation functions to form a CHAIN.

# Chain Rule is kind of like the transitive property.
# Suppose we are a collecting the heights and the weights of someone.
# >> They would have a graph with a slope of 2/1 == 2. (For every 1 unit increased in weight, 2 units are increased into height.)
# SUppose we have another graph collecting the weights and shoe size.
# >> They would have another graph with a slope of (1/4). (For every 1 unit increased in height, 1/4 units are increased into shoe size.))
# So these two graphs are corresponding.
# Weight can predict height and height can predict shoe size.
# So we if we want to determine the exact changes with respect to changes in weight....
# WE can take the derivative of the equation if shoe size.....
#==================== (dshoesize/dweight) = (dheight/dweight) x (dshoesize/dheight)
# The relationship above is called the chain rule.

# Its used to help create a form of multiple function outputs and multiply them for the final outcome.

#VERY IMPORTANT-------------

"""
Derivatives of a function f(x):
    - how fast f changes around x (slope)
    - will f increase or decrease if we increse x
    - https://www.youtube.com/watch?v=3p09AyD-eWI


"""

#=============BACKPROPAGATION(With Basic levels of Optimization)===============#
# SUppose the network we are wokring it isnt trained (obviously). 
# The network is supposes to recognize hand written images and We input a 2 but we get all sorts of wrong answers.
# We first find the loss of the network.
# Since we want the network to classify it as an image of a 2 but the output value of the "2" in the layer is low,....
# WE CAN NUDGE ALL THE weights AND BIASES UP FOR the "2" and nudge all the other neuron values down. And the the should be proportional to its size as well
#   (wrong answer: 6 ~ 0.9 >>> thsi should be nudged down more than the other ones because the network thinks this is the highest value.)

# WEIGHTS ONLY>>>>>
#   Once you go back you should retrace your steps to see which weights have the moist effect. And then you should change those.

# BIASES ONLY>>>>
#   Once you go back change the bias of the neuron in the prevoius layer that influences the Cost Function

# Basically you have a list of nudges to every neuron that you have to do.
# Then you recursivly apply the same properties to the first layer weights and biases.


# >>>>>>>>>>>>>> THE MAIN KEY IDEA IS THAT THIS WORKS FOR ONLY A 2 SO WE NEED TO DO THIS FOR ALL POSSIBLE OUTCOMES.
# Every SINGLE Training DATA needs to be back propagated.

import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
from nnfs.datasets import vertical_data
import numpy as np
import nnfs

nnfs.init()


# ================================================================ - main classes


class LayerThick:
    def __init__(self, n_inputs, n_neurons):
        # Basically we are intializing out Inputs and Weights
        # We want the shape too.
        # WHen a layer is created we need 2 things...
        # WHat is the size of the inputs and how many neurons we want in it.
        # >>>>>> n_inputs and N_neurons in the .randn function are the size of matric you wanna create
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        # we multiplieing the inputs and neurons by 0.1 because we want the values to be between 0 and 1
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs = inputs
        # This function makes the NN move <"FORWARD">:
        # Calculates the outputs from the function above.
        self.output = np.dot(inputs, self.weights) + self.biases
    # BACK PROP METHOD 
    def backward(self,dvalues):
        # Gradientiantial Parameters
        # >>> .T ====== IS TO KEEP IT TRANSPOSED
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        self.dinputs = np.dot(dvalues, self.weights.T)


class ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
        self.inputs = inputs
        # This is the ReLU
    # Backward pass
    def backward(self, dvalues):
        # Since we need to modify the original variable,
        # let's make a copy of the values first
        self.dinputs = dvalues.copy()
        # Zero gradient where input values were negative
        self.dinputs[self.inputs <= 0] = 0



class Softmax():
    def forward(self, inputs):
        #self.output = exp_values / np.sum(exp_values)
        # ALl of this would work with a just a 1D Vector yet it wont work with a Matrix/Batch because it will add every single number.
        # We need to specify what numbers columns to multiply...
        # We also need to divide it by the correct alinements so... 4
        # Plus the number can get too big and overflow.
        # We need to subtract the max value from the
        self.inputs = inputs
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
        
    def backward(self, dvalues):
        # Create uninitialized array
        self.dinputs = np.empty_like(dvalues)
        # Enumerate outputs and gradients
        for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
            # Flatten output array
            single_output = single_output.reshape(-1, 1)
            # Calculate Jacobian matrix of the output and
            jacobian_matrix = np.diagflat(single_output) - \
                np.dot(single_output, single_output.T)
            # Calculate sample-wise gradient
            # and add it to the array of sample gradients
            self.dinputs[index] = np.dot(jacobian_matrix,
                                        single_dvalues)

# Common loss class
class Loss:
    # Calculates the data and regularization losses
    # given model output and ground truth values
    def calculate(self, output, yn):
        # Calculate sample losses
        sample_losses = self.forward(output, y)
        # Calculate mean loss
        data_loss = np.mean(sample_losses)
        # Return loss
        return data_loss
        # Cross-entropy loss

#Loss_CategoricalCrossentropy


class CCE(Loss):
    # Forward pass
    def forward(self, y_pred, y_true):
        # Number of samples in a batch
        samples = len(y_pred)
        # Clip data to prevent division by 0
        # Clip both sides to not drag mean towards any value
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

    # Probabilities for target values -
        # only if categorical labels
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[
                range(samples),
                y_true
            ]
        # Mask values - only for one-hot encoded labels
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(
                y_pred_clipped * y_true,
                axis=1
            )
        # Losses
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods

    def backward(self, dvalues, y_true):
   # Number of samples
        samples = len(dvalues)
        # Number of labels in every sample
        # We'll use the first sample to count them
        labels = len(dvalues[0])
        # If labels are sparse, turn them into one-hot vector
        if len(y_true.shape) == 1:
            y_true = np.eye(labels)[y_true]
        # Calculate gradient
        self.dinputs = -y_true / dvalues
        # Normalize gradient
        self.dinputs = self.dinputs / samples
# Softmax classifier - combined Softmax activation
# and cross-entropy loss for faster backward step


class Softmax_CCE():

    # Creates activation and loss function objects
    def __init__(self):
        self.activation = Softmax()
        self.loss = CCE()

    # Forward pass
    def forward(self, inputs, y_true):
        # Output layer's activation function
        self.activation.forward(inputs)
        # Set the output
        self.output = self.activation.output
        # Calculate and return loss value
        return self.loss.calculate(self.output, y_true)

    # Backward pass

    def backward(self, dvalues, y_true):

        # Number of samples
        samples = len(dvalues)

        # If labels are one-hot encoded,
        # turn them into discrete values
        if len(y_true.shape) == 2:
            y_true = np.argmax(y_true, axis=1)

        # Copy so we can safely modify
        self.dinputs = dvalues.copy()
        # Calculate gradient
        self.dinputs[range(samples), y_true] -= 1
        # Normalize gradient
        self.dinputs = self.dinputs / samples


# Create dataset
X, y = spiral_data(samples=100, classes=3)

# Create Dense layer with 2 input features and 3 output values
dense1 = LayerThick(2, 3)

# Create ReLU activation (to be used with Dense layer):
activation1 = ReLU()

# Create second Dense layer with 3 input features (as we take output
# of previous layer here) and 3 output values (output values)
dense2 = LayerThick(3, 3)

# Create Softmax classifier's combined loss and activation
costfunc = Softmax_CCE()

# Perform a forward pass of our training data through this layer
dense1.forward(X)

# Perform a forward pass through activation function 
# takes the output of first dense layer here
activation1.forward(dense1.output)

# Perform a forward pass through second Dense layer
# takes outputs of activation function of first layer as inputs
dense2.forward(activation1.output)

# Perform a forward pass through the activation/loss function
# takes the output of second dense layer here and returns loss
loss = costfunc.forward(dense2.output, y)
# Let's see output of the first few samples:
print(costfunc.output[:5])

# Print loss value
print('loss:', loss)

# Calculate accuracy from output of activation2 and targets
# calculate values along first axis
predictions = np.argmax(costfunc.output, axis=1)
if len(y.shape) == 2:
    y = np.argmax(y, axis=1)
accuracy = np.mean(predictions == y)

# Print accuracy
print('acc:', accuracy)

# Backward pass
costfunc.backward(costfunc.output, y)
dense2.backward(costfunc.dinputs)
activation1.backward(dense2.dinputs)
dense1.backward(activation1.dinputs)

# Print gradients
print(dense1.dweights)
print(dense1.dbiases)
print(dense2.dweights)
print(dense2.dbiases)
