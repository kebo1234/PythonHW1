class OrderError(Exception):
    """
    Raise OrderError for invalid orders (e.g., zero or negative quantity)
    """
    pass

class ExecutionError(Exception):
    """Raised when order execution fails"""
    pass