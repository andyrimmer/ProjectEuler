// Euler discovered the remarkable quadratic formula:
//
// n^2+n+41
//
// It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
// . However, when n=40,402+40+41=40(40+1)+41
//  is divisible by 41, and certainly when n=41,412+41+41
//  is clearly divisible by 41.
//
// The incredible formula n2−79n+1601
//  was discovered, which produces 80 primes for the consecutive values 0≤n≤79
// . The product of the coefficients, −79 and 1601, is −126479.
//
// Considering quadratics of the form:
//
// n^2 + a*n+b where |a| < 1000 and |b| ≤ 1000
//
// where |n| is the modulus/absolute value of n
//
// Find the product of the coefficients, a and b for the quadratic expression that produces the
// maximum number of primes for consecutive values of n starting with n=0


// Test if a given number is prime or not. This runs in O(n) and uses O(1) memory
function is_prime(x){
    if (x <= 1){
        return false;
    }
    for (i=2; i<x; ++i){
        if (x % i == 0){
            return false;
        }
    }
    return true;
}


// Return a function to evaulate (n^2 + a*n + b) for given n
function generate_polynomial(a, b){
    return function (n){
        return Math.pow(n, 2) +a*n + b;
    }
}


function count_num_consecutive_primes(polynomial, start_val, end_val, increment){
    num_primes = 0;
    for (n=start_val; n<=end_val; n+=increment){
        if (is_prime(polynomial(n))){
            num_primes += 1;
        } else {
            break;
        }
    }
    return num_primes
}

max_consecutive_primes = 0;
best_a = -999;
best_b = -999;

for (a=-999; a<=999; ++a){
    for (b=-999; b<=999; ++b){

        polynomial = generate_polynomial(a,b);
        nun_primes = count_num_consecutive_primes(polynomial, 0, 10000, 1);

        if (num_primes > max_consecutive_primes){
            max_consecutive_primes = num_primes;
            best_a = a;
            best_b = b;
            console.log('New record: For a = ' + a + ' and b = ' + b + ' num consecutive primes = ' + num_primes + ' and product of and b = ' + a*b);
        }
    }
}
