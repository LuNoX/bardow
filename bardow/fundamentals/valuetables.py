from typing import Set, override, Tuple
from functools import cache

from sympy.physics import units
from sympy.physics.units import dimensions
from sympy.physics.units.definitions.dimension_definitions import (
    temperature, volume, amount_of_substance, mass, pressure)
from CoolProp import CoolProp as Cp

from bardow.model import variablerelationship, variable, errors


# TODO: refactor all of this into a sympy to CoolProp backend

# http://www.coolprop.org/coolprop/HighLevelAPI.html#id6
# Phase String: Phase Region
# “liquid”: p < pcrit & T < Tcrit ; above saturation
# “gas”: p < pcrit & T < Tcrit ; below saturation
# “twophase”: p < pcrit & T < Tcrit ; mixed liquid/gas
# “supercritical_liquid”: p > pcrit & T < Tcrit
# “supercritical_gas”: p < pcrit & T > Tcrit
# “supercritical”: p > pcrit & T > Tcrit
# “not_imposed”: (Default) CoolProp to determine phase

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
            # TODO: calculate T, rho and p first so subsequent calls can use
            #  faster lookups
            self.variables.remove(unknown)
            self.variables.add(known)
        return knowns

    @staticmethod
    def find_optimal_lookup_inputs(knowns: Set[variable.Known]
                                   ) -> Tuple[variable.Known, variable.Known]:
        if num_knowns := len(knowns) < 2:
            raise errors.TooFewKnownsError(
                f"Expected at least 2 known variables, got {num_knowns}!"
                f"Knowns: {knowns}")
        # CoolProp is fastest with (T, rho) as input, slower with (T, p) and
        # significantly slower in other cases
        T = rho = rho_molar = p = False
        for known in knowns:
            print(known.dimension)
            T = rho = rho_molar = p = known
            # TODO: implement
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
        target_value = Cp.PropsSI(parameter,
                                  first_input_parameter, first_value,
                                  second_input_parameter, second_value,
                                  'Water')
        return target.create_known(target_value, unit)

    @staticmethod
    @cache
    def map_sympy_dimension_to_coolprop_parameter(
            dimension: dimensions.Dimension) -> tuple[str, units.Unit]:
        # TODO: implement

        # http://www.coolprop.org/coolprop/HighLevelAPI.html#id19

        # pressure: variable.Variable
        # P Pa IO False Pressure

        # volume: variable.Variable
        # DMOLAR, Dmolar mol / m ^ 3 IO False Molar density
        # D, DMASS, Dmass kg / m ^ 3 IO False Mass density

        # temperature: variable.Variable
        # T K IO False Temperature

        # internal_energy: variable.Variable
        # UMOLAR, Umolar J/mol IO False Molar specific internal energy
        # U, UMASS, Umass J/kg IO False Mass specific internal energy

        # enthalpy: variable.Variable
        # HMOLAR, Hmolar J/mol IO False Molar specific enthalpy
        # H, HMASS, Hmass J/kg IO False Mass specific enthalpy

        # entropy: variable.Variable
        # SMOLAR, Smolar J/mol/K IO False Molar specific entropy
        # S, SMASS, Smass J/kg/K IO False Mass specific entropy

        pass

    @staticmethod
    @cache
    def convert_known_variable_to_coolprop_parameter_pair(
            known: variable.Known) -> Tuple[str, float]:
        parameter, unit = CoolPropWaterProperties. \
            map_sympy_dimension_to_coolprop_parameter(known.dimension)
        value = units.convert_to(known._backend_representation.value, unit)
        return parameter, value
