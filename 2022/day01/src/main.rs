use std::cmp::Reverse;
use std::error::Error;
use std::fs::File;
use std::io::{BufRead, BufReader};

const INPUT: &str = "input.txt";

fn main() -> Result<(), Box<dyn Error>> {
    let file = File::open(INPUT)?;
    let reader = BufReader::new(file);

    let mut calories = Vec::new();
    let mut current = 0;
    for line in reader.lines() {
        let line = line?;
        if line == "" {
            calories.push(current);
            current = 0;
            continue;
        }
        current += line.parse::<i32>()?;
    }
    calories.sort_by_key(|w| Reverse(*w));
    println!("{}", calories[0]);
    println!("{}", calories[0] + calories[1] + calories[2]);
    Ok(())
}
