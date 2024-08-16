from typing import Set, override, Tuple

from CoolProp import CoolProp as cp

from bardow.model import variablerelationship, variable


class WaterProperties(variablerelationship.ValueTable):

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
        pass

    @staticmethod
    def lookup(inputs: Tuple[variable.Known, variable.Known],
               target: variable.Unknown) -> variable.Known:
        pass
