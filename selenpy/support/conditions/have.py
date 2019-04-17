from selenpy.helper import conditions

# *** WebDriver conditions ***


def title(exact_value):
    return conditions.Title(exact_value)

