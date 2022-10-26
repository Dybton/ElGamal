import random

#Helper functions

#brute force private key to find bobs private key using shared based shared prime and public key
def brute_force_private_key(shared_prime, shared_base, public_key):
    for i in range(1, shared_prime):
        if (shared_base ** i) % shared_prime == public_key:
            return i

# random_int generates a random integer between 0 and p
def random_int(p):
    return random.randint(0, p)

#Exercise 1 + 2
# 1. You are Alice and want to send 2000 kr. to Bob through a confidential message. You decide to use the ElGamal public key method.
# 2. You are now Eve, who can intercept encrypted messages, including Alice’s one.
# Write code that allows Eve to find Bob’s private key and reconstruct Alice’s
# message. NOTE: Recall that Eve has access to the public terms g, p, and PK.

g = 666 #shared base
p = 6661 #shared prime

# Bob
gx_mod_p = 2227 #Bobs public key
bobs_private = brute_force_private_key(p, g, gx_mod_p) #

# Alice
y = random_int(p) #Alice's private key
gy_mod_p = (g ** y) % p #Alice's public key
shared_secret_alice = (gx_mod_p ** y) % p #Alice's shared secret

plain_message = 2000

# Alice encrypts the message using the shared secret
encrypted_message = (plain_message * shared_secret_alice) % p

#Using Alice's public key we can now calculate Bob's shared message. Note that Alice's shared secret is the same as Bob's shared secret
shared_secret_bob = (gy_mod_p ** bobs_private) % p #Bob's shared secret

#We calculate shared_secret_inverse such that we can decrypt the message
shared_secret_inverse = pow(shared_secret_bob, -1, p)

#We decrypt the message and see that it's the same as the plain message
decrypted_message = (encrypted_message * shared_secret_inverse) % p


#Exericse 3 
#  Write code that can modify Alice’s encrypted message
# so that when Bob decrypts it, he will get the double amount originally sent for
# Alice (so, if Alice’s original encrypted message is ’2000’, then Bob would decrypt
# ’4000’).

#We can do this by multiplying the encrypted message with two followed by mod p. This will double the encrypted message. 
# And since we mod with p afterwards Bob has no way of knowing that we doubled the message.
encrypted_message = encrypted_message * 2 % p 

decrypted_message = (encrypted_message * shared_secret_inverse) % p
print(decrypted_message)


