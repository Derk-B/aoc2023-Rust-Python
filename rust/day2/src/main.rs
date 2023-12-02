use std::cmp::max;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;
use regex;

fn main() {
    let start = Instant::now();

    // Part 1
    let mut result: u32 = 0;

    if let Ok(lines) = read_lines("src/input.txt") {
        for (i, line) in lines.enumerate() {
            if let Ok(l) = line {
                if !check_game(&l) { 
                    continue; 
                };
                
                if let Ok(index) = u32::try_from(i) {
                    result += index + 1;
                }
            }
        }
    }

    println!("part1: {}", result);

    // Part 2
    let mut result: u32 = 0;

    if let Ok(lines) = read_lines("src/input.txt") {
        for line in lines {
            if let Ok(l) = line {
                result += get_game_factor(&l)
            }
        }
    }

    println!("part2: {}", result);

    let duration = start.elapsed();
    println!("Time elapsed: {:?}", duration);
}

fn check_game(game: &str) -> bool {
    let game_data: &str = game.split(": ").collect::<Vec<&str>>()[1];
    let sets: Vec<&str> = game_data.split("; ").collect();
    for set in sets {
        let actions: Vec<&str> = set.split(", ").collect();
        for action in actions {
            let count_and_color = action.split_whitespace().collect::<Vec<&str>>();
            if let Ok(count) = count_and_color[0].parse::<u32>() {
                let res: bool = match count_and_color[1] {
                    "green" => count <= 13,
                    "red" => count <= 12,
                    "blue" => count <= 14,
                    _ => false
                };
                if !res {
                    return false;
                }
            }
        }
    }

    true
}

fn get_game_factor(game: &str) -> u32 {
    let (mut max_green, mut max_red, mut max_blue): (u32, u32, u32) = (0, 0, 0);
    let game_data: &str = game.split(": ").collect::<Vec<&str>>()[1];
    let re = regex::Regex::new(r"; |, ").unwrap();
    for action in re.split(game_data) {
        let count_and_color: Vec<&str> = action.split_whitespace().collect::<Vec<&str>>();
        if let Ok(count) = count_and_color[0].parse::<u32>() {
            match count_and_color[1] {
                "green" => max_green = max(max_green, count),
                "red" => max_red = max(max_red, count),
                "blue" => max_blue = max(max_blue, count),
                _ => continue,
            }
        }
    }

    max_green * max_red * max_blue
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}