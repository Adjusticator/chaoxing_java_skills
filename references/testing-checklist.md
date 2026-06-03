# Java Lab Testing Checklist

## Compile Checks

- Compile from a clean output directory.
- Verify package names match folder paths.
- Remove or ignore stale `.class` files inside `src`.
- Use `javac -encoding UTF-8` for Chinese source/comments unless the project proves another encoding.
- Confirm the main class name is correct, including package prefix.
- For single-file labs, compile only `Main.java` in its own folder to avoid duplicate `Main` classes from other experiments.
- Verify the program lives in the correct experiment-number folder, such as `实验三/Main.java`, before finalizing.

## Console Program Checks

Prepare scripted input for:

- A complete happy path
- Empty input or sentinel-only input, such as only `0`, when records are optional
- Invalid menu choice
- Invalid number or empty field if input validation exists
- Incomplete records where a required token is missing
- Malformed structured fields, such as a bad date or time string
- Out-of-range values, such as month `13`, day `32`, hour `24`, minute/second `60`, or negative IDs when IDs must be positive
- Add/query/update/delete flow
- Exit path

When using `Scanner`, watch for newline consumption after `nextInt`, `nextDouble`, or `next`.
When using `split`, verify the resulting array length and non-empty parts before parsing integers.

## Persistence Checks

For file/database labs:

- Add data, exit, restart, and query the same data.
- Test missing file behavior on first run.
- Test duplicate IDs.
- Test corrupted or malformed data if the code claims to handle it.
- Confirm relative paths work from project root.

## JUnit Checks

If JUnit is present:

- Keep tests independent.
- Use clear Arrange-Act-Assert structure.
- Add boundary cases, not only sample cases.
- Avoid relying on test execution order.

## Hidden-Judge Awareness

If the lab may be auto-graded:

- Match required class names, method signatures, packages, and output format exactly.
- Avoid extra prompts in output when the grader expects raw answers.
- Send invalid-input diagnostics to `System.err` or suppress them when the judge expects exact `System.out`.
- Do not require absolute local paths.
- Do not read from files unless required.
- Keep public APIs stable.
- Prefer one `Main.java` with one public class unless the assignment requires multiple public classes or packages.

## Report Evidence

Record:

- Compile command or IDE run result
- At least one normal test output
- At least one edge/invalid test output when relevant
- Screenshots for GUI/database experiments if the report requires them
- Explanation of any known limitation
