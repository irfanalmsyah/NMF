import numpy, argparse
import als

def main(set_of_numbers, row, col, error=1e-7, iteration=100):
    set_of_numbers = [int(n) for n in set_of_numbers.split(',')]
    matrix = numpy.array(set_of_numbers).reshape(row, col)
    result = als.als(matrix, error, iteration)
    print("W: {}\n".format(result['W']))
    print("H: {}".format(result['H']))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('set_of_numbers', type=str, help='Comma-separated set of numbers to be processed')
    parser.add_argument('row', type=int, help='Row number')
    parser.add_argument('col', type=int, help='Column number')
    parser.add_argument('-e', '--error', type=float, default=0.0000000001, help='Error threshold')
    parser.add_argument('-i', '--iteration', type=int, default=100, help='Maximum number of iterations')
    args = parser.parse_args()

    main(args.set_of_numbers, args.row, args.col, args.error, args.iteration)
