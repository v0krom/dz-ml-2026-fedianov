import numpy as np


def prod_non_zero_diag(X):
    diag = np.diag(X)
    return np.prod(diag[diag != 0])


def are_multisets_equal(x, y):
    return np.array_equal(np.sort(x), np.sort(y))


def max_after_zero(x):
    return np.max(x[1:][x[:-1] == 0])


def convert_image(img, coefs):
    return np.sum(img * coefs, axis=2)


def run_length_encoding(x):
    change_indices = np.where(x[1:] != x[:-1])[0] + 1

    starts = np.concatenate(([0], change_indices))
    ends = np.concatenate((change_indices, [len(x)]))

    values = x[starts]
    counts = ends - starts

    return values, counts


def pairwise_distance(x, y):
    return np.sqrt(
        np.sum(
            (x[:, np.newaxis, :] - y[np.newaxis, :, :]) ** 2,
            axis=2
        )
    )
