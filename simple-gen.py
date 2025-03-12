def generate_kolakoski(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]

    arr = [1, 2, 2]
    i = 2
    current_value = 1

    while len(arr) < n:
        run_length = arr[i]
        arr.extend([current_value] * run_length)
        current_value = 3 - current_value
        i += 1

    return arr[:n]

if __name__ == "__main__":
    n = int(input())
    kolakoski_sequence = generate_kolakoski(n)

    with open("output.txt", "w") as file:
        line_length = 100
        for i in range(0, len(kolakoski_sequence), line_length):
            file.write(" ".join(map(str, kolakoski_sequence[i:i + line_length])) + "\n")

