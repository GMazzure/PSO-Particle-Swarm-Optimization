import argparse
import sys

import src.CostFunctions as CostFunctions
from src.Trainer import Trainer


def main():
    """ feed arguments and start algorithm

    Args:
        args (): algorithm start args
    """
    args = parse_arguments(sys.argv[1:])

    print("Args: \n{")
    for arg, value in vars(args).items():
        print(f"  '{arg}': {value}")
    print("}")

    if args.function == 1:
        costFunction = CostFunctions.Schwefel()
    elif args.function == 2:
        costFunction = CostFunctions.fRaRastriginstrigin()
    else:
        costFunction = CostFunctions.Third()

    trainer = Trainer(costFn=costFunction,
                      scavangerCount=args.individualsCount,
                      max_it_without_optimization=args.max_it_without_optimization)
    trainer.run()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--runTimes', type=int,
                        help='Number of times to run the simulation', default=1)

    parser.add_argument('-f', '--function', type=int,
                        help='Function (1: Schwefel; 2: Rastrigin; 3:Third(unnamend).', default=1)

    parser.add_argument('-t', '--type', type=int,
                        help='Type of optimization. 1: Maximization. 2: Minimization', default=1)

    parser.add_argument('-i', '--individualsCount', type=int,
                        help='Number of individuals. default=100', default=100)

    parser.add_argument('-m', '--max_it_without_optimization', type=int,
                        help='Number of iterations in which the algorithm will try to optimize result', default=20)

    # parser.add_argument('-min','--min', type=int,
    #                     help='Minimo nas coordenadas.', default=0)

    # parser.add_argument('--max', type=int,
    #                     help='Maximo nas coordenadas ', default=100)

    # parser.add_argument('--chart', type=int,
    #                     help='Retorna os charts em vez da visualização', default=0)

    # parser.add_argument('--debug', type=int,
    #                     help='Modo debug.', default=0)

    return parser.parse_args(argv)


if __name__ == "__main__":
    main()
