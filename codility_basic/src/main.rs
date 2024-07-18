fn main() {
    println!("Hello, world!");
}

// return the smallest positive integer (greater than 0) that does not occur in A
pub fn solution(A: &mut Vec<i32>) -> i32 {
    let mut smallest_positive = 1;
    A.sort();
    for i in A {
        if *i == smallest_positive {
            smallest_positive += 1;
        }
    }
    smallest_positive
}