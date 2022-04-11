RELATIVE_DIR=`dirname "$BASH_SOURCE"`
CANONICAL_DIR=`readlink -f $RELATIVE_DIR`
CUR_DIR=${CANONICAL_DIR}

python run_before_deploy.py