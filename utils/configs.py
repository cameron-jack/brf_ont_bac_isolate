# guppy base calling
guppy_basecaller = (
    "/home/groups/schwessinger/guppy/6.5.7/ont-guppy/bin/guppy_basecaller"
)
guppy_kit = "SQK-RBK114-96"
guppy_model = "dna_r10.4.1_e8.2_400bps_sup.cfg"

# dorado base calling
dorado_basecaller = (
    "/home/groups/schwessinger/dorado/0.7.0/bin/dorado"
)
dorado_kit = "SQK-RBK114-96"
dorado_model = "sup"

nextflow = "nextflow"
wf_clone_validation = "epi2me-labs/wf-clone-validation"
nanoFilt = "NanoFilt"
alignment_sh_script = (
    "/media/nvme/MinKNOW/OtherSequencing/simple_plasmid/utils/alignment.sh"
)

# environment should be in full path
# Conda environment path to nanofilt
nanofilt_env = "/home/groups/schwessinger/condaEnvs/nanofilt-env"

# bin path to minimap2 and samtools, ends without '/'
# ${path2bin}/minimap2
# ${path2bin}/samtools
path2bin = "/media/nvme/MinKNOW/OtherSequencing/simple_plasmid/bin"

nthreads = "8"
