import re


class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        """
        validate the email
        Args:
            value:

        Returns:

        """
        # \b Matches the empty string, but only at the beginning or end of a word.
        # | OR operator
        # {2, 5} 2 to 5 repetitions of either A-Z or a-z
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Za-z]{2,5}\b'
        if re.fullmatch(pattern, value):
            self._email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        """
        save the email into a file
        Returns:

        """
        with open('emails.text', 'a') as f:
            f.write(self.email + '\n')
