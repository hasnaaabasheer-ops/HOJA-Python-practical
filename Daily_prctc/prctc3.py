def find_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers)
    return average

marks = [75, 80, 90, 85, 70 ,99]
avg = find_average(marks)

if avg > 70:
    print("Excellent")
else:
    print("Keep Improving")

    print("Average:", avg)