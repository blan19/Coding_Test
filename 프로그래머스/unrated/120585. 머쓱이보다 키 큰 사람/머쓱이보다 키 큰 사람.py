def solution(array, height):
    return len([people for people in array if people > height])