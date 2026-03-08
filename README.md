# Worldbuilde

Worldbuilde lets you organize your creative universe from files (.docx, .pdf, .xlsx, .pptx, .csv, etc) into queryable markdown, plot-building tools, and lore support.

## How To Use

1. **Upload Prompt**  
   Place your files into `input_files/` (docx, pdf, pptx, xlsx, csv, etc).
2. **Convert to Markdown**  
   Run `md_creator.py` and follow the prompts for category and file selection.  
   This creates structured markdown in `docs/` and updates `docs/index.md`.
3. **AI Keyword Finder**  
   Optionally run `ai_keyword_finder.py` to discover connections or get writing prompts.
4. **Automated Index**  
   On every push, GitHub Actions runs basic checks and updates docs/index.md.

## Dependencies

```sh
pip install python-docx python-pptx PyPDF2 pandas openpyxl
```

## Upload & Convert Example

```python
# Example CLI run:
python md_creator.py
```
