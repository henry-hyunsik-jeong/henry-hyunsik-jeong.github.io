#!/bin/bash
RELATIVE_DIR=`dirname "$BASH_SOURCE"`
CANONICAL_DIR=`readlink -f $RELATIVE_DIR`
CUR_DIR=${CANONICAL_DIR}

cd document-site
conda activate page