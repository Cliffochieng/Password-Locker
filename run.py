import random
import string


from userData import UserData
from credentialsData import CredentialsData

def new_users(name_one, name_two, email_address, user_name, pass_word):

    """
    creates new user 
    """
    new_user = UserData(name_one, name_two, email_address, user_name, pass_word)
    
    return new_user

def save_accounts(account):
    """
    save new user account
    """
    account.save_account()


def check_user(used_name, used_password):
    """
    checks if user exists
    """
    user_exists = UserData.user_login(used_name, used_password)

    return user_exists

def add_credential(acc, acc_name, acc_password):
    """
    adds a credential
    """
    added_credential = CredentialsData(acc, acc_name, acc_password)

    return added_credential


def save_credentials(credential):
    """
    saves created credential
    """
    credential.save_credential()

def randompassword():
    """
    generates a random password
    """

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    password = ''.join(random.choice(chars) for x in range(size))

    return password
