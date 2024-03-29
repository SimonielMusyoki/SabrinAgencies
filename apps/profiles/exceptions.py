from rest_framework.exceptions import APIException


class ProfileNotFoundException(APIException):
    status_code = 404
    default_detail = "Profile with such arguments is not found"


class NotYourProfileException(APIException):
    status_code = 400
    default_detail = "You can not edit a profile that does not belong to you"
