from toqito.helper.constants import e0, e1
from toqito.states.is_mixed import is_mixed

import unittest


class TestIsMixed(unittest.TestCase):
    """Unit test for is_mixed."""

    def test_is_mixed(self):
        rho = 3/4*e0*e0.conj().T + 1/4*e1*e1.conj().T
        self.assertEqual(is_mixed(rho), True)


if __name__ == '__main__':
    unittest.main()