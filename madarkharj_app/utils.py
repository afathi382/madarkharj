




import uuid
from .serializers import FactorSerializer


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except:
        return False


def factor_calculator(factors, profile_id):
    serializer= FactorSerializer(factors, many= True)
    amount=0
    for factor in serializer.data:
        if factor['owner']== uuid.UUID(profile_id):
            amount+=factor['price']
        if uuid.UUID(profile_id) in factor['share_with']:
            members=factor['share_with']
            amount-=factor['price']/len(members) 
    
    return amount