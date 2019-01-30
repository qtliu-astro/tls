import numpy
from transitleastsquares import FAP

if __name__ == "__main__":
    print("Starting test FAP...", end='')
    numpy.testing.assert_equal(FAP(SDE=2), numpy.nan)
    numpy.testing.assert_equal(FAP(SDE=7), 0.009443778)
    numpy.testing.assert_equal(FAP(SDE=99), 8.0032e-05)
    print("passed")
