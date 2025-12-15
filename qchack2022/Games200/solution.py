#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


dev = qml.device("default.qubit", wires=2)


def prepare_entangled(alpha, beta):
    """Construct a circuit that prepares the (not necessarily maximally) entangled state in terms of alpha and beta
    Do not forget to normalize.

    Args:
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>
    """

    # QHACK #
    
    # firstly we have to normalize the values by using a normalizing factor
    
    normalizing_factor = np.sqrt(alpha**2 + beta**2) 
    
    if normalizing_factor == 0:
        return  # leave |00>

    ratio = np.clip(alpha/normalizing_factor, -1.0, 1.0)
    theta = 2*np.arccos(ratio)
    
    
    # now we can start preparing the quantum state
    
    qml.RY(theta, wires=0)
    qml.CNOT(wires=[0, 1])
    
    
    # QHACK #

@qml.qnode(dev)
def chsh_circuit(theta_A0, theta_A1, theta_B0, theta_B1, x, y, alpha, beta):
    """Construct a circuit that implements Alice's and Bob's measurements in the rotated bases

    Args:
        - theta_A0 (float): angle that Alice chooses when she receives x=0
        - theta_A1 (float): angle that Alice chooses when she receives x=1
        - theta_B0 (float): angle that Bob chooses when he receives x=0
        - theta_B1 (float): angle that Bob chooses when he receives x=1
        - x (int): bit received by Alice
        - y (int): bit received by Bob
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (np.tensor): Probabilities of each basis state
    """

    prepare_entangled(alpha, beta)

    # QHACK #
    
    # we can use a trick that instead of rotating of the device + theta we can rotate the qubit -theta*2 (here 2 is because we need to rotate the angle by theta not theta/2)

    # for alice
    if x == 0:
        qml.RY(-theta_A0*2, wires = 0)
    else:
        qml.RY(-theta_A1*2, wires = 0)
        
    # for bob
    if y == 0:
        qml.RY(-theta_B0*2, wires = 1)
    else:
        qml.RY(-theta_B1*2, wires = 1)
    
    # QHACK #

    return qml.probs(wires=[0, 1])
    

def winning_prob(params, alpha, beta):
    """Define a function that returns the probability of Alice and Bob winning the game.

    Args:
        - params (list(float)): List containing [theta_A0,theta_A1,theta_B0,theta_B1]
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (float): Probability of winning the game
    """

    # QHACK #
    
    # now we need to call the chsh circuit function for each pair of (x, y) to get the probability vector of that particular input bits
    
    # now we need to calculate the winning probability that is sum of all the winning probability cases
    
    # the chsh circuit function return us a prob vector looks like 
    # [P(00), P(01), P(10), P(11)].
    
    # what i initially wrote:
    
    # prob_00 = chsh_circuit(params[0], params[1], params[2], params[3], 0, 0, alpha, beta)
    # prob_01 = chsh_circuit(params[0], params[1], params[2], params[3], 0, 1, alpha, beta)
    # prob_10 = chsh_circuit(params[0], params[1], params[2], params[3], 1, 0, alpha, beta)
    # prob_11 = chsh_circuit(params[0], params[1], params[2], params[3], 1, 1, alpha, beta)
    
    # prob_win_00 = prob_00[0] + prob_00[3]
    # prob_win_01 = prob_01[0] + prob_01[3]
    # prob_win_10 = prob_10[0] + prob_10[3]
    # prob_win_11 = prob_11[1] + prob_11[2]
    
    # prob_win = (prob_win_00 + prob_win_01 + prob_win_10 + prob_win_11)/4    

    # when i try to optimize it i get the better and more concise approach

    
    total = 0.0
    
    for x in (0, 1):
        for y in (0, 1):
            probs = chsh_circuit(params[0], params[1], params[2], params[3], x, y, alpha, beta)

            if x * y == 0:# a == b
                total += probs[0] + probs[3]  
            else:# a != b
                total += probs[1] + probs[2]  
                
    return total / 4.0

    # QHACK #
    

def optimize(alpha, beta):
    """Define a function that optimizes theta_A0, theta_A1, theta_B0, theta_B1 to maximize the probability of winning the game

    Args:
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (float): Probability of winning
    """

    def cost(params):
        """Define a cost function that only depends on params, given alpha and beta fixed"""
        # optimizers are to minimize a value but here we have to mazimize so we return its negative
        return -1* winning_prob(params, alpha, beta)

    # QHACK #

    #Initialize parameters, choose an optimization method and number of steps
    init_params = np.array([0, np.pi/4, np.pi/8, -np.pi/8], requires_grad = True) # initializing with the standard bell state values
    opt = qml.GradientDescentOptimizer(stepsize= 0.1)
    steps = 100


    # QHACK #
    
    # set the initial parameter values
    params = init_params

    for i in range(steps):
        # update the circuit parameters 
        # QHACK #

        params = opt.step(cost, params)
        params = params % (2*np.pi)

        # QHACK #

    return winning_prob(params, alpha, beta)


if __name__ == '__main__':
    inputs = sys.stdin.read().split(",")
    output = optimize(float(inputs[0]), float(inputs[1]))
    print(f"{output}")