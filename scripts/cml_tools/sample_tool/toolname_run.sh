#!/bin/bash
set -e
ml yq

# Change this to your config file name present in the same directory
CONFIG_FILE="toolname_config.yaml"

TAG=$(yq '.TAG' "$CONFIG_FILE")
ATTRIBUTE1=$(yq '.ATTRIBUTE1' "$CONFIG_FILE")
OUTPUT=$(yq '.OUTPUT' "$CONFIG_FILE")

#conda activate ml-env
ml bedtools
#ml torch
athena annotate-bins --track-list "$ATTRIBUTE1" "$ATTRIBUTE2" --output-bins "$OUTPUT/output_${TAG}_annotated_bins.bed"
