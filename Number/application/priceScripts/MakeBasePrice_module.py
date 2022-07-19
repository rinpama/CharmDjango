def func(data, data2, wagesUp, partsUp, *args, **kwargs):
    X = int(data.SM)
    Y = int(data.SM)
    Z = int(partsUp)
    A = int(data2.ceiling300)
    B = int(data2.ceiling300)
    C = int(wagesUp)

    keiten = X + Y * Z - 100 + A + B * C - 100
    majikiri = X * 100 + Y * 300

    answer = {
        'keiten': keiten,
        'majikiri': majikiri,
    }
    return answer


if __name__ == "__main__":
    func()
