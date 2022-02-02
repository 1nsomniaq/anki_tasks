def urlify(arr, len_s):
    space_count = 0
    for i in range(len_s):
        if arr[i] == ' ':
            space_count += 1

    pointer = len_s - 1
    end_pointer = len(arr) - 1
    while pointer >= 0:
        if arr[pointer] == ' ':
            arr[end_pointer] = '0'
            arr[end_pointer-1] = '2'
            arr[end_pointer-2] = '%'
            end_pointer -= 3
        else:
            arr[end_pointer] = arr[pointer]
            end_pointer -= 1

        pointer -= 1

    return ''.join(arr)


print(urlify(list('df fg ghrt rr      '), 13))
