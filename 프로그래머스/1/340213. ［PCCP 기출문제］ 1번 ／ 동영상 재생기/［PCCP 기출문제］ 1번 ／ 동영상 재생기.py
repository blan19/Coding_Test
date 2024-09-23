from datetime import datetime, timedelta

def solution(video_len, pos, op_start, op_end, commands):
    for command in commands:
        if isOp(pos, op_start, op_end):
                pos = op_end
                
        if isStart(pos, command):
            pos = "00:00"
        elif isEnd(pos, video_len, command):
            pos = video_len
        else:
            new_pos = datetime.strptime(pos, "%M:%S") + timedelta(seconds=10) if command == "next" else datetime.strptime(pos, "%M:%S") + timedelta(seconds=-10)
            pos = new_pos.strftime("%M:%S")
            if isOp(pos, op_start, op_end):
                pos = op_end
        print(pos)
    return pos

def isStart(pos, command):
    if command == "prev" and datetime.strptime(pos, "%M:%S") < datetime.strptime("00:10", "%M:%S"):
        return True
    return False

def isEnd(pos, video_len, command):
    if command == "next" and datetime.strptime(pos, "%M:%S") + timedelta(seconds=10) > datetime.strptime(video_len, "%M:%S"):
        return True
    return False

def isOp(pos, op_start, op_end):
    if datetime.strptime(op_start, "%M:%S") <= datetime.strptime(pos, "%M:%S") <= datetime.strptime(op_end, "%M:%S"):
        return True
    return False