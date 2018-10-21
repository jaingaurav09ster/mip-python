
'''
Create exceptions based on your inputs. Please follow the tasks below.

 - Capture and handle system exceptions
 - Create custom user-based exceptions
'''


class ApplicationException(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super(ApplicationException, self).__init__(message)

        # Now for your custom code...
        self.errors = errors
        self.message = message
