# Basic package test

from plotter import Plotter


def main():
    """
    Tests importing of package
    """

    print("Test complete.")
    return True


def test_import():
    assert main() is True


if __name__ == '__main__':
    main()

