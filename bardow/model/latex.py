from sympy import latex


# TODO: Define a custom printer that sets
# inv_trig_style='full'
# ln_notation=True
# mat_symbol_style='bold'
# mat_delim="("
#
# then also separates scalars, unknowns and units.
# e.g.: (250pi/2)*(p/V)*(kg*m/s**2)
#
# optionally finally replaces base units with derived units if it shortens the
# representation
# e.g. (250pi/2)*(p/V)*(N)


def my_latex(*args, **kwargs) -> str:
    return latex(*args, **kwargs)
