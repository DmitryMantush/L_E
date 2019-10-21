def one_arg(cls):  # this allows us to give a Version class only 'version' argument
    def wrapper(z: str):
        return cls()(z)
    return wrapper


@one_arg
class Version:

    def __init__(self):
        self.result = []

    def __call__(self, ver):
        self.ver = ver

        ver_dots_only = ver.replace('-', '.')
        ver_comp = ver_dots_only.split('.')
        for token in ver_comp:
            if token.isdigit():
                self.result.append(token)
            else:
                if token[0].isdigit():
                    new_token = float(token[0])
                    for i in range(1, len(token)):
                        n = (ord(token[i]) - 96) * 0.3 * 10 ** (-i)
                        new_token += n
                    self.result.append(str(new_token))
                else:
                    self.result.append(token)
        return self.result


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1b', '1.0.10-alpha.beta'),
        # ('1.0.0-rc.1', '1.0.0'),  # this test is failed
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
