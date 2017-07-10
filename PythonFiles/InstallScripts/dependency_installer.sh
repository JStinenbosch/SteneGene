#!/usr/bin/env bash

installBlast+(){
if which blastn > /dev/null; then
    echo Blast is already installed
else
    sudo apt-get install ncbi-blast+

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
    sudo apt-get install bedtools
fi
}

installClustalO(){
if which clustalo > /dev/null; then
    echo ClustalO is already installed
else
    sudo apt-get install clustalo
fi
}

installORFfinder(){
if [ -f ORFfinder ]; then
 echo ORFfinder is already available locally
else
 wget ftp://ftp.ncbi.nlm.nih.gov/genomes/TOOLS/ORFfinder/linux-i64/ORFfinder.gz
 gunzip ORFfinder.gz
 chmod +x ORFfinder
fi
}

installTkinter(){
    sudo apt-get install python3-tk
}

installWxWidgets(){
    sudo apt-get install wxwidgets
}

installBlast+
installBedtools
installClustalO
installORFfinder
installTkinter
installWxWidgets