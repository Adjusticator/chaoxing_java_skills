# Java Lab Workflow

## Requirement Intake

When starting a Java lab, collect the source of truth in this order:

1. Assignment document or teacher-provided prompt
2. Existing project files
3. Sample input/output and screenshots
4. Rubric, naming rules, submission rules, and deadline notes
5. User preferences only after course requirements are clear

If the assignment is a PDF or image, extract text first and keep exact wording for method names, menu labels, and output requirements.

## Deliverable Map

Create a short deliverable map before coding:

- Experiment folder: infer `实验一`, `实验二`, `实验三`, etc. from the PDF title, filename, or user message
- Code: required packages, classes, interfaces, methods, main entry point, and whether a single `Main.java` is best
- Data: input files, output files, database tables, initial seed data
- Tests: sample cases, self-designed cases, JUnit if required
- Report: sections, screenshots, command output, design diagrams only when the user or assignment asks for a report
- Packaging: zip naming, project folder naming, encoding, IDE expectations

Default to a runnable `.java` program folder named after the experiment number, such as `实验三/Main.java`. Do not create `.txt` artifacts unless explicitly requested.

## Project Inspection

Use fast local discovery:

```powershell
rg --files
rg "class |interface |enum |public static void main|TODO|FIXME|package "
```

Check:

- Whether packages match folder paths
- Whether there are duplicate public classes
- Whether `.class` files or old `bin` output are mixed into `src`
- Whether input files are expected relative to project root
- Whether the code is intended for IntelliJ, Eclipse, Maven, Gradle, or plain `javac`
- Whether the current workspace contains multiple experiments named `Main.java`; if so, compile only the current folder or current file
- Whether the target `实验几` folder already exists; if it does, work inside it without deleting unrelated user files

## Design Before Editing

For course labs, a small design note prevents many mistakes:

- Entity classes: fields, constructors, getters/setters, `toString`
- Service/manager classes: add, delete, update, query, sort, persist
- UI layer: console menu or GUI event handling
- Persistence layer: text file, serialization, or database
- Validation: duplicate IDs, missing IDs, invalid numeric input

Use simple designs unless the assignment explicitly asks for layered architecture.

## Implementation Order

1. Fix compile blockers first.
2. Implement domain classes and signatures required by the prompt.
3. Add business logic with simple tests or manual scripted input.
4. Add persistence or database code.
5. Polish menu/output text to match requirements.
6. Run full verification.
7. Leave the user with a runnable `.java` file or runnable folder named by experiment number. Write reports/documents only when requested.

## Handling Ambiguity

If the prompt is ambiguous but a reasonable assumption is low-risk, choose the simplest interpretation and state it. Ask the user only when the ambiguity changes the required deliverable, such as GUI vs console, database vs file storage, or a specific teacher-mandated format.
