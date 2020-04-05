import crypt
import pickle
from pathlib import Path


def check(user, pwd):
    '''
    '''
    try:
        with Path('pdb.pkl').open('rb') as f:
            hashes = pickle.load(f)
    except FileNotFoundError:
        hashes = {}
    if user not in hashes:
        hashes[user] = crypt.crypt(pwd, user)
        with Path('pdb.pkl').open('wb+') as f:
            pickle.dump(hashes, f)
        return True
    else:
        ciphertxt = hashes[user]
        encryptxt = crypt.crypt(pwd, ciphertxt)
        return ciphertxt == encryptxt
