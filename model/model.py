import numpy
import os

NODES_NUM = 10;

def generate_states():
    states = []

    for i in range(0, NODES_NUM):
        if i == 0:
            # initial state
            states.append([0, 0, True])
        elif i == 1:
            # 1st row
            for j in range(0, NODES_NUM):
                states.append([i, j, True])
            # 3rd column
            for j in range(0, NODES_NUM):
                states.append([i, j, False])
        else:
            # remaining matrix
            for j in range(0, NODES_NUM - i + 1):
                states.append([i, j, False])

    return states

def get_state(states, state):
    if state in states:
        return states.index(state)
    else:
        return -1

def compute_send_rate(item, rate):
    return (NODES_NUM - (item[0] + item[1])) * rate

def compute_receive_rate(item, rate):
    return item[0] * rate

def generate_matrix(states, send_rate, receive_rate):
    matrix = numpy.zeros((len(states), len(states)))

    for index, item in enumerate(states):
        if item == [0, 0, True]:
            matrix[0][1] = compute_send_rate([0, 0], send_rate)
        elif item[0] == 1:
            next_state = [1, item[1] + 1, item[2]]
            pos = get_state(states, next_state)
            if pos != -1:
                matrix[index][pos] = compute_send_rate(item, send_rate)

            if item[1] == 0 or item[1] == 1:
                prev_state = [item[1], 0, True]
            else:
                prev_state = [item[1], 0, False]
            pos = get_state(states, prev_state)
            if pos != -1:
                matrix[index][pos] = compute_receive_rate(item, receive_rate)
        else:
            next_state = [item[0], item[1] + 1, False]
            pos = get_state(states, next_state)
            if pos != -1:
                matrix[index][pos] = compute_send_rate(item, send_rate)

            prev_state = [item[0] - 1, item[1], False]
            pos = get_state(states, prev_state)
            if pos != -1:
                matrix[index][pos] = compute_receive_rate(item, receive_rate)

    for i in range(0, len(matrix)):
        matrix[i][i] = -sum(matrix[i])

    return matrix

def init_file():
    path = "./data/model.csv"
    file = open(path, "w+")
    file.write("state,prob,load\n")
    file.close()

def append_file(steady_state, states, scale):
    path = "./data/model.csv"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as file:
        for index, prob in enumerate(steady_state[1:]):
            state = states[index]
            if prob < 0:
                prob = 0
            if state[2]:
                val = "t"
            else:
                val = "c"
                prob = prob*state[0]
            file.write("{},{},{}\n".format(val, prob, ((6914 - 32) / 2) / (1.314*scale)))

init_file()

states = generate_states()
states_num = len(states)

for scale in range(3, 100, 1):
    scale = scale/1000

    LAMBDA = 1.314*scale
    MU = 1 #1000000 / ((6914 - 32) / 2)

    transition_matrix = generate_matrix(states, LAMBDA, MU)
    Q = numpy.ones((states_num, states_num + 1))
    Q[:,:-1] = transition_matrix

    zeroes = [0] * states_num
    zeroes.append(1)

    steadystate_matrix = numpy.linalg.lstsq(Q.transpose(), zeroes, rcond=None)

    dot = numpy.dot(steadystate_matrix[0], transition_matrix)
    error_matrix = numpy.isclose(a=dot, b=numpy.zeros((states_num, states_num)))

    append_file(steadystate_matrix[0], states, scale)

    print("[ STEP ] "+str(scale)+" "+str(numpy.all(error_matrix)))
