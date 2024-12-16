from dataclasses import dataclass

from Command import Command


@dataclass
class ExecutionStatus:
    status: str
    command: Command