from email import message
from operator import mod
import random


#Exercise 1:


#You are Alice and want to send 2000 kr. to Bob through a confidential message. You decide to use the ElGamal public key method.


#Create a function that uses the elgamal method to encrypt a message. 
# The function should take the message, the public key and the private key as input and return the encrypted message as output.

#Create a function that generates a random integer between 0 and 500

#Shared
g = 666 #shared base
p = 6661 #shared prime

#brute force private key to find bobs private key using shared based shared prime and public key
def brute_force_private_key(shared_prime, shared_base, public_key):
    for i in range(1, shared_prime):
        if (shared_base ** i) % shared_prime == public_key:
            return i

# define a function that generates aa random integer between 0 and p
def random_int():
    return random.randint(0, p)

# Bob
gx_mod_p = 2227 #Bobs public key

# Alice
y = random_int()
gy_mod_p = (g ** y) % p #Alices public key
shared_secret_alice = (gx_mod_p ** y) % p 

plain_message = 2000

#Encrypted message
encrypted_message = (plain_message * shared_secret_alice) % p


### Decrypt
#create a function that decrypts the encrypted message. 
# The function should take the encrypted message, the public key and the private key as input and return the decrypted message as output.

bobs_private = brute_force_private_key(p, g, gx_mod_p)
shared_secret_bob = (gy_mod_p ** bobs_private) % p

s_inverse = pow(shared_secret_bob, -1, p)


#Exericse 3 
encrypted_message = encrypted_message * 2 % p
decrypted_message = (encrypted_message * s_inverse) % p
print(decrypted_message)


