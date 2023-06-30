def scale(value:float, min_a:float, max_a:float, min_b:float, max_b:float) -> float:
    """Simple linear scaler

    Args:
        value (float): Value to be scaled'
        min_a (float): Min value from value's range
        max_a (float): Max value from value's range
        min_b (float): Min value from target range
        max_b (float): Max value from target range
        
    Returns:
        float: Value scaled to target range
    """
    return (((value - min_a) / (max_a - min_a)) * (max_b - min_b)) + min_b
