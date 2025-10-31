
#!/bin/bash
set -e
ml yq

CONFIG_FILE="config.pipelinetag.featuretag.yaml"

# Read config values using yq
TAG=$(yq '.TAG' "$CONFIG_FILE")
INPUT1=$(yq '.INPUT1' "$CONFIG_FILE")
SAMPLE_ANALYSIS_V =$(yq '.SAMPLE_ANALYSIS_V' "$CONFIG_FILE")
OUTPUT_DIR=$(yq '.OUTPUT_DIR' "$CONFIG_FILE")
LOG_LEVEL=$(yq '.LOG_LEVEL' "$CONFIG_FILE")

#every final output (not processed) reported here must contain the TAG and version of the analysises.

mkdir -p "$OUTPUT_DIR"

# Python and R scripts
python ../scripts/analysis/sample.py "$INPUT1" "../data/processed/sample/output_${SAMPLE_ANALYSIS_V}"

#run a tool on the output of the previous step
path/to/tool/tool.sh "../data/processed/sample/output_${SAMPLE_ANALYSIS_V}" "../data/processed/tool_name/output_${TAG}"

#run Rscript
ml R
Rscript "../data/processed/tool_name/output_${TAG}" "$OUTPUT_DIR/${TAG}_${SAMPLE_ANALYSIS_V}_results.txt" "$LOG_LEVEL"
