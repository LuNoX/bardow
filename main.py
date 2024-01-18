from sympy import solve, symbols, pi, Eq, latex
from sympy.physics.units.systems import SI
from sympy.physics.units import Quantity, length, mass
from sympy.physics.units import kilometer, meter, kilogram
from sympy.physics.units.util import quantity_simplify
from sympy.physics.units import convert_to

from sympy.physics.units import UnitSystem


def test() -> None:
    x = symbols("x")
    l = Quantity("l")
    SI.set_quantity_dimension(l, kilometer.dimension)
    SI.set_quantity_scale_factor(l, 2 * kilometer)
    r = Quantity("r")
    SI.set_quantity_dimension(r, length)
    SI.set_quantity_scale_factor(r, 4 * meter)
    m = Quantity("m")
    SI.set_quantity_dimension(m, mass)
    SI.set_quantity_scale_factor(m, 2 * kilogram)

    eq = Eq(x, 2 * l * m / (r ** 2))

    q = solve(eq, x)
    print(q[0])
    print(convert_to(q[0], [1 / meter]))

    res = convert_to(q[0], SI._base_units)
    print(res.as_coeff_Mul())
    print(latex(res))


if __name__ == '__main__':
    test()
