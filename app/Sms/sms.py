def send(to, source, body):
    #to: str, from: str / source, body: str
    proceed = False
    if to[0:2] == "07":
        proceed = True
    else:
        return InvalidDestinationException(MessageException)
        
    if source[0:2] == "07":
        proceed = True
    else:
        return InvalidDestinationException(MessageException)
    
    if proceed == True:
        access_api = "Fail" # api response is failed
        access_api = "Wait" # api response is successful if there is no credit
        access_api = "Success" # api response is successful if there is credit
        if access_api == "Success":
            return "success"
        elif access_api == "Wait":
            return "wait"
        else:
            return OutOfCreditException(MessageException)
    else:
        return MessageException(Exception)


class MessageException(Exception):
    """Message Exception"""

class OutOfCreditException(MessageException):
    """The owner of this website has failed to pay enough money to
    the mobile phone company, ergo the message was not sent."""

class InvalidDestinationException(MessageException):
    """The given destination phone number is invalid."""
