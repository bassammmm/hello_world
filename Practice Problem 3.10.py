print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignent #1")
print("Practice Problem 3.10")

def noVowel(s):
    for x in s:
        if x in ("a","e","i","o","u","A","E","I","U"):
            print("False")
            break
            
    else:
        print("True")

user_string = input("\n\nPlease enter a word:")
noVowel(user_string)
