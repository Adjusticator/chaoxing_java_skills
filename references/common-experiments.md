# Common Java Course Experiments

## Classes And Objects

Check constructors, encapsulation, getters/setters, `static` use, and `toString`. Prefer `private` fields and narrow methods over `protected` fields unless inheritance is explicitly required. For beginner labs, prefer explicit code over clever abstractions.

Typical pitfalls:

- Public class name does not match file name
- Fields are left public when encapsulation is required
- Fields are made `protected` even though no subclass needs direct access
- Constructor does not initialize all required fields
- Floating-point output misses required precision

## Inheritance, Interfaces, Polymorphism

Confirm the exact relationship required by the prompt: `extends`, `implements`, abstract class, or interface. Use inheritance for true "is-a" relationships and composition for "has-a" relationships unless the prompt mandates otherwise. If the experiment is about polymorphism, demonstrate parent/interface references pointing to child objects.

Typical pitfalls:

- Overloading instead of overriding
- Missing `@Override`
- Parent class lacks no-arg constructor required by child constructors
- Access modifiers are too restrictive for overridden methods
- Subclassing only to reuse fields, when a contained member object would be clearer

## Date, Time, And Schedule Records

For date/time labs, first document the accepted input format, such as `id yyyy/mm/dd hh:mm:ss`, and any sentinel value such as `0`. Prefer `LocalDate`, `LocalTime`, `LocalDateTime`, and `DateTimeFormatter` when the assignment does not require custom classes. If custom `Date` and `Time` classes are required, put parsing, range validation, comparison, and formatting in focused helper methods rather than in `main`.

Typical pitfalls:

- Accessing `split` results before checking that date and time each have exactly three parts
- Letting invalid values such as month `13`, day `32`, hour `24`, or second `60` crash the program
- Ignoring incomplete records, such as an ID without both date and time
- Formatting output differently from the sample, especially padded versus non-padded date/time values
- Duplicating comparison methods with identical behavior

## Collections And Generics

Use `List` for ordered records, `Map` for ID lookup, and `Set` for uniqueness. Use `Comparator` for sorting by score, name, date, or ID.

Typical pitfalls:

- Comparing strings with `==`
- Removing from a list while iterating with an enhanced for-loop
- Sorting numeric strings lexicographically
- Forgetting duplicate-ID checks

## Exceptions And File I/O

Use `try-with-resources`. Keep paths relative to project root unless the assignment gives fixed paths.

Typical pitfalls:

- Scanner input newline issues after `nextInt`
- File not found because of IDE working directory
- Not specifying encoding for Chinese text
- Failing to close streams

## GUI Labs

For Swing, update UI on the Event Dispatch Thread with `SwingUtilities.invokeLater`. Separate event handlers from business logic enough that the logic remains testable.

Typical pitfalls:

- Null layout that breaks resizing
- Long-running work on the UI thread
- Missing input validation before parsing numbers
- Not refreshing table/list models after data changes

## JDBC CRUD Systems

Use `PreparedStatement`, close resources, and keep SQL/table creation scripts aligned with Java fields. Check whether the teacher expects MySQL, SQL Server, SQLite, or another database.

Typical pitfalls:

- Hard-coded local password in final submission
- SQL injection through string concatenation
- Driver dependency missing from classpath
- Mismatch between database column types and Java types

## Multithreading

Identify shared mutable state. Use `synchronized`, `Lock`, or thread-safe collections only where needed. Demonstrate thread names and deterministic enough output for a lab report.

Typical pitfalls:

- Calling `run()` instead of `start()`
- Assuming output order is deterministic
- Race conditions on counters
- Not shutting down thread pools

## Socket Programming

Keep protocol simple: one request per line or a documented message format. Use separate threads only when multiple clients are required.

Typical pitfalls:

- Server and client disagree on port or message termination
- Blocking forever on `readLine` because no newline was sent
- Not closing sockets
- Local firewall or occupied port confusion

## Data Structures And Algorithms

Prefer correctness and clear complexity explanation. Add small test cases for empty, one element, duplicate values, already sorted input, and reverse order.

Typical pitfalls:

- Off-by-one loop bounds
- Mutating input when the method should be pure
- Recursive base case missing
- Complexity claims in the report that do not match the implementation
