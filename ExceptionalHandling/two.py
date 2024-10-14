
import three

def add(a,b):
    try:
        print("inside two")
        return three.realAddition(a,b, 100)
    except Exception as e:
        print(e)
        return False