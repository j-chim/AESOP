import argparse
from helper.utils import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", "-i")
    parser.add_argument("--output_dir", "-o")
    args = parser.parse_args()

    spe = stanford_parsetree_extractor(args.output_dir)
    src_pure_parses, src_parses = spe.run(args.file_path)
    with open(args.file_path, "r") as f:
        src_lines = [line.strip("\n") for line in f]

    level = 3
    print("write diverse source file")
    # generate the future target parses from the frequencies list
    path = "processed-data/ParaNMT50-hf-refine/repe_statistics"

    with open(os.path.join(args.output_dir, f"level{level}_paranmt.source"), "w+") as output_file:
        with open(os.path.join(path, f"repe_para_{level}.txt"), "r") as f:
            frequency_lines = f.readlines()
        level_, freq = generate_dict(frequency_lines), generate_counts_dict(frequency_lines)
        for i in range(0, len(src_lines)):
            print(i)
            possible_drawn = step2_rouge(level_, freq, src_lines[i], level)[3]
            for possible in possible_drawn:
                output_file.write(f"{src_lines[i]}<sep>{src_parses[i]}<sep>{possible}\n")













