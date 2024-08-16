from typing import Set, override, Tuple
from functools import cache

from sympy.physics import units
from sympy.physics.units import dimensions
from sympy.physics.units.definitions.dimension_definitions import (
    temperature, volume, amount_of_substance, mass, pressure)
from CoolProp import CoolProp as cp

from bardow.model import variablerelationship, variable, errors


# TODO: refactor all of this into a sympy to CoolProp backend

class CoolPropWaterProperties(variablerelationship.ValueTable):

    @override
    def relate(self) -> Set[variable.Known]:
        knowns = {var for var in self.variables if var.is_known}
        inputs = self.find_optimal_lookup_inputs(knowns)
        unknowns = self.variables - knowns
        knowns = set()
        for unknown in unknowns:
            known = self.lookup(inputs, unknown)
            knowns.add(known)
            self.variables.remove(unknown)
            self.variables.add(known)
        return knowns

    @staticmethod
    def find_optimal_lookup_inputs(knowns: Set[variable.Known]
                                   ) -> Tuple[variable.Known, variable.Known]:
        if l := len(knowns) < 2:
            raise errors.TooFewKnownsError(
                f"Expected at least 2 known variables, got {l}: {knowns}")
        # CoolProp is fastest with T, rho as input, slower with T, p and
        # significantly slower in every other case
        T = rho = rho_molar = p = False
        for known in knowns:
            print(known.dimension)
            T = rho = rho_molar = p = known
            # match known.dimension:
            #     case temperature:
            #         T = known
            #     case mass/volume:
            #         rho = known
            #     case mass/amount_of_substance:
            #         rho_molar = known
            #     case volume/mass:
            #         rho = 1/known
            #     case volume/amount_of_substance:
            #         rho_molar = 1/known
            #     case pressure:
            #         pressure = known

        rho = rho or rho_molar
        if T and rho:
            return T, rho
        if T and p:
            return T, p
        # If neither fast case is available, just pick any two items
        iterator = iter(knowns)
        return next(iterator), next(iterator)

    @staticmethod
    @cache
    def lookup(inputs: Tuple[variable.Known, variable.Known],
               target: variable.Unknown) -> variable.Known:
        parameter, unit = CoolPropWaterProperties. \
            map_sympy_dimension_to_coolprop_parameter(target.dimension)
        first_input_parameter, first_value = CoolPropWaterProperties. \
            convert_known_variable_to_coolprop_parameter_pair(inputs[0])
        second_input_parameter, second_value = CoolPropWaterProperties. \
            convert_known_variable_to_coolprop_parameter_pair(inputs[1])
        target_value = cp.PhaseSI(parameter,
                                  first_input_parameter, first_value,
                                  second_input_parameter, second_value)
        return target.create_known(target_value, unit)

    @staticmethod
    @cache
    def map_sympy_dimension_to_coolprop_parameter(
            dimension: dimensions.Dimension) -> tuple[str, units.Unit]:
        # TODO: implement
        pass

    @staticmethod
    @cache
    def convert_known_variable_to_coolprop_parameter_pair(
            known: variable.Known) -> Tuple[str, float]:
        parameter, unit = CoolPropWaterProperties. \
            map_sympy_dimension_to_coolprop_parameter(known.dimension)
        value = units.convert_to(known._sympy_quantity, unit)
        return parameter, value
