import sys

def read_flight_paths(r):
   '''Read flight paths data from reader r, returning lists of start, 
   finish, and energy.'''
  
   starts = []
   finishes = []
   energies = []

   energyOverhead = int(r.readline())
   for line in r:
     start, finish, energy = line.split()
     starts.append(int(start))
     finishes.append(int(finish))
     energies.append(int(energy))

 
   return (starts, finishes, energies)

def process_flight_paths(starts,finishes,energies):
   '''Return the paths that is optimal. Came home late last night,
      therefore will be working on this today/tomorrow whenever time permits. '''
  
   return starts[0]

if __name__ == "__main__":
   input_file = open(sys.argv[1], "r")
   starts, finishes, energies = read_flight_paths(input_file)
   print process_flight_paths(starts, finishes, energies)
   input_file.close()


