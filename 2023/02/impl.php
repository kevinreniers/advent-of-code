<?php
declare(strict_types=1);

$sample = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
];

function process(string $line, int $redCubes, int $greenCubes, int $blueCubes): int
{
    [$gameRaw, $setsRaw] = explode(': ', $line);

    preg_match_all('/(?P<count>\d+) red/', $setsRaw, $redMatches);
    if (max(array_map('intval', $redMatches['count'])) > $redCubes) {
        return 0;
    }

    preg_match_all('/(?P<count>\d+) green/', $setsRaw, $greenMatches);
    if (max(array_map('intval', $greenMatches['count'])) > $greenCubes) {
        return 0;
    }

    preg_match_all('/(?P<count>\d+) blue/', $setsRaw, $blueMatches);
    if (max(array_map('intval', $blueMatches['count'])) > $blueCubes) {
        return 0;
    }

    return (int) preg_replace('/\D+/', '', $gameRaw);
}

function calc(array $in, int $redCubes, int $greenCubes, int $blueCubes): int
{
    return array_sum(array_map(fn ($line) => process($line, $redCubes, $greenCubes, $blueCubes), $in));
}

echo 'TEST: ' . calc($sample, 12, 13, 14) . PHP_EOL;
echo 'REAL: ' . calc(explode(PHP_EOL, file_get_contents('puzzle.txt')), 12, 13, 14) . PHP_EOL;

function leastCubes(string $line): int
{
    $sets = explode(': ', $line)[1];

    preg_match_all('/(?P<count>\d+) red/', $sets, $redMatches);
    preg_match_all('/(?P<count>\d+) green/', $sets, $greenMatches);
    preg_match_all('/(?P<count>\d+) blue/', $sets, $blueMatches);

    return array_product([
        max(array_map('intval', $redMatches['count'])),
        max(array_map('intval', $greenMatches['count'])),
        max(array_map('intval', $blueMatches['count'])),
    ]);
}

function powerOfSets(array $in): int
{
    return array_sum(array_map(fn ($item) => leastCubes($item), $in));
}

echo 'POWER: ' . powerOfSets(explode(PHP_EOL, file_get_contents('puzzle.txt'))) . PHP_EOL;