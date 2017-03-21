#!/usr/bin/python3

# This script plots the data produced by run_trials.sh

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy

CSV_FILE = 'results.csv'

def main():
    # read the data from the CSV files
    data = numpy.genfromtxt(CSV_FILE, delimiter=',', names=True)

    # plot training steps vs classification accuracy
    plt.plot(data['n'], data['false_positive'], 'r.', markersize=20)
    plt.plot(data['n'], data['false_negative'], 'g.', markersize=20)
    plt.plot(data['n'], data['accuracy'], 'b.', markersize=20)
    plt.title('Number of Training Steps vs Classification Accuracy \n and False Negative/Positive Rates')
    plt.xlabel('Number of Training Steps')
    plt.ylabel('Classification Accuracy')
    plt.grid(True)
    plt.savefig('training_steps_vs_accuracy.png')

if __name__=='__main__':
    main()
