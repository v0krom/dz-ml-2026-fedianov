def prod_non_zero_diag(X):
    result = 1

    for i in range(min(len(X), len(X[0]))):
        if X[i][i] != 0:
            result *= X[i][i]

    return result


def are_multisets_equal(x, y):
    return sorted(x) == sorted(y)


def max_after_zero(x):
    result = None

    for i in range(1, len(x)):
        if x[i - 1] == 0:
            if result is None or x[i] > result:
                result = x[i]

    return result


def convert_image(img, coefs):
    height = len(img)
    width = len(img[0])

    result = []

    for i in range(height):
        row = []

        for j in range(width):
            value = 0

            for k in range(len(coefs)):
                value += img[i][j][k] * coefs[k]

            row.append(value)

        result.append(row)

    return result


def run_length_encoding(x):
    values = [x[0]]
    counts = [1]

    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            counts[-1] += 1
        else:
            values.append(x[i])
            counts.append(1)

    return values, counts


def pairwise_distance(x, y):
    result = []

    for i in range(len(x)):
        row = []

        for j in range(len(y)):
            distance = 0

            for k in range(len(x[i])):
                distance += (x[i][k] - y[j][k]) ** 2

            row.append(distance ** 0.5)

        result.append(row)

    return result