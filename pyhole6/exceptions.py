class Pyhole6Error(Exception):
    """Base exception for Pyhole6 client"""
    pass

class AuthenticationError(Pyhole6Error):
    """Raised when authentication fails"""
    pass
