def entrance_fee(ages) -> int:
    """
    Calculates the admission fee for the amusement park.

    parameters:
        ages :List of Ages
    returns:
        int: The total calculated entry fee.
    """

    kid, adult, senior = 5000, 10000, 7000

    total_fee = 0

    for age in ages:
        if age >= 65:
            total_fee = total_fee + senior
        elif age >= 19:
            total_fee = total_fee + adult
        else:
            total_fee = total_fee + kid

    return total_fee