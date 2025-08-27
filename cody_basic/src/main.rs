fn main() {
    println!("Starting...");
    let str = String::from("aabbb");
    println!("Result: {}", solution(str));

    let str = String::from("ba");
    println!("Result: {}", solution(str));

    let str = String::from("aaa");
    println!("Result: {}", solution(str));

    let str = String::from("b");
    println!("Result: {}", solution(str));

    let str = String::from("abba");
    println!("Result: {}", solution(str));

}

/* given a string str consisting of N letters 'a' and/or 'b'
 returns true when all letters 'a' are before all letters 'b'
 and return false otherwise
 */
fn solution(str: String) -> bool {
    let mut a = 0;
    let mut b = 0;
    
    for c in str.chars() {
        if c == 'a' {
            a = 1;

            if b > 0 {
                return false;
            }
        } else {
            b = 1;
        }
        
    }

    return true;
}

