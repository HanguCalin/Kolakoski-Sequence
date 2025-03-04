def generate_kolakoski(n):
    arr = [0] * n
    arr[0], arr[1], arr[2] = 1, 2, 2

    i, length, curr = 2, 3, 1

    while length < n:
        run_length = arr[i]
        i += 1
        curr = 3 - curr

        for _ in range(run_length):
            if length < n:
                arr[length] = curr
                length += 1

    return arr

n = int(input())
sequence = generate_kolakoski(n)

with open("output.txt", "w") as file:
    line_length = 50
    for i in range(0, len(sequence), line_length):
        file.write(" ".join(map(str, sequence[i:i + line_length])) + "\n")