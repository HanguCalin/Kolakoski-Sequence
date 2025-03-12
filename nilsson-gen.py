def generate_kolakoski_nilsson(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]

    arr = [1, 2, 2]
    i, j = 3, 2

    while i < n:
        repeat = arr[j]
        value = 3 - arr[-1]

        for _ in range(repeat):
            if i >= n:
                break
            arr.append(value)
            i += 1
            
        j += 1

    return arr

if __name__ == "__main__":
    n = int(input())
    kolakoski_sequence = generate_kolakoski_nilsson(n)

    with open("output.txt", "w") as file:
        line_length = 100
        for i in range(0, len(kolakoski_sequence), line_length):
            file.write(" ".join(map(str, kolakoski_sequence[i:i + line_length])) + "\n")

