#! /bin/bash

export HOME=/usit/cere-utv01/u1/tvl
export HISTFILE=.bash_history
export PATH=$PATH:/local/opt/postgresql/bin
export PGUSER="cerebrum"
export PGSSLMODE="prefer"
export CEREBRUM_HOME="/cerebrum"
export PGHOST=dbpg-cere-utv.uio.no
export PGDATABASE="template1"
export CEREBRUM_HOME="/cerebrum/uio"
export PG_PW_FILE="${CEREBRUM_HOME}/etc/passwords/passwd-$PGUSER@$PGDATABASE@$PGHOST"
export PGPASSWORD=`cat $PG_PW_FILE| cut -f 2`
export PYTHONSTARTUP=~/.pythonrc

alias bofh="bofh --url http://cere-utv01.uio.no:2206 --set 'console_prompt=tvl_test> '"
alias bofhd="python ~/cerebrum/servers/bofhd/bofhd.py -c ~/uio/config.dat --logger-name=console --logger-level=DEBUG --port 2206 --unencrypted"
alias python="python2.6"

export PATH=.:/local/bin/python/:/uio/kant/usit-uait-u1/jsama/bin/:/local/bin/:/local/opt/oraclient10.2/product/10.2.0/bin:/local/opt/oraclient10.2/OPatch/:/local/opt/oraclient10.2/perl/bin:/uio/kant/usit-uait-u1/jsama/bin:/local/bin:/local/opt/oraclient10.2/product/10.2.0/bin:/local/opt/oraclient10.2/OPatch/:/local/opt/oraclient10.2/perl/bin:/usr/kerberos/bin:/usr/bin:/bin:/usr/sbin:/sbin:/local/bin:/local/opt/postgresql/bin:/site/bin:/local/opt/postgresql/bin:/site/bin:$PATH
#export PYTHONPATH=/site/tvl/uio/:/site/tvl/cerebrum:/uio/kant/usit-uait-u1/jsama/src/cerebrum:/site/lib/python2.5/site-packages/:/local/lib/python2.5:/usr/lib64/python2.6:.
#export PYTHONPATH=/site/tvl/uio/:/site/tvl/cerebrum:/uio/kant/usit-uait-u1/jsama/src/testconfig/uio:/usit/cere-utv01/u1/jsama/pylib/suds-0.4-py2.4.egg:/uio/kant/usit-uait-u1/jsama/src/cerebrum:/site/lib/python2.5/site-packages/:/uio/kant/usit-uait-u1/jsama/pylib:/usit/cere-utv01/u1/jsama/pylib/lib/python:/usit/cere-utv01/local/lib/python2.5/:.
#export PYTHONPATH=/site/tvl/uio:/site/tvl/src:/usit/cere-utv01/u1/jsama/pylib/suds-0.4-py2.4.egg:/site/lib/python2.5/site-packages/:/uio/kant/usit-uait-u1/jsama/pylib:/usit/cere-utv01/u1/jsama/pylib/lib/python:.

#export PYTHONPATH=.:/usit/cere-utv01/u1/tvl/src/sap2bas-xml-new-fileformat:/usit/cere-utv01/u1/tvl/uio/:/usit/cere-utv01/u1/tvl/src/cerebrum_sites/etc/uio/:/site/lib/python2.5/site-packages/:.
export PYTHONPATH=.:~/cerebrum:/usit/cere-utv01/u1/tvl/uio/:/usit/cere-utv01/u1/tvl/src/cerebrum_sites/etc/uio/:/site/lib/python2.5/site-packages/:.

source ~/.bashrc
