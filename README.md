
# Lowther Lab Sample Project (Development Template)

This repository is a **sample project layout** for analyses in the Lowther Lab.  
It is intended as a lightweight **template** for organizing:

- Input data and intermediate outputs  
- Analysis scripts (Python / R / shell)  
- Reusable I/O utilities  
- Simple, tag-driven pipelines

The code and configuration files here are illustrative rather than a fully
working pipeline. Adapt and extend them for your own projects.

---

## Repository Structure

```text
Lowther_lab_sample_project_dev/  # Repo root (analysis-focused project template)
├── config/                                     # Central configuration (single source of truth)
│   └── input_adds.txt                          # Logical input names → file paths mapping
├── data/                                       
│   ├── input/                                  # Inputs that are smaller than 50MB
│   │   ├── file.log                            # The log file explains where the input files come from also it contains the log of their changes (new versions; v1->v2) 
│   │   └── sample_input.csv                    
│   ├── processed/                              # Intermediate outputs produced by analyses; not final reportable results. Mostly to be used in the next steps of anlaysis.
│   │   ├── analysis/                           
│   │   │   └── sampleAN/                       
│   │   │       └── table.tsv                   
│   │   └── README.md                           # Notes on intermediate outputs
│   └── temp/                                   # Scratch space for temporary files (safe to clear)
├── docs/                                       # High-level documentation / notes
│   └── analysis_description.txt                # Human-readable overview of analyses in plain language
├── output/                                     # Report-ready outputs (tables/plots) for sharing
│   ├── plots/                                  
│   │   ├── analysis/                           
│   │   │   └── sampleAN_sk/                    
│   │   │       └── plt1.png                    
│   │   └── pipeline/                           
│   │       └── sample_pipeline_plt.png         
│   └── tables/                                 
│       ├── analysis/                           
│       │   └── sampleAN_sk/                    
│       │       └── table1.tsv                  
│       └── pipeline/                           
│           └── table1.tsv                      
├── scripts/                                    # All code (analysis modules, pipelines, utilities)
│   ├── analysis/                               # Main analysis scripts (reproducible, parameterized)
│   │   ├── sketch/                             # sketch analyses (prototype area)
│   │   │   ├── __init__.py                     
│   │   │   └── sampleAN.py                     # Example sketch analysis script
│   │   ├── __init__.py                         
│   │   └── sample.py                           # Example analysis script (skeleton)
│   ├── cml_tools/                              # Wrappers/configs for external command-line tools
│   │   └── sample_tool/                        
│   │       ├── toolname_config.yaml            
│   │       └── toolname_run.sh                 
│   ├── code_blocks/                            # Reusable fragments + small test units
│   │   ├── code_archive.py                     # Archived reusable code snippets
│   │   └── test_units.py                       # Small checks / test units
│   ├── IOmanager/                              # I/O utilities (load data + resolve names)
│   │   ├── __init__.py                         
│   │   ├── dt_loader.py                        # Data loading helpers
│   │   └── name_resolver.py                    # Resolves logical names + stamps (git/time)
│   ├── pipeline/                               # Pipeline; combining several analyses and cml-tools (orchestration entrypoints)
│   │   ├── config.pipelinetag.featuretag.yaml  
│   │   └── run_pipelinetag.sh                  
│   └── plotting/                               # Reusable plotting helpers
│       ├── __init__.py                         
│       └── analysis_sample.py                  
├── .gitignore                                  # Git ignore rules (outputs/temp/IDE files, etc.)
└── README.md                                   # Project-level documentation (how to run + conventions)

```

---

## Requirements

This template assumes access to:

- **Python** (3.x) with:
  - `pandas`
- **R** (optional; for downstream steps in the example pipeline)
- **yq** (YAML processor) available as a module or on the `PATH`
- A Unix-like environment (Linux / macOS) for running the shell scripts

On many HPC systems, these are loaded via environment modules, e.g.:

```bash
ml python
ml R
ml yq
```

Adjust to your local environment / module system.

---

## Configuration: `config/input_adds.txt`

The file `config/input_adds.txt` maps logical names to file paths, one per line:

```text
# Comment lines start with '#'
sample_input: ./data/input/sample_input.csv
another_input: /path/to/another_input.tsv
```

