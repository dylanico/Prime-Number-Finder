def prime_finder():
    """Creates a list of all of the the prime numbers up to and including the one entered"""
    while True:
        try:
            prime_number = int(input("Choose any number to find the prime numbers up to that number"))
        except:
            print("That is not a number. Try again")
        else:
            break
            
    
    prime_list = []
    random_list = [2,3,5,7]
    range_list = list(range(2,prime_number+1))
    for number in range_list:
        ##return prime numbers in a new list - the prime_list namely
        if number in random_list:
            prime_list.append(number)
        else:
            if number%2==0 or number%3==0 or number%5==0 or number%7==0:
                pass
            else:
                prime_list.append(number)
        
        
                
                
    print(f'Here is the list of prime numbers up to (or including) {prime_number}: {prime_list}.')
    #return f'Here is the list of prime numbers up to (or including) {prime_number}: {prime_list}.'

prime_finder()