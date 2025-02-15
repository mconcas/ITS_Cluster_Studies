import os
import yaml

run_number = 505645

os.system(f'alien.py ls /alice/data/2021/OCT/{run_number}/apass2/ > out.txt')
os.system(f'rm -rf {run_number}/*')





with open('out.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

if not os.path.exists(f'{run_number}'):
        os.makedirs(f'{run_number}')

if not os.path.exists('part_merging'):
        os.makedirs('part_merging')


input_dir = f'/alice/data/2021/OCT/{run_number}/apass2/'

for index,line in enumerate(lines):
    if(index>60): 
            continue
    if line[0:6] == 'o2_ctf':
        input_path = input_dir + line
        os.system(f' alien.py cp -T 32 {input_path}o2match_itstpc.root file:part_merging/o2match_itstpc.root{index}')
        os.system(f' alien.py cp -T 32 {input_path}o2trac_its.root file:part_merging/o2trac_its.root{index}')
        os.system(f' alien.py cp -T 32 {input_path}o2clus_its.root file:part_merging/o2clus_its.root{index}')
        os.system(f' alien.py cp -T 32 {input_path}o2_primary_vertex.root file:part_merging/o2_primary_vertex.root{index}')



os.system(f'hadd {run_number}/o2match_itstpc.root part_merging/o2match_itstpc.root*')
os.system(f'hadd {run_number}/o2clus_its.root part_merging/o2clus_its.root*')
os.system(f'hadd {run_number}/o2trac_its.root part_merging/o2trac_its.root*')
os.system(f'hadd {run_number}/o2_primary_vertex.root part_merging/o2_primary_vertex*')


os.system('rm -rf part_merging')
os.system('rm -rf out.txt')


