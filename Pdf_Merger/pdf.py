import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merge_obj = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merge_obj.append(pdf)
    merge_obj.write('merged.pdf')


pdf_combiner(inputs)
