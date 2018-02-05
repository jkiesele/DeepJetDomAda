
if [ ! $DEEPJETCORE ]
	then
       export DEEPJETCORE=../DeepJetCore
    fi

THISDIR=`pwd`
cd $DEEPJETCORE/
source lxplus_env.sh
cd $THISDIR
export PYTHONPATH=`pwd`/modules:$PYTHONPATH
export DEEPJET=`pwd`
