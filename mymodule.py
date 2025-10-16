def energy_conversion(joules: float) -> float:
    """Convert energy from Joules to kilocalories."""
    if joules < 0:
        raise ValueError("Energy cannot be negative")
    return joules / 4184.0
#asfasfsa
