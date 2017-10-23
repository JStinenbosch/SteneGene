#!/usr/bin/env bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    *)          machine="UNKNOWN:${unameOut}"
esac
echo ${machine}

installBlast+(){
if which blastn > /dev/null; then
    echo Blast is already installed
else
    case "${machine}" in
        Darwin) brew install ncbi-blast+;;
        Linux) sudo apt-get install ncbi-blast;;
    esac

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
    case "${machine}" in
        Darwin) brew install bedtools;;
        Linux) sudo apt-get install bedtools;;
    esac
fi
}

installClustalO(){
if which clustalo > /dev/null; then
    echo ClustalO is already installed
else
    case "${machine}" in
        Darwin) brew install clustalo;;
        Linux) sudo apt-get install clustalo;;
    esac
fi
}

installORFfinder(){
if which getorf > /dev/null; then
 echo ORFfinder is already installed
else
    case "${machine}" in
        Darwin) brew install emboss;;
        Linux) sudo apt-get install emboss;;
    esac
# Same problem here, should be replaced by something like this
# wget ftp://ftp.ncbi.nlm.nih.gov/genomes/TOOLS/ORFfinder/linux-i64/ORFfinder.gz
# gunzip ORFfinder.gz
# chmod +x ORFfinder
fi
}

installBlast+
installBedtools
installClustalO
installORFfinder