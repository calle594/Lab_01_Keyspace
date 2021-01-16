import sys, math

def get_keyspace(passwd):
    """print entrophy valuefor ascii password"""
    print ("Keyspace")
    char_set = 95
    keyspace = char_set ** 4
    attempts =  keyspace / 3 
    passwdsPerHour = 100000000
    averageTimeToCrack = attempts/ passwdsPerHour

    print("Password:", passwd + "- total of: " + str(keyspace) + " key combinations")
    print("Average attempts to crack: " + str(attempts))
    print("Average time to find password: " + str(averageTimeToCrack) + " hours")
    
passwd = 'tes '
get_keyspace(passwd)
