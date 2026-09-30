"""Main module of the Pairsum problem."""

from typing import Annotated

from algobattle.problem import InstanceModel, Problem, SolutionModel
from algobattle.types import MinLen, SizeIndex, UniqueItems, u64
from algobattle.util import Role, ValidationError

Number = SizeIndex


class Instance(InstanceModel):
    """An instance of a Pairsum problem."""

    numbers: Annotated[list[u64], MinLen(4)]

    @property
    def size(self) -> int:
        return len(self.numbers)


class Solution(SolutionModel[Instance]):
    """A solution to a Pairsum problem."""

    indices: Annotated[tuple[Number, Number, Number, Number], UniqueItems]

    def validate_solution(self, instance: Instance, role: Role) -> None:
        super().validate_solution(instance, role)
        first = instance.numbers[self.indices[0]] + instance.numbers[self.indices[1]]
        second = instance.numbers[self.indices[2]] + instance.numbers[self.indices[3]]
        if first != second:
            raise ValidationError("Solution elements don't have the same sum.")


Pairsum = Problem(name="Pairsum", min_size=4, instance_cls=Instance, solution_cls=Solution)
