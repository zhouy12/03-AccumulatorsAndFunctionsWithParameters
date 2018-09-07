"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Michelle.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_powers()
    run_test_sum_powers_in_range()


def run_test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')
    # Test 1:
    expected = 1 ** (-0.3) + 2 ** (-0.3) + 3 ** (-0.3) + 4 ** (-0.3) + 5 ** (-0.3)
    actual = sum_powers(5, -0.3)
    print('test 1 expects:', expected)
    print('        actual:', actual)

    # Test 2:
    expected = 1 ** 9 + 2 ** 9 + 3 ** 9 + 4 ** 9
    actual = sum_powers(4, 9)
    print('test 2 expects:', expected)
    print('        actual:', actual)

    # Test 3:
    expected = 1 ** 20 + 2 ** 20 + 3 ** 20
    actual = sum_powers(3, 20)
    print('test 3 expects:', expected)
    print('        actual:', actual)

def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    total = 0
    for k in range(n):
        total = total+(k+1)**p
    return total
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------



def run_test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')
    # Test 1:
    expected = 2 ** 4 + 3 ** 4
    actual = sum_powers_in_range(2, 3, 4)
    print('test 1 expects:', expected)
    print('        actual:', actual)

    # Test 2:
    expected = 3 ** 5 + 4 ** 5
    actual = sum_powers_in_range(3, 4, 5)
    print('test 2 expects:', expected)
    print('        actual:', actual)

    # Test 3:
    expected = 4 ** 6 + 5 ** 6
    actual = sum_powers_in_range(4, 5, 6)
    print('test 3 expects:', expected)
    print('        actual:', actual)


def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """
    total = 0
    for k in range(n - m + 1):
        total = total + (m + k) ** p
    return total
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
