<?php
declare(strict_types=1);

$sample = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
];

function process(string $line): int
{
    $line = text2digits($line);

    preg_match_all('/\d/', $line, $matches);

    $first = reset($matches[0]);
    $last = end($matches[0]);

    return (int) sprintf('%d%d', $first, $last);
}

function text2digits(string $line)
{
    $map = [
        'one' => '1',
        'two' => '2',
        'three' => '3',
        'four' => '4',
        'five' => '5',
        'six' => '6',
        'seven' => '7',
        'eight' => '8',
        'nine' => '9',
    ];

    while (preg_match('/(one|two|three|four|five|six|seven|eight|nine)/', $line, $matches) === 1) {
        $line = preg_replace("/$matches[0]/", $map[$matches[0]], $line, 1);
    }

    return $line;
}

function calc(array $in): int
{
    return array_sum(array_map(fn (string $line) => process($line), $in));
}

assert(142 === calc($sample));

echo calc(explode(PHP_EOL, file_get_contents('puzzle.txt'))) . PHP_EOL;