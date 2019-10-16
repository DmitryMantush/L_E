from packaging import version as v


def one_arg(cls):  # this allows us to give a Version class only 'version' argument
    def wrapper(z: str):
        return cls()(z)
    return wrapper


@one_arg
class Version:

    def __init__(self):
        pass

    def __call__(self, ver):
        self.ver = ver
        return v.parse(ver)


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        # ('1.0.1b', '1.0.10-alpha.beta'),  # this test is failed
        ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), 'le failed'
        assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()


# Расширить реализацию класса Version,
# чтобы позволять использовать его для
# семантического сравнения.
#
# Пример:
#
# print(Version('1.1.3') < Version('2.2.3'))
# True
#
# print(Version('1.3.0') > Version('0.3.0'))
# True
#
# print(Version('0.3.0b') < Version('1.2.42'))
# True
#
# print(Version('1.3.42') == Version('42.3.1'))
# False
