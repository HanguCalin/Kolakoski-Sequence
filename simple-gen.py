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

if __name__ == "__main__":
    n = int(input())
    kolakoski_sequence = generate_kolakoski(n)

    with open("output.txt", "w") as file:
        line_length = 100
        for i in range(0, len(kolakoski_sequence), line_length):
            file.write(" ".join(map(str, kolakoski_sequence[i:i + line_length])) + "\n")

