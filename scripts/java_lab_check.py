#!/usr/bin/env python3
"""Compile and optionally run a plain Java course-lab project."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


EXCLUDED_DIRS = {".git", ".idea", ".vscode", "bin", "build", "out", "target"}


def find_java_files(project: Path, src: str | None, single_file: str | None) -> list[Path]:
    if single_file:
        path = (project / single_file).resolve()
        try:
            path.relative_to(project)
        except ValueError:
            raise SystemExit(f"Java file must be inside project directory: {path}")
        if not path.exists():
            raise SystemExit(f"Java file does not exist: {path}")
        if path.suffix != ".java":
            raise SystemExit(f"--file must point to a .java file: {path}")
        return [path]

    root = project / src if src else project
    if not root.exists():
        raise SystemExit(f"Source path does not exist: {root}")

    files: list[Path] = []
    for path in root.rglob("*.java"):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(project).parts):
            continue
        files.append(path)
    return sorted(files)


def run_command(command: list[str], cwd: Path, stdin_text: str | None = None) -> int:
    print(f"[cmd] {' '.join(command)}")
    completed = subprocess.run(
        command,
        cwd=str(cwd),
        input=stdin_text,
        text=True,
        capture_output=True,
    )
    if completed.stdout:
        print("[stdout]")
        print(completed.stdout.rstrip())
    if completed.stderr:
        print("[stderr]")
        print(completed.stderr.rstrip())
    print(f"[exit] {completed.returncode}")
    return completed.returncode


def read_stdin_text(args: argparse.Namespace) -> str | None:
    if args.stdin_file:
        return Path(args.stdin_file).read_text(encoding=args.stdin_encoding)
    if args.stdin is not None:
        return args.stdin
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile and run a plain Java lab project.")
    parser.add_argument("--project", default=".", help="Project root directory.")
    parser.add_argument("--src", help="Optional source directory relative to project root, e.g. src.")
    parser.add_argument("--file", help="Compile only one .java file relative to project root, e.g. Main.java.")
    parser.add_argument("--main", help="Main class to run, including package name if any.")
    parser.add_argument("--encoding", default="UTF-8", help="Source file encoding for javac.")
    parser.add_argument("--out", default="bin", help="Compilation output directory.")
    parser.add_argument("--compile-only", action="store_true", help="Compile without running.")
    parser.add_argument("--stdin", help="Text passed to the Java program stdin.")
    parser.add_argument("--stdin-file", help="File whose content is passed to stdin.")
    parser.add_argument("--stdin-encoding", default="UTF-8", help="Encoding for --stdin-file.")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    if not project.exists():
        raise SystemExit(f"Project directory does not exist: {project}")

    javac = shutil.which("javac")
    java = shutil.which("java")
    if not javac or not java:
        raise SystemExit("javac/java not found on PATH. Install a JDK and add it to PATH.")

    java_files = find_java_files(project, args.src, args.file)
    if not java_files:
        raise SystemExit("No .java files found.")

    out_dir = project / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    compile_cmd = [javac, "-encoding", args.encoding, "-d", str(out_dir)]
    compile_cmd.extend(str(path) for path in java_files)
    compile_code = run_command(compile_cmd, project)
    if compile_code != 0 or args.compile_only:
        return compile_code

    if not args.main:
        print("[info] Compilation succeeded. No --main provided, so run step skipped.")
        return 0

    stdin_text = read_stdin_text(args)
    run_cmd = [java, "-cp", str(out_dir), args.main]
    return run_command(run_cmd, project, stdin_text)


if __name__ == "__main__":
    sys.exit(main())
