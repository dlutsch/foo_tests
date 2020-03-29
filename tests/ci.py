import ef_tests
import global_vars


def check_errors():
    for k, v in global_vars.errors.items():
        print(f"> error in file: {k}")
        print(v)

    assert not global_vars.errors


if __name__ == '__main__':

    ef_tests.validate_yaml()
    ef_tests.validate_json()

    check_errors()