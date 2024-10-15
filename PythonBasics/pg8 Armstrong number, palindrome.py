
lower = int(input("Enter lower value: "))
higher = int(input("Enter higher value: "))

for num in range(lower,higher+1):

        temp = num
        ord = len(str(num))
        sum = 0
        while temp > 0:
            r = temp%10
            sum += pow(r,ord)
            temp //= 10  # //= returns integer value    /= returns float value
        if(num==sum):
            print(num)

