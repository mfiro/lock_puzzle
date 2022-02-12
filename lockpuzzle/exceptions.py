class InvalidNumberOfDigitsException(Exception):
    def __init__(self, n_digits):
        self.message = f'Invalid number of digits. Your guess must include {n_digits} digits'
    
    def __str__(self):
        return 'InvalidNumberOfDigitsException: %s' % self.message