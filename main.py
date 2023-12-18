from TELNET import get_user_ID
from brain import add_new_user

def gen_iban(ID):
    longueur_partie = len(ID) // 5
    iban = [ID[i:i+longueur_partie] for i in range(0, len(ID), longueur_partie)]
    iban = '-'.join(iban)
    return iban


def gen_iban_user(pseudo):
    iban =  get_user_ID(True, pseudo)
    iban = iban[0:34]
    iban = gen_iban(iban)
    return iban


def creat_user(pseudo):
    iban = gen_iban_user(pseudo)
    add_new_user(iban)


iban = creat_user("Alexo")






