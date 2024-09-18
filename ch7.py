import math

def newton_root(a, x):
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.0000001:
            break
        x = y
    return y

def test_square_root(num):
    print(f"{'a': <3} {'mysqrt(a)': <14} {'math/sqrt(a)': <14} {'diff': <14}")
    print(f"{'-': <3} {'---------': <14} {'------------': <14} {'----': <14}")
    for i in range(1, num+1):
        sqrt_value = round(math.sqrt(i), 11)
        newton_value = round(newton_root(i, 1.8), 11)
        print("{: <3} {: <14} {: <14} {: <14}".format(float(i), sqrt_value, newton_value, abs(sqrt_value - newton_value)))

def eval_loop():
    last_result = None  # To store the result of the last evaluation
    while True:
        user_input = input("Enter an expression (or type 'done' to quit): ")
        
        if user_input.lower() == 'done':
            break
        
        # Evaluate the input and print the result
        last_result = eval(user_input)
        print(last_result)
    
    print("Last evaluated result:", last_result)
    return last_result  # Return the last evaluated result


def estimate_pi():
    first_term = (2 * math.sqrt(2) / 9801)
    k = 1
    last_term = 1103
    current = 1103
    while current > 1e-15:
        current = (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k) * 396**(4*k))
        # print(current)
        last_term += current
        k += 1

    return 1/(first_term * last_term)

if __name__ == '__main__':

    # Exercise 7.1
    test_square_root(9)

    # Exercise 7.2
    last_eval = eval_loop()

    # Exercise 7.3
    print(estimate_pi())
