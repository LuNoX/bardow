from dataclasses import dataclass

from bardow.model import variable


@dataclass
class State:
    pressure: variable.Variable
    volume: variable.Variable
    temperature: variable.Variable
    internal_energy: variable.Variable
    enthalpy: variable.Variable
    entropy: variable.Variable

    name: str = ""
