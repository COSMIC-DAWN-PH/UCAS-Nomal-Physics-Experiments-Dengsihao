#!/usr/bin/env python3
"""Preprocess a physics experiment report folder.

This helper matches the layout used by this repository's ``dsh`` examples:
each experiment is normally a self-contained directory containing its .tex
file, analysis scripts, images, tables, and sometimes an image subdirectory
named fig/Fig/Figure.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tif", ".tiff", ".webp"}
IMAGE_DIR_NAMES = ("Figure", "figure", "Fig", "fig", "Figures", "figures")


def repo_root() -> Path:
    return Path.cwd().resolve()


def resolve_experiment_folder(folder: str) -> Path:
    raw = Path(folder).expanduser()
    candidates = [
        raw,
        repo_root() / raw,
        repo_root() / "dsh" / raw,
    ]
    for candidate in candidates:
        if candidate.is_dir():
            return candidate.resolve()
    raise FileNotFoundError(f"Cannot find experiment folder: {folder}")


def resolve_pdf(pdf_name: str, experiment_dir: Path) -> Path:
    raw = Path(pdf_name).expanduser()
    candidates = [
        raw,
        repo_root() / raw,
        experiment_dir / raw,
        repo_root() / "讲义" / raw,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()

    matches = list(experiment_dir.rglob(pdf_name))
    lecture_dir = repo_root() / "讲义"
    if lecture_dir.is_dir():
        matches += list(lecture_dir.rglob(pdf_name))
    if matches:
        return matches[0].resolve()

    raise FileNotFoundError(f"Cannot find PDF manual: {pdf_name}")


def import_pdf_reader():
    try:
        from PyPDF2 import PdfReader  # type: ignore

        return PdfReader
    except ImportError:
        try:
            from pypdf import PdfReader  # type: ignore

            return PdfReader
        except ImportError as exc:
            raise RuntimeError("Missing PDF dependency. Install with: python -m pip install PyPDF2") from exc


def extract_pdf_text(pdf_path: Path, output_path: Path) -> None:
    reader_cls = import_pdf_reader()
    reader = reader_cls(str(pdf_path))
    parts: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        parts.append(f"\n\n===== Page {index} =====\n{text.strip()}\n")
    output_path.write_text("".join(parts).strip() + "\n", encoding="utf-8")


def safe_stem(value: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_.")
    return stem or "image"


def needs_rename(path: Path) -> bool:
    return path.stem != safe_stem(path.stem) or " " in path.name


def image_dirs(experiment_dir: Path) -> list[Path]:
    dirs = [experiment_dir / name for name in IMAGE_DIR_NAMES if (experiment_dir / name).is_dir()]
    return dirs or [experiment_dir]


def rename_images(experiment_dir: Path) -> list[tuple[Path, Path]]:
    renamed: list[tuple[Path, Path]] = []
    for directory in image_dirs(experiment_dir):
        images = sorted(p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS)
        counter = 1
        for image in images:
            if not needs_rename(image):
                continue
            while True:
                target = directory / f"fig{counter:03d}{image.suffix.lower()}"
                counter += 1
                if not target.exists():
                    break
            image.rename(target)
            renamed.append((image, target))
    return renamed


def copy_self_to_root() -> None:
    target = repo_root() / "workflow_preprocess.py"
    source = Path(__file__).resolve()
    if source != target:
        shutil.copy2(source, target)


def write_manifest(experiment_dir: Path, renamed: list[tuple[Path, Path]], pdf_path: Path) -> None:
    image_files = sorted(
        p.relative_to(experiment_dir).as_posix()
        for p in experiment_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    )
    lines = [
        "# Preprocess Manifest",
        "",
        f"- Experiment folder: {experiment_dir}",
        f"- PDF manual: {pdf_path}",
        f"- Extracted text: {experiment_dir / 'extracted_manual.txt'}",
        "",
        "## Images",
        *[f"- {name}" for name in image_files],
        "",
        "## Renamed Images",
    ]
    if renamed:
        for old, new in renamed:
            lines.append(f"- {old.relative_to(experiment_dir).as_posix()} -> {new.relative_to(experiment_dir).as_posix()}")
    else:
        lines.append("- None")
    (experiment_dir / "preprocess_manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Prepare an experiment folder for physics report generation.")
    parser.add_argument("experiment_folder", help="Experiment folder path or a folder name under dsh/")
    parser.add_argument("pdf_manual", help="Manual PDF path, or a filename under the experiment folder or 讲义/")
    parser.add_argument(
        "--install-root-wrapper",
        action="store_true",
        help="Copy this helper to ./workflow_preprocess.py for compatibility with older skill text.",
    )
    args = parser.parse_args(argv)

    experiment_dir = resolve_experiment_folder(args.experiment_folder)
    pdf_path = resolve_pdf(args.pdf_manual, experiment_dir)
    output_path = experiment_dir / "extracted_manual.txt"

    extract_pdf_text(pdf_path, output_path)
    renamed = rename_images(experiment_dir)
    write_manifest(experiment_dir, renamed, pdf_path)
    if args.install_root_wrapper:
        copy_self_to_root()

    print(f"Experiment folder: {experiment_dir}")
    print(f"PDF manual: {pdf_path}")
    print(f"Extracted text: {output_path}")
    print(f"Renamed images: {len(renamed)}")
    print(f"Manifest: {experiment_dir / 'preprocess_manifest.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
