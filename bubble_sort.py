def bubble_sort(number):
    for i in range(len(number)-1, -1, -1):
        for j in range(i):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
                print(number)
                
bubble_sort([99,50,20,55,1,0,5])