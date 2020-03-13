set -e

MC_BUILD_DIR='build'

mc_main() {
    if [[ -e ${MC_BUILD_DIR} ]]; then
        echo "== Exiting because build directory exists"
        exit 1
    fi

    mkdir ${MC_BUILD_DIR}
    cd ${MC_BUILD_DIR}
    cmake ..
    make install rpm
}

mc_main