- Lines beginning with `#` or empty lines are ignored.
- Keys and values are separated by the first `:` on the line.
- These logical names are used by the I/O utilities in `scripts/IOmanager`.

---

## I/O Utilities

### `scripts/IOmanager/add_resolver.py`

Key functions:

- `get_file_name(fn)`  
  Looks up `fn` in `config/input_adds.txt` and returns the corresponding path.

- `get_git_mark()`  
  Returns the first 4 characters of the current git commit hash (or `None` on failure).

- `get_time_mark()`  
  Returns a simple date–time string of the form `MM-DD-HH-MM`.

These helpers can be used to:

- Resolve input files by a logical name rather than hard-coding paths.
- Stamp outputs with a git commit and timestamp for reproducibility.

### `scripts/IOmanager/dt_loader.py`

Provides a generic data loader pattern:



Usage example:

```python
from IOmanager.dt_loader import load_dt

df = load_dt("sample_input", "sample_input_reader") # first is the data file name in input_adds.txt, second is the function name in IOmanager.dt_loader
```

You can define additional loader functions (e.g., for TSV, parquet, etc.) and call them via `load_dt`.

---

## Example Analysis Scripts

### `scripts/analysis/sample.py`

This file illustrates the pattern for a finalized (ready to use, with a set of inputs and outputs) analysis script:

- Defines an **analysis name** (`AN`) and **version** (`VN`).
- Reads inputs from `sys.argv`.
- Produces outputs in `data/processed/analysis_<AN>/output_<VN>.tsv`.

The current file is a **skeleton** and needs to be completed before use (e.g., define `result`, create the output directory, etc.). Use it as a template for your own analyses.

### Sketch Analyses
This is the playground for exploratory data analysis and prototyping. After an analysis is finilized it should be moved to the main analysis directory.
`scripts/analysis/sketch/sample.py` and `docs/sketch_analysis_ext.txt` show how to keep “scratch” / exploratory analyses separated from the main, reproducible analysis code.

---

## Example Pipeline

A pipeline is a set of analyses and tools wired together to process data from raw inputs to final results.

The `scripts/pipeline` directory shows one way to wire analyses together with a YAML config and a bash runner.

### Config: `config.pipelinetag.featuretag.yaml`

Example structure:

```yaml
TAG: "pipeline_TAG"          # Descriptive tag (e.g., data version, cohort)
INPUT1: "data/input1.csv"    # Path or logical input
SAMPLE_ANALYSIS_V: 1         # Version number for the analysis
OUTPUT_DIR: "results/output_directory"
LOG_LEVEL: "INFO"
```

### Runner: `run_pipelinetag.sh`

This bash script demonstrates:

- Loading `yq` to read YAML values.
- Creating the output directory.
- Running:
  - a Python analysis step,
  - an external tool,
  - and an R script on the results.

You will need to:

- Fix paths, variable names (e.g., spacing around `=`), and commands.
- Replace placeholder lines like `path/to/tool/tool.sh` with real tools.
- Point the R script to a real `.R` file.

Use it as a starting point for building a reproducible pipeline around your own analyses.

---

## Code Blocks and Tests

- `scripts/code_blocks/code_archive.py`  
  Stores small code fragments that may be reused later.

- `scripts/code_blocks/test_units.py`  
  Contains small test functions (e.g., `TU_1` checks that all genes in an annotation table are longer than 200 bases).  
  These can be imported and used in QC steps.

---

## Outputs

- **Intermediate data** should be written under `data/processed/`, ideally in analysis-specific subdirectories (e.g., `data/processed/analysis_sample/`).
- **Final results** (tables, figures) should be written under `output/` and `output/plots/`.

Example:

```text
data/processed/analysis_sample/output_v1.tsv
output/plots/analysis/sample_plt1.png
```

---

## Adapting This Template

To use this project structure for your own work:

1. **Clone or copy** this repository.
2. Update:
   - `config/input_adds.txt` with your own logical input names.
   - `scripts/analysis/sample.py` (or create new analysis scripts).
   - `scripts/pipeline/config*.yaml` and `run_*.sh` to reflect your pipeline.
3. Keep:
   - Raw inputs in `data/input/`
   - Intermediate tables in `data/processed/`
   - Final figures/tables in `output/`
   - Notes and design sketches in `docs/`

This template is intentionally minimal, so that each lab project can extend it in the direction that best fits its analysis needs.
