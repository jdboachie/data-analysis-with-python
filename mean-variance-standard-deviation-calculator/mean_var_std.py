import numpy as np


def calculate(list):
    try:
        list = np.array(list).reshape(3, 3)
    except Exception:
        raise ValueError("List must contain nine numbers.")

    calculations = {}

    ax_1_avg = np.mean(list, axis=0)
    ax_2_avg = np.mean(list, axis=1)

    calculations['mean'] = [
        ax_1_avg.tolist(),
        ax_2_avg.tolist(),
        np.mean(list)
    ]

    ax_1_var = np.var(list, axis=0)
    ax_2_var = np.var(list, axis=1)

    calculations['variance'] = [
        ax_1_var.tolist(),
        ax_2_var.tolist(),
        np.var(list)
    ]

    ax_1_stdev = np.std(list, axis=0)
    ax_2_stdev = np.std(list, axis=1)

    calculations['standard deviation'] = [
        ax_1_stdev.tolist(),
        ax_2_stdev.tolist(),
        np.std(list)
    ]

    ax_1_max = np.max(list, axis=0)
    ax_2_max = np.max(list, axis=1)

    calculations['max'] = [
        ax_1_max.tolist(),
        ax_2_max.tolist(),
        np.max(list)
    ]

    ax_1_min = np.min(list, axis=0)
    ax_2_min = np.min(list, axis=1)

    calculations['min'] = [
        ax_1_min.tolist(),
        ax_2_min.tolist(),
        np.min(list)
    ]

    ax_1_sum = np.sum(list, axis=0)
    ax_2_sum = np.sum(list, axis=1)

    calculations['sum'] = [
        ax_1_sum.tolist(),
        ax_2_sum.tolist(),
        np.sum(list)
    ]

    return calculations
