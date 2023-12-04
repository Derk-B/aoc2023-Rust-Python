use std::fs::File;
use std::io::{self, BufRead, Error};
use std::path::Path;
use std::time::Instant;

fn main() {
    let start = Instant::now();

    let mut result1: u32 = 0;
    let mut result2: u32 = 0;

    let lines = read_lines("src/input.txt").unwrap();
    
    for (i, line) in lines.enumerate() {
        match line {
            Ok(l) => {
                let parts: Vec<&str> = l.split(" : ").collect();
                
            }

            Err(_) => {
                println!("Could not read line!")
            }
        }

    }

    println!("part1: {}", result1);
    println!("part2: {}", result2);

    let duration = start.elapsed();
    println!("Time elapsed: {:?}", duration);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}