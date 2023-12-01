use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // Part 1
    let mut result: u32 = 0;
    if let Ok(lines) = read_lines("src/input.txt") {
        for line_opt in lines {
            if let Ok(line) = line_opt {
                let line_value: u32 = get_line_value(&line);
                result += line_value;
            }
        }
    }

    println!("part1: {}", result);

    // Part 2
    let mut result: u32 = 0;
    if let Ok(lines) = read_lines("src/input.txt") {
        for line_opt in lines {
            if let Ok(line) = line_opt {
                let line_value: u32 = get_real_line_value(&line);
                result += line_value;
            }
        }
    }

    println!("part2: {}", result);
}

fn get_real_line_value(line: &str) -> u32 {
    let mut all_numbers: Vec<u32> = Vec::new();
    let digit_words: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    for (i, c) in line.chars().enumerate() {
        if c.is_numeric() {
            if let Some(number) = c.to_digit(10) {
                all_numbers.push(number);
            }
            continue;
        }
        for (word_index, word) in digit_words.iter().enumerate() {
            if line[i..].starts_with(word) {
                if let Ok(real_number) = u32::try_from(word_index) {
                    all_numbers.push(real_number + 1);
                }
            }
        }
    }

    if let Some(first) = all_numbers.first() {
        if let Some(last) = all_numbers.last() {
            return first * 10 + last;
        }
    }

    0
}

fn get_line_value(line: &str) -> u32 {
    let mut all_numbers: Vec<u32> = Vec::new();
    for c in line.chars() {
        if c.is_numeric() {
            if let Some(number) = c.to_digit(10) {
                all_numbers.push(number)
            }
        }
    }

    if let Some(first) = all_numbers.first() {
        if let Some(last) = all_numbers.last() {
            return first * 10 + last;
        }
    }

    0
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}