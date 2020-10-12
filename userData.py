class UserData:

    '''
    class to create new user accounts 
    '''
    create_account = []

    def __init__(self, firstName, lastName, email, username, password):

        """
        Initializes the class
        """

        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password

    def save_account(self):

        """
        saves the new user to create_account list
        """

        UserData.create_account.append(self)