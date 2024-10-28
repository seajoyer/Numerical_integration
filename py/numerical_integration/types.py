from dataclasses import dataclass
from typing import Optional

@dataclass
class IntegrationResult:
    method_name: str
    value: float
    step_size: float
    error: Optional[float] = None

    def __str__(self) -> str:
        base_str = (
            f"{self.method_name}:\n"
            f"  Value: {self.value:.10f}\n"
            f"  Step size: {self.step_size:.10f}"
        )
        if self.error is not None:
            base_str += f"\n  Error: {self.error:.10f}"
        return base_str
