def convert_cel_to_far():
    cel = int(input("Enter a temperature in degrees F: "))
    far= (cel *9/5) +32
    print(cel, "C degrees F = ", far)

def convert_far_to_cel():
    far1 = int(input("Enter a temperature in degrees C: "))
    cel1 = (far1-32)*5/9
    print(far1, " F degrees C = ", cel1)

convert_cel_to_far()
convert_far_to_cel()
