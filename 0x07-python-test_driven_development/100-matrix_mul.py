#!/usr/bin/python3


from unittest import result


def matrix_mul(m_a, m_b):


    if not isinstance((m_a), list):
        raise TypeError("m_a must be a list")
    if not isinstance((m_b), list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(x, list) for x in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(x, list) for x in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or all(len(x) == 0 for x in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(x) == 0 for x in m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(x, (float, int)) for sublist in m_a for x in sublist):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (float, int)) for sublist in m_b for x in sublist):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[x]) == len(m_a[x + 1]) for x in range(len(m_a) - 1)):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[x]) == len(m_b[x + 1]) for x in range(len(m_b) - 1)):
        raise TypeError("each row of m_b must be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for sub_list in m_a:
        temp_list =[]
        for i in range(len(m_b[0])):
            temp = 0
            for j in range(len(sub_list)):
                temp += sub_list[j] * m_b[j][i]
            temp_list.append(temp)
        result.append(temp_list)
    return (result)
