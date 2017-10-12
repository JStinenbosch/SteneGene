#!/usr/bin/env bash

installBlast+(){
if which blastn > /dev/null; then
    echo Blast is already installed
else
    brew install ncbi-blast+

# Should be replaced by this to support other linux distros
#    wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.6.0+-x64-linux.tar.gz
#    tar xzvf ncbi-blast-2.6.0+-x64-linux.tar.gz
#    ./configure && make && sudo make install
fi
}
installBedtools(){
if which bedtools > /dev/null; then
    echo Bedtools are already installed
else
    brew install bedtools
fi
}

installClustalO(){
if which clustalo > /dev/null; then
    b ClustalO is already installed
else
    brew install clustalo
fi
}

installORFfinder(){
if which getorf > /dev/null; then
 echo ORFfinder is already available locally
else
 brew install emboss
# Same problem here, should be replaced by something like this
# wget ftp://ftp.ncbi.nlm.nih.gov/genomes/TOOLS/ORFfinder/linux-i64/ORFfinder.gz
# gunzip ORFfinder.gz
# chmod +x ORFfinder
fi
}

installTkinter(){
    brew install python3-tk
}

installWxWidgets(){
    brew install wxwidgets
}

installBlast+
installBedtools
installClustalO
installORFfinder
installTkinter
installWxWidgets