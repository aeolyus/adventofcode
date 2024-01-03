// use std::collections::HashMap;
use std::error::Error;
use std::fs::File;
use std::io::{BufRead, BufReader};

const INPUT: &str = "input.txt";

fn main() -> Result<(), Box<dyn Error>> {
    let file = File::open(INPUT)?;
    let reader = BufReader::new(file);

    // let opp_to_you = HashMap::from([("A", "X"), ("B", "Y"), ("C", "Z")]);
    // let you_to_opp = HashMap::from([("X", "A"), ("Y", "B"), ("Z", "C")]);
    let mut current = 0;
    let mut perfect_current = 0;
    for line in reader.lines() {
        let line = line?;
        let sliced: Vec<&str> = line.split_whitespace().collect();
        println!("{:?}", sliced);
        // sliced[1] = you_to_opp[&sliced[1]];
        let opp = points(sliced[0])?;
        let you = points(sliced[1])?;
        let points = ((you - opp + 1).rem_euclid(3)) * 3 + you;
        let perfect_points = ((you - 1) * 3) + (you + opp).rem_euclid(3) + 1;
        println!("{}", perfect_points);
        current += points;
        perfect_current += perfect_points;
    }

    println!("");
    println!("{}", current);
    println!("{}", perfect_current);
    Ok(())
}

fn points(a: &str) -> Result<i32, Box<dyn Error>> {
    match a {
        "A" | "X" => Ok(1),
        "B" | "Y" => Ok(2),
        "C" | "Z" => Ok(3),
        _ => Err("Not a move".into()),
    }
}
