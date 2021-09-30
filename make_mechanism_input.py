from datetime import datetime
import numpy as np

from rmgpy.chemkin import load_chemkin_file

# rmg probably has a class that does this better. I think it's model. This is where doing the surface mechanism diff might come in handy...
# It's a good exercise in dealing with the different classes. Or maybe this is the warmup for the surface_mechanism diff


def write_mechanism_input_file(fname):
    with open(fname, 'w') as f:
        f.write(f'# Zacros mechanism input autogenerated with AutoKMC {datetime.now()}\n\n')


fname = "/home/moon/autokmc/task1/mechanism_input.dat"
# write_mechanism_input_file(fname)

my_cti = '/home/moon/methanol/perturb_5000/run_0000/cantera/chem_annotated.cti'
my_chem = '/home/moon/methanol/perturb_5000/run_0000/chemkin/chem_annotated-surface.inp'
my_dict = '/home/moon/methanol/perturb_5000/run_0000/chemkin/species_dictionary.txt'


# start with the gas species
my_chem = '/home/moon/autokmc/task0/co_zacros_add_gas/chemkin/chem_annotated-gas.inp'
my_dict = '/home/moon/autokmc/task0/co_zacros_add_gas/chemkin/species_dictionary.txt'

species_list, reaction_list = load_chemkin_file(my_chem, dictionary_path=my_dict)


for rxn in reaction_list:
    if rxn.index == 3:
        # print(rxn)
        print(rxn.kinetics.Ea * 4.3363E-2)  # kcal/mol to eV
        print(rxn.get_equilibrium_constant(900))

for spec in species_list:
    if '(30)' in spec.label or spec.label == '[O]OC([O])=O':
        print(spec)
        T = 900
        print(spec.get_enthalpy(T) * 1.03636E-05)  # convert to eV
    # print(spec.label)
# print(reaction_list)
