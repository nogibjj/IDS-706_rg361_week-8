fn main() {
    let n = 31;
    let mut fac: u128 = 1;
    for i in 1..=n {
        fac *= i as u128;
    }
    println!("{}", fac);
}