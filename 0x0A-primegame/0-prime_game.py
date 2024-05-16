#!/usr/bin/python3
"""
Prime Game

Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and
removing that number and its multiples from the set.
The player that cannot make a move loses the game.

This script determines the winner of multiple rounds
of the game and returns the player who won the most rounds.
"""


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def play_game(n, primes):
    board = [True] * (n + 1)
    player_turn = 0
    current_prime_index = 0

    while True:
        while (current_prime_index < len(primes) and
                primes[current_prime_index] <= n and
                not board[primes[current_prime_index]]):
            current_prime_index += 1
        if (current_prime_index == len(primes) or
                primes[current_prime_index] > n):
            break

        prime = primes[current_prime_index]

        for multiple in range(prime, n + 1, prime):
            board[multiple] = False

        player_turn = 1 - player_turn

    return player_turn


def isWinner(x, nums):
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = play_game(n, primes)
            if winner == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
