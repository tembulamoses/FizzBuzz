def fizz_buzz(n):

    # a number divisible by both is logically divissible by both
    # hence 15
    if n is None:
        return "please enter a whole number"
    if isinstance(n, int):
        if n%15 == 0:
            # Divisible by both 3 and 5
            return 'FizzBuzz'

        elif n % 3 == 0:
            # Divisible by 3
            return 'Fizz'

        elif n % 5 == 0:
            # Divisible by 5
            return 'Buzz'

        else:
            # Not divisible by wither 5 or 5
            return n
    else:
        return "please enter a whole number"        