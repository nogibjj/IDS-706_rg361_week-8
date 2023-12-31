use std::time::Instant;
// extern crate num_bigint;
// extern crate num_traits;

// use num_bigint::BigUint;
// use num_traits::{One};

fn main() {
    let start = Instant::now();
    let n: u128 = 31;
    let mut _fac: u128 = 1;
    for i in 1..=n {
        _fac *= i;
    }

    let duration = start.elapsed();
    print!("{}", duration.as_nanos());
}
