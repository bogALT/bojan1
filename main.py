# My Objects:
from CyclomaticComplexityAnalyzer import CyclomaticComplexityAnalyzer
from Downloader import Downlaoder
from FolderComparator import FolderComparator
from JARExtractor import JARExtractor
from JLCodeAnalyzer import JLCodeAnalyzer
from MavenRepositorySearcher import MavenRepositorySearcher
import tkinter as tk
from tkinter import ttk
import csv

def separator():
    print("\n"+"-"*80)

def read_csv():
    file_names = []
    with open('gav_input.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            g = row[0]
            a = row[1]
            file_names.append(g + "_" + a)
    print(file_names)



if __name__ == '__main__':
    print("Starting the program..")
    # read_csv()    # automatize searching gavs -> fill an array with GAVs
    # define GAV - only for testing, later input from terminale
    g = "net.sf.mpxj"
    a = "mpxj"
    v = "11.0.0"

    '''    # download the JAR file from MVN repository
    dl = Downlaoder()
    jar_file = dl.download(g, a, v)

    separator()
    # Extract java files from JAR to oDir
    je = JARExtractor()
    oDir = je.extract(jar_file)

    separator()
    # count LOCs per method
    jlca = JLCodeAnalyzer(oDir)
    avg_locs_per_method = jlca.start()
    print(f"On average we have {avg_locs_per_method} locs per method\n")

    separator()
    print("\nStarting Cyclomatic complexity analysis")
    cca = CyclomaticComplexityAnalyzer(oDir)
    cca.start()'''

    separator()

    mrs = MavenRepositorySearcher()

    # ----------------------------------------------------------------
    #               AUTOMATIZING THE ANALYSIS
    # only when you have no specific versions to look for
    #
    print("Searching for last version of ", g)
    last = mrs.search_last_version(g, a)
    print("Last version = ", last)
    # ----------------------------------------------------------------


    # search the Maven Repository for version - 1
    print("Searching for version precedent to ", v)
    precedent = mrs.search_GAV(g, a, v)  # check what to do when incomplete parameters are set
    print(f"Version {v} has predecessor {precedent}")

    separator()
    # download the precedent version
    # download the JAR file (version -1) from MVN repository
    #dl = Downlaoder()
    jar_file = dl.download(g, a, precedent)

    # Extract java files from JAR to oDir
    #je = JARExtractor()
    oDir_precedent = je.extract(jar_file)

    separator()
    print(f"Comparing {oDir_precedent} and {oDir}:")

    # create Directory comparator
    comparator = FolderComparator(oDir, oDir_precedent)
    num_different_files, num_files_examined = comparator.count_different_files()
    print(f"Changed files: {num_different_files}")
    print(f"Examined files: {num_files_examined}")

