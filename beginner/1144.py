n = int(input())
i = 1
while n > 0:
    line_1 = {
        "first": i,
        "second": i * i,
        "third": i * i * i
    }

    line_2 = {
        "first": i,
        "second": line_1["second"] + 1,
        "third": line_1["third"] + 1
    }

    i = i + 1
    n = n - 1

    print(line_1["first"], line_1["second"], line_1["third"])

    print(line_2["first"], line_2["second"], line_2["third"])
    