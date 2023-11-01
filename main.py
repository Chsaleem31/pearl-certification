from pearl import Pearl
from helpers import run_tests

if __name__ == '__main__':
  pearl = Pearl('input.txt')
  pearl.optimize_placements()
  pearl.generate_output('generated_output.txt')

  # Run tests to check generated output
  run_tests()
