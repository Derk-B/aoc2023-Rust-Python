use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;

struct CardCount {
    len: usize,
    list: Vec<i32>
}

impl CardCount {
    fn _increase(&mut self, i: usize) {
        while self.len <= i {
            self.len += 1;
            self.list.push(1);
        }
    }

    fn add(&mut self, i: usize, val: i32) {
        self._increase(i);

        self.list[i] += val;
    }

    fn get(&mut self, i: usize) -> i32 {
        self._increase(i);

        return self.list[i];
    }

    fn get_sum(&self) -> i32 {
        return self.list.iter().sum();
    }
}

fn main() {
    let start = Instant::now();

    let mut result1: i32 = 0;

    let lines = read_lines("src/input.txt").unwrap();

    let mut winning_numbers: [bool; 100] = [false; 100];
    let mut card_counts: CardCount = CardCount { len: 0, list: Vec::new() };
    
    for (line_index, line) in lines.enumerate() {
        match line {
            Ok(l) => {
                let parts = l
                    .split(": ")
                    .collect::<Vec<&str>>()[1]
                    .split(" | ").into_iter()
                    .collect::<Vec<&str>>();

                let win_nums: Vec<usize> = parts[0]
                .split_whitespace()
                .map(|n| n.parse::<usize>())
                .filter_map(Result::ok)
                .collect();
            
                // Note the winning numbers
                for n in win_nums {
                    winning_numbers[n] = true;
                }

                let our_nums: Vec<usize> = parts[1]
                    .split_whitespace()
                    .map(|n| n.parse::<usize>())
                    .filter_map(Result::ok)
                    .collect();

                let mut match_count: u32 = 0;
                for n in our_nums {
                    if winning_numbers[n] {
                        match_count += 1;
                    }
                }
                
                // Part 1
                if match_count > 0 {
                    result1 += i32::pow(2, match_count - 1);
                }

                winning_numbers = [false; 100];

                // Part 2
                for i in 0 .. match_count {
                    let next_index: usize = line_index + usize::try_from(i).unwrap() + 1;

                    let current_count = card_counts.get(line_index);
                    card_counts.add(next_index, current_count);
                }
            }

            Err(_) => {
                println!("Could not read line!")
            }
        }
    }

    let result2: i32 = card_counts.get_sum();

    println!("part1: {}", result1);
    println!("part2: {}", result2);

    let duration = start.elapsed();
    println!("Time elapsed: {:?}", duration);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}