import tqdm
import time

def generate_PIN(digits_possible,length_of_PIN):
    
    import numpy as np
    
    len_digits_possible = len(digits_possible)
    print("~~~~ Generating random PIN ~~~~")
    random_PIN = ''.join(np.random.choice(digits_possible, length_of_PIN))
    print("")
    
    file1 = open("PIN.txt","w")
    file1.writelines(random_PIN)
    file1.close() 

def timing_verifier(PIN_guess, verifier_design= 'variable'):
    
    # verifier_design = 'variable' when it is non-protected, 'constant' when it is running in constant time
    # in this function, we assume that the length of PIN_guess match the length of PIN_correct, so no error check is performed
    
    with open('PIN.txt') as f:
        lines = f.readlines()
    
    PIN_correct = (lines[0])
    
    correctness_check = 0
    
    iterator = tqdm.tqdm(range(len(PIN_correct)))
    
    if verifier_design == 'variable':
        for i in iterator:
            time.sleep(0.1)
            if(PIN_guess[i] != PIN_correct[i]):
                break
            else:
                correctness_check+=1

    elif verifier_design == 'constant':
        for i in iterator:
            time.sleep(0.1)
            if(PIN_guess[i] != PIN_correct[i]):
                continue
            else:
                correctness_check+=1
    
    if correctness_check == len(PIN_correct):
        print("Entered PIN is correct")
        return 1
    else:
        print("Entered PIN is incorrect")
        return 0

if __name__ == "__main__":       
      
    length_of_PIN = 6
    digits_possible = ['0','1','2','3','4','5','6','7','8','9']
    
    len_digits_possible = len(digits_possible)
    
    print("Generating PIN...")
    generate_PIN(digits_possible, length_of_PIN)
    print("")
    
    N_attempts = 0
    while 1:
        
        PIN_guess = input("Enter PIN guess (6 digits, 0-9):")
        N_attempts += 1
        if len(PIN_guess)!=length_of_PIN:
            print("Incorrect PIN length.... Try again")
            continue
        else:
            check = [(x not in digits_possible) for x in PIN_guess]
            if sum(check)!=0:
                print("Incorrect digit entered.... Try again")
                continue
        
        start_time = time.time()        
        x = timing_verifier(PIN_guess,'variable')
        print("time taken: ", time.time()-start_time)
        
        if x == 1:
            print("Correct PIN recovered.")
            print("No of attempts ", N_attempts)
            break
    
    
    