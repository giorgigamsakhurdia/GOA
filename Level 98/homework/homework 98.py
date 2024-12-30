def get_unique_elements(matrix):
    unique_elements = set()
    for row in matrix:
        for element in row:
            unique_elements.add(element)
    return list(unique_elements)


#2

#ver gavige