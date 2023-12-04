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
    preg_match_all('/\d/', $line, $matches);

    $first = reset($matches[0]);
    $last = end($matches[0]);

    $v = (int) sprintf('%d%d', $first, $last);

    if (getenv('DEBUG')) {
        echo "LINE $line" . PHP_EOL;
        echo "VAL: $v" . PHP_EOL;
    }

    return $v;
}

function calc(array $in): int
{
    return array_sum(array_map(fn (string $line) => process($line), $in));
}

assert(142 === calc($sample));

echo calc(explode(PHP_EOL, file_get_contents('puzzle.txt'))) . PHP_EOL;