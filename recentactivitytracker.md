# Warm-Up Challenge — Recent Activity Tracker

## Overview

Build a simple in-memory activity tracker that processes a stream of timestamped events.

This exercise is designed to practice:

- Working with streaming input
- Managing time-based data
- Choosing appropriate data structures
- Handling boundary conditions carefully
- Writing clean, incremental logic

You may use **any programming language** you’re comfortable with.

---

## What We Care About

- Clean and readable code (without using AI to write the code for you)
- Clear reasoning and explanation
- Appropriate data structure choices
- Correct handling of time boundaries
- Steady progress toward a working solution
- Thoughtful testing strategy
- Speed (time yourself to see how much you can complete in 1 hour)

---

## Problem Statement

You will read lines from standard input in the following format:

    <timestamp_ms> <event_name>

Example:

    0 login
    200 click
    400 scroll
    1200 login
    1500 click
    

Timestamps are integers representing milliseconds.

Your task:

> For each event, print how many events occurred within the last **W milliseconds**, including the current event.

For this exercise, assume `W = 1000`

---

## Window Definition

For an event at time `t`, count all events whose timestamps fall within:

    (t - W, t]


You must:

- Choose and clearly state your boundary convention.
- Apply it consistently.

Input timestamps will be in **non-decreasing order**.

---

## Output Format

For each input line, print:

    <timestamp_ms> <event_name> <count_in_window>


Example output:

    0 login 1
    200 click 2
    400 scroll 3
    1200 login 2
    1500 click 2


---

## Assumptions

- Input is well-formed.
- Timestamps are sorted.
- Continue processing until EOF.
- All data may be kept in memory.

You do **not** need to handle:

- Concurrency
- Persistent storage
- Extremely large datasets

---

## Requirements

- Maintain correct counts for each event.
- Remove events that fall outside the time window.
- Avoid unnecessary recomputation.
- Keep your implementation simple and readable.

---

## Suggested Development Approach

You may want to think about:

- How to efficiently track only the relevant recent events.
- How to remove events that are no longer in the window.
- How to test boundary cases (e.g., events exactly `W` milliseconds apart).

You are encouraged to:

- Run your program incrementally.
- Print intermediate results while debugging.
- Test edge cases.